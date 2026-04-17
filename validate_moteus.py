"""
validate_moteus.py — Volumetric & Symmetric-Difference Comparison
Compares original STEP/STP files against rebuilt output STL files.

INSTALL (run once):
    pip3 install trimesh manifold3d numpy cadquery
    # OR if using build123d instead of cadquery:
    pip3 install trimesh manifold3d numpy build123d

RUN:
    python3 validate_moteus.py
"""

import os
import sys
import struct
import tempfile
import numpy as np

# ─── trimesh ──────────────────────────────────────────────────
try:
    import trimesh
    HAS_TRIMESH = True
except ImportError:
    HAS_TRIMESH = False
    print("[WARNING] trimesh not found. Run: pip3 install trimesh manifold3d")

# ─── STEP loader: try cadquery first, then build123d ──────────
HAS_CQ = HAS_B123 = False
try:
    import cadquery as cq
    HAS_CQ = True
except ImportError:
    pass

if not HAS_CQ:
    try:
        import build123d as b123
        HAS_B123 = True
    except ImportError:
        pass

if not HAS_CQ and not HAS_B123:
    print("[WARNING] No STEP loader found.")
    print("  Install one:  pip3 install cadquery   OR   pip3 install build123d")


# ══════════════════════════════════════════════════════════════
#  STEP → temp STL conversion
# ══════════════════════════════════════════════════════════════

def step_to_temp_stl(step_path: str) -> str | None:
    """
    Convert a STEP/STP file to a temporary STL file.
    Returns the path to the temp STL, or None on failure.
    """
    tmp = tempfile.NamedTemporaryFile(suffix=".stl", delete=False)
    tmp.close()
    tmp_path = tmp.name

    if HAS_CQ:
        try:
            shape = cq.importers.importStep(step_path)
            cq.exporters.export(shape, tmp_path)
            return tmp_path
        except Exception as e:
            print(f"    [cadquery error] {e}")

    if HAS_B123:
        try:
            from build123d import import_step, export_stl, Mesher
            shape = import_step(step_path)
            # build123d ≥ 0.7 API
            try:
                export_stl(shape, tmp_path)
            except TypeError:
                m = Mesher()
                m.add_shape(shape)
                m.write(tmp_path)
            return tmp_path
        except Exception as e:
            print(f"    [build123d error] {e}")

    os.unlink(tmp_path)
    return None


# ══════════════════════════════════════════════════════════════
#  Raw STL helpers  (carried over from original validate.py)
# ══════════════════════════════════════════════════════════════

def _is_binary_stl(path):
    with open(path, 'rb') as f:
        hdr = f.read(80)
    return not (hdr[:5] == b'solid' and hdr[5:6] in (b' ', b'\n', b'\r'))

def _get_triangles(path):
    tris = []
    if _is_binary_stl(path):
        with open(path, 'rb') as f:
            f.read(80)
            n = struct.unpack('<I', f.read(4))[0]
            for _ in range(n):
                d = struct.unpack('<12fH', f.read(50))
                tris.append([d[3:6], d[6:9], d[9:12]])
    else:
        verts = []
        with open(path, 'r', errors='ignore') as f:
            for line in f:
                s = line.strip()
                if s.startswith('vertex'):
                    p = s.split()
                    verts.append([float(p[1]), float(p[2]), float(p[3])])
        for i in range(0, len(verts) - 2, 3):
            tris.append([verts[i], verts[i+1], verts[i+2]])
    return np.array(tris, dtype=np.float64)

def volume_from_stl(path):
    """Signed-volume (divergence theorem) on raw STL triangles."""
    total = 0.0
    for tri in _get_triangles(path):
        v1, v2, v3 = tri
        total += np.dot(v1, np.cross(v2, v3)) / 6.0
    return abs(total)


# ══════════════════════════════════════════════════════════════
#  Orientation search  (all 24 proper axis-aligned rotations)
# ══════════════════════════════════════════════════════════════

def _all_24_rotations():
    from itertools import permutations, product
    rots = []
    for perm in permutations([0, 1, 2]):
        for signs in product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, j in enumerate(perm):
                R[i, j] = signs[i]
            if round(np.linalg.det(R)) == 1:
                rots.append(R)
    return rots

ALL_24 = _all_24_rotations()

def _centre(pts):
    return pts - (pts.min(axis=0) + pts.max(axis=0)) / 2.0

def _best_rotation(pts_a_raw, pts_b_raw, subsample=1000):
    rng = np.random.default_rng(0)
    pa  = _centre(pts_a_raw)
    pb  = _centre(pts_b_raw)
    ia  = rng.choice(len(pa), min(subsample, len(pa)),  replace=False)
    ib  = rng.choice(len(pb), min(subsample, len(pb)),  replace=False)
    pa_s, pb_s = pa[ia], pb[ib]
    best_d, best_R = np.inf, np.eye(3)
    for R in ALL_24:
        pb_rot = (R @ pb_s.T).T
        diff   = pa_s[:, None, :] - pb_rot[None, :, :]
        d      = np.sqrt((diff**2).sum(axis=2)).min(axis=1).mean()
        if d < best_d:
            best_d, best_R = d, R
    return best_R


# ══════════════════════════════════════════════════════════════
#  Symmetric difference  (orientation-aware, requires trimesh)
# ══════════════════════════════════════════════════════════════

def symmetric_difference(stl_a: str, stl_b: str):
    """
    Returns (sym_diff_mm3, orig_vol_mm3, error_string).
    error_string is None on success.
    """
    if not HAS_TRIMESH:
        return None, None, "trimesh not installed"
    try:
        a = trimesh.load(stl_a, force='mesh')
        b = trimesh.load(stl_b, force='mesh')

        a.apply_translation(-a.bounding_box.center_mass)
        b.apply_translation(-b.bounding_box.center_mass)

        best_R = _best_rotation(np.array(a.vertices), np.array(b.vertices))
        T = np.eye(4); T[:3, :3] = best_R
        b.apply_transform(T)

        trimesh.repair.fill_holes(a)
        trimesh.repair.fill_holes(b)

        if not a.is_watertight or not b.is_watertight:
            return None, None, "open-shell mesh (boolean ops unavailable)"

        a_minus_b = trimesh.boolean.difference([a, b], engine='manifold')
        b_minus_a = trimesh.boolean.difference([b, a], engine='manifold')

        v_amb = abs(a_minus_b.volume) if a_minus_b is not None and len(a_minus_b.faces) > 0 else 0.0
        v_bma = abs(b_minus_a.volume) if b_minus_a is not None and len(b_minus_a.faces) > 0 else 0.0

        return v_amb + v_bma, abs(a.volume), None
    except Exception as e:
        return None, None, str(e)


# ══════════════════════════════════════════════════════════════
#  Core comparison
# ══════════════════════════════════════════════════════════════

def compare(part_name: str, orig_step: str, output_stl: str, results: list):
    """
    Compute volumetric difference and symmetric difference.
    Appends a result dict to `results`.
    """
    rec = {"name": part_name, "vol_diff": None, "vol_pct": None,
           "sym_diff": None, "sym_pct": None, "note": ""}

    # ── check output STL exists ───────────────────────────────
    if not os.path.exists(output_stl):
        rec["note"] = "output STL not found"
        results.append(rec)
        return

    # ── check original STEP exists ────────────────────────────
    if not os.path.exists(orig_step):
        rec["note"] = "original STEP not found"
        results.append(rec)
        return

    # ── convert STEP → temp STL ───────────────────────────────
    tmp_stl = step_to_temp_stl(orig_step)
    if tmp_stl is None:
        rec["note"] = "STEP conversion failed"
        results.append(rec)
        return

    try:
        # ── volumetric difference ─────────────────────────────
        v_orig    = volume_from_stl(tmp_stl)
        v_out     = volume_from_stl(output_stl)
        vol_diff  = abs(v_orig - v_out)
        vol_pct   = vol_diff / v_orig * 100 if v_orig > 0 else 0.0

        rec["vol_diff"] = vol_diff
        rec["vol_pct"]  = vol_pct

        # ── symmetric difference ──────────────────────────────
        sym_diff, orig_vol, err = symmetric_difference(tmp_stl, output_stl)
        if sym_diff is not None:
            sym_pct = sym_diff / orig_vol * 100 if orig_vol and orig_vol > 0 else 0.0
            rec["sym_diff"] = sym_diff
            rec["sym_pct"]  = sym_pct
        else:
            rec["note"] = err or "sym-diff unavailable"

    finally:
        try:
            os.unlink(tmp_stl)
        except OSError:
            pass

    results.append(rec)


# ══════════════════════════════════════════════════════════════
#  PARTS REGISTRY
# ══════════════════════════════════════════════════════════════

BASE_ORIG   = "/Users/softage/Desktop/Moteus/Original Step:stl files"
OUTPUT_DIR  = "/Users/softage/Desktop/Moteus/Script"

PARTS = [
    # (display_name, original_step_relative_path)

    # ── X1 / 3d ──────────────────────────────────────────────
    ("21-0487A_MXM",                 "X1/3d/21-0487A_MXM.step"),
    ("21-0664E_1233-1C_MXM",         "X1/3d/21-0664E_1233-1C_MXM.step"),
    ("D0014A",                       "X1/3d/D0014A.stp"),
    ("DDA0008E",                     "X1/3d/DDA0008E.stp"),
    ("DRB0008F",                     "X1/3d/DRB0008F.stp"),
    ("DRL0008A",                     "X1/3d/DRL0008A.stp"),
    ("DSE0006A",                     "X1/3d/DSE0006A.stp"),
    ("FDMT80080DC",                  "X1/3d/FDMT80080DC.stp"),
    ("IND_4018-WE-LQS_WRE",          "X1/3d/IND_4018-WE-LQS_WRE.step"),
    ("IND_6028-WE-LQS_WRE",          "X1/3d/IND_6028-WE-LQS_WRE.step"),
    ("IND_8040-WE-LQS_WRE",          "X1/3d/IND_8040-WE-LQS_WRE.step"),
    ("IND_DFE252012_MUR",            "X1/3d/IND_DFE252012_MUR.step"),
    ("QFN-16_MA600_MNP",             "X1/3d/QFN-16_MA600_MNP.step"),
    ("RTA0040B",                     "X1/3d/RTA0040B.stp"),
    ("S3B-PH-SM4-TB_LF__SN_",        "X1/3d/S3B-PH-SM4-TB_LF__SN_.step"),
    ("TSSOP14_OSM",                  "X1/3d/TSSOP14_OSM.step"),
    ("SM08B-GHS-TB",                 "X1/3d/SM08B-GHS-TB.STEP"),
    ("XT60PW-M",                     "X1/3d/XT60PW-M.step"),
    ("TSON Advance",                 "X1/3d/TSON Advance.step"),
    ("SM07B-GHS-TB-LF--SN---3DModel-STEP-56544","X1/3d/SM07B-GHS-TB-LF--SN---3DModel-STEP-56544.STEP"),
    ("XT30PW-M",                     "X1/3d/XT30PW-M.step"),
    ("SOP_Advance",                  "X1/3d/SOP_Advance.step"),
    ("SM06B-GHS-TB",                 "X1/3d/SM06B-GHS-TB.step"),
    ("UFQFPN-48_7X7X0P55MM",         "X1/3d/UFQFPN-48_7X7X0P55MM.step"),
    ("SOD-523_STM",                  "X1/3d/SOD-523_STM.step"),
    ("S6B-ZR-SM4A-TF_LF__SN_",       "X1/3d/S6B-ZR-SM4A-TF_LF__SN_.step"),

    # ── X1 / r1 ──────────────────────────────────────────────
    ("20250427-moteus-x1-r1",        "X1/r1/20250427-moteus-x1-r1.step"),

    # ── N1 / R1.2 ────────────────────────────────────────────
    ("20230226-moteus-n1-mechanical", "N1/R1.2/20230226-moteus-n1-mechanical.step"),

    # ── N1 / R1.3 ────────────────────────────────────────────
    ("20230523-moteus-n1-r1_3-mechanical", "N1/R1.3/20230523-moteus-n1-r1_3-mechanical.step"),

    # ── Controller / r4.3 ────────────────────────────────────
    ("20200729-moteus-controller-r43-mechanical", "Controller/r4.3/20200729-moteus-controller-r43-mechanical.step"),

    # ── Controller / r4.5 ────────────────────────────────────
    ("20210124-moteus-controller-r45-mechanical", "Controller/r4.5/20210124-moteus-controller-r45-mechanical.step"),
]


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print()
    print("╔" + "═"*78 + "╗")
    print("║  Moteus Parts — Validation Report (Volume & Symmetric Difference)" + " "*10 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"  Originals : {BASE_ORIG}")
    print(f"  Outputs   : {OUTPUT_DIR}")
    print(f"  STEP loader : {'cadquery' if HAS_CQ else 'build123d' if HAS_B123 else '✗ NONE — install cadquery or build123d'}")
    print(f"  trimesh   : {'✓' if HAS_TRIMESH else '✗ not installed'}")
    print()

    results = []

    for display_name, rel_orig in PARTS:
        orig_step  = os.path.join(BASE_ORIG, rel_orig)
        # Output STL is always:  output_<stem>.stl
        stem       = os.path.splitext(os.path.basename(rel_orig))[0]
        output_stl = os.path.join(OUTPUT_DIR, f"output_{stem}.stl")

        print(f"  Processing: {display_name} ...", end="", flush=True)
        compare(display_name, orig_step, output_stl, results)
        last = results[-1]
        status = "OK" if last["vol_diff"] is not None else f"SKIP ({last['note']})"
        print(f"\r  [{status:<40}] {display_name}")

    # ── compact results table ─────────────────────────────────
    COL = [38, 16, 10, 16, 10]
    SEP = "─" * (sum(COL) + len(COL)*3 + 1)

    print()
    print("┌" + "─"*78 + "┐")
    print(f"│  {'Part Name':<{COL[0]}}  {'Vol Diff (mm³)':>{COL[1]}}  {'Vol (%)':>{COL[2]}}  {'Sym Diff (mm³)':>{COL[3]}}  {'Sym (%)':>{COL[4]}}  │")
    print("├" + "─"*78 + "┤")

    for r in results:
        name = r["name"][:COL[0]]

        if r["vol_diff"] is not None:
            vd  = f"{r['vol_diff']:>{COL[1]}.3f}"
            vp  = f"{r['vol_pct']:>{COL[2]}.2f}%"
        else:
            vd  = f"{'N/A':>{COL[1]}}"
            vp  = f"{'N/A':>{COL[2]}}"

        if r["sym_diff"] is not None:
            sd  = f"{r['sym_diff']:>{COL[3]}.3f}"
            sp  = f"{r['sym_pct']:>{COL[4]}.2f}%"
        else:
            note = (r["note"] or "")[:COL[3]+COL[4]+3]
            sd  = f"{'—':>{COL[3]}}"
            sp  = f"{'—':>{COL[4]}}"

        note_str = f"  [{r['note']}]" if r["note"] and r["vol_diff"] is None else ""
        print(f"│  {name:<{COL[0]}}  {vd}  {vp}  {sd}  {sp}  │{note_str}")

    print("└" + "─"*78 + "┘")
    print()
    print("  Notes:")
    print("  • Vol Diff   = |volume(original) − volume(output)|  in mm³")
    print("  • Vol (%)    = Vol Diff as % of original volume")
    print("  • Sym Diff   = (A−B) ∪ (B−A) boolean volume in mm³  [requires watertight meshes]")
    print("  • Sym (%)    = Sym Diff as % of original volume")
    print("  • '—' in Sym columns means the mesh is an open shell or trimesh is unavailable.")
    print()
