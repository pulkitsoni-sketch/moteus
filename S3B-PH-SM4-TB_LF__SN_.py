from build123d import *

# Part: S3B-PH-SM4-TB_LF__SN_

with BuildPart() as part:
    # Rect in XZ plane at Y=5.5 (9.9 x 7.6), extrude to Y=0.0
    # X: -4.95 to 4.95, Z: -7.6 to 0.0
    sk = Plane(origin=(0, 5.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk):
        with BuildLine():
            Line((-4.95, -7.6), (4.95, -7.6))
            Line((4.95, -7.6), (4.95, 0.0))
            Line((4.95, 0.0), (-4.95, 0.0))
            Line((-4.95, 0.0), (-4.95, -7.6))
        make_face()
    extrude(amount=5.5)

    # Subtract rect in XZ plane at Y=5.5, extrude to Y=0.0 (+X side)
    sk2 = Plane(origin=(0, 5.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk2):
        with BuildLine():
            Line((4.05, -0.8), (4.95, -0.8))
            Line((4.95, -0.8), (4.95, 0.0))
            Line((4.95, 0.0), (4.05, 0.0))
            Line((4.05, 0.0), (4.05, -0.8))
        make_face()
    extrude(amount=5.5, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(sk2):
        with BuildLine():
            Line((-4.05, -0.8), (-4.95, -0.8))
            Line((-4.95, -0.8), (-4.95, 0.0))
            Line((-4.95, 0.0), (-4.05, 0.0))
            Line((-4.05, 0.0), (-4.05, -0.8))
        make_face()
    extrude(amount=5.5, mode=Mode.SUBTRACT)

    # Subtract rect in XY plane at Z=0.0 (X: 3.45→4.95, Y: 0.0→0.4), extrude to Z=-3.0
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((3.45, 0.0), (4.95, 0.0))
            Line((4.95, 0.0), (4.95, 0.4))
            Line((4.95, 0.4), (3.45, 0.4))
            Line((3.45, 0.4), (3.45, 0.0))
        make_face()
    extrude(amount=-3.0, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((-3.45, 0.0), (-4.95, 0.0))
            Line((-4.95, 0.0), (-4.95, 0.4))
            Line((-4.95, 0.4), (-3.45, 0.4))
            Line((-3.45, 0.4), (-3.45, 0.0))
        make_face()
    extrude(amount=-3.0, mode=Mode.SUBTRACT)

    # Subtract rect in XY at Z=0.0 (X: -2.825→2.825, Y: 0.0→0.09), extrude to Z=-6.0
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((2.825, 0.0), (-2.825, 0.0))
            Line((-2.825, 0.0), (-2.825, 0.09))
            Line((-2.825, 0.09), (2.825, 0.09))
            Line((2.825, 0.09), (2.825, 0.0))
        make_face()
    extrude(amount=-6.0, mode=Mode.SUBTRACT)

    # Subtract rect in XZ plane at Y=5.5 (X: -4.15→4.15, Z: -7.6→-6.0), extrude to Y=0.0
    sk3 = Plane(origin=(0, 5.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((-4.15, -7.6), (4.15, -7.6))
            Line((4.15, -7.6), (4.15, -6.0))
            Line((4.15, -6.0), (-4.15, -6.0))
            Line((-4.15, -6.0), (-4.15, -7.6))
        make_face()
    extrude(amount=5.5, mode=Mode.SUBTRACT)

    # Subtract triangle in YZ plane at X=4.95, extrude to X=-4.95
    # Points in sketch coords (sketch X=world Y, sketch Y=world Z)
    sk4 = Plane(origin=(4.95, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk4):
        with BuildLine():
            Line((5.5, -6.0), (3.7, -6.0))
            Line((3.7, -6.0), (2.776, -7.6))
            Line((2.776, -7.6), (5.5, -7.6))
            Line((5.5, -7.6), (5.5, -6.0))
        make_face()
    extrude(amount=-9.9, mode=Mode.SUBTRACT)

    # Subtract rect in XZ plane at Y=5.5 (X: 2.3→3.3, Z: -6.0→-2.0), extrude to Y=4.2
    sk5 = Plane(origin=(0, 5.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk5):
        with BuildLine():
            Line((2.3, -6.0), (3.3, -6.0))
            Line((3.3, -6.0), (3.3, -2.0))
            Line((3.3, -2.0), (2.3, -2.0))
            Line((2.3, -2.0), (2.3, -6.0))
        make_face()
    extrude(amount=1.3, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(sk5):
        with BuildLine():
            Line((-2.3, -6.0), (-3.3, -6.0))
            Line((-3.3, -6.0), (-3.3, -2.0))
            Line((-3.3, -2.0), (-2.3, -2.0))
            Line((-2.3, -2.0), (-2.3, -6.0))
        make_face()
    extrude(amount=1.3, mode=Mode.SUBTRACT)

    # Subtract rect in YZ plane at X=4.95 (Y: 2.55→4.705, Z: -5.415→-0.8), extrude to X=4.75
    sk6 = Plane(origin=(4.95, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6):
        with BuildLine():
            Line((2.55, -0.8), (4.705, -0.8))
            Line((4.705, -0.8), (4.705, -5.415))
            Line((4.705, -5.415), (2.55, -5.415))
            Line((2.55, -5.415), (2.55, -0.8))
        make_face()
    extrude(amount=-0.2, mode=Mode.SUBTRACT)

    # Mirror: -X side (at X=-4.95, extrude to X=-4.75)
    sk7 = Plane(origin=(-4.95, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk7):
        with BuildLine():
            Line((2.55, -0.8), (4.705, -0.8))
            Line((4.705, -0.8), (4.705, -5.415))
            Line((4.705, -5.415), (2.55, -5.415))
            Line((2.55, -5.415), (2.55, -0.8))
        make_face()
    extrude(amount=0.2, mode=Mode.SUBTRACT)

    # Subtract L-profile in YZ plane at X=4.05, extrude to X=4.95 (amount=0.9)
    sk8 = Plane(origin=(4.05, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk8):
        with BuildLine():
            Line((4.705, -0.8), (4.705, -2.715))
            Line((4.705, -2.715), (3.42, -2.715))
            Line((3.42, -2.715), (3.42, -5.415))
            Line((3.42, -5.415), (2.55, -5.415))
            Line((2.55, -5.415), (2.55, -0.8))
            Line((2.55, -0.8), (4.705, -0.8))
        make_face()
    extrude(amount=0.9, mode=Mode.SUBTRACT)

    # Mirror: -X side (at X=-4.05, extrude to X=-4.95)
    sk9 = Plane(origin=(-4.05, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk9):
        with BuildLine():
            Line((4.705, -0.8), (4.705, -2.715))
            Line((4.705, -2.715), (3.42, -2.715))
            Line((3.42, -2.715), (3.42, -5.415))
            Line((3.42, -5.415), (2.55, -5.415))
            Line((2.55, -5.415), (2.55, -0.8))
            Line((2.55, -0.8), (4.705, -0.8))
        make_face()
    extrude(amount=-0.9, mode=Mode.SUBTRACT)

    # 11-point profile at Z=0.0, extrude to Z=-4.25, subtract
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((-3.3, 4.355), (-2.3, 4.355))
            Line((-2.3, 4.355), (-2.3, 4.2))
            Line((-2.3, 4.2), (-1.3, 4.2))
            Line((-1.3, 4.2), (-1.3, 5.0))
            Line((-1.3, 5.0), (1.3, 5.0))
            Line((1.3, 5.0), (1.3, 4.2))
            Line((1.3, 4.2), (2.3, 4.2))
            Line((2.3, 4.2), (2.3, 4.355))
            Line((2.3, 4.355), (3.3, 4.355))
            Line((3.3, 4.355), (3.3, 0.7))
            Line((3.3, 0.7), (-3.3, 0.7))
            Line((-3.3, 0.7), (-3.3, 4.355))
        make_face()
    extrude(amount=-4.25, mode=Mode.SUBTRACT)

    # 4-point profile in YZ plane at X=-3.3, extrude to X=3.3
    sk10 = Plane(origin=(-3.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk10):
        with BuildLine():
            Line((2.825, -4.25), (2.225, -4.85))
            Line((2.225, -4.85), (0.7, -4.85))
            Line((0.7, -4.85), (0.7, -4.25))
            Line((0.7, -4.25), (2.825, -4.25))
        make_face()
    extrude(amount=6.6, mode=Mode.SUBTRACT)

    # Profile with arcs in YZ plane at X=4.05, extrude to X=3.3 (subtract)
    import numpy as np

    def arc_mid_from_centre(p1, p2, centre, r):
        c = np.array(centre)
        a = np.array(p1)
        b = np.array(p2)
        va = a - c
        vb = b - c
        mid_dir = va / np.linalg.norm(va) + vb / np.linalg.norm(vb)
        norm = np.linalg.norm(mid_dir)
        if norm < 1e-10:
            perp = np.array([-va[1], va[0]])
            mid_dir = perp / np.linalg.norm(perp)
        else:
            mid_dir = mid_dir / norm
        mid = c + mid_dir * r
        return tuple(mid)

    # Sketch coords: X=world Y, Y=world Z
    am1 = arc_mid_from_centre((2.55, -1.65), (2.80, -1.9), (2.80, -1.65), 0.25)
    am2 = arc_mid_from_centre((3.10, -1.9), (3.35, -1.65), (3.10, -1.65), 0.25)

    # +X side
    sk11 = Plane(origin=(4.05, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk11):
        with BuildLine():
            Line((2.55, 0.0), (2.55, -1.65))
            ThreePointArc((2.55, -1.65), am1, (2.80, -1.9))
            Line((2.80, -1.9), (3.10, -1.9))
            ThreePointArc((3.10, -1.9), am2, (3.35, -1.65))
            Line((3.35, -1.65), (3.35, 0.0))
            Line((3.35, 0.0), (2.55, 0.0))
        make_face()
    extrude(amount=-0.75, mode=Mode.SUBTRACT)

    # Mirror: -X side (at X=-4.05, extrude to X=-3.3)
    sk12 = Plane(origin=(-4.05, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk12):
        with BuildLine():
            Line((2.55, 0.0), (2.55, -1.65))
            ThreePointArc((2.55, -1.65), am1, (2.80, -1.9))
            Line((2.80, -1.9), (3.10, -1.9))
            ThreePointArc((3.10, -1.9), am2, (3.35, -1.65))
            Line((3.35, -1.65), (3.35, 0.0))
            Line((3.35, 0.0), (2.55, 0.0))
        make_face()
    extrude(amount=0.75, mode=Mode.SUBTRACT)

    # Chamfer edge from (-3.3, 0.7, 0.0) to (3.3, 0.7, 0.0) by 0.16mm
    target_edge = None
    for e in part.edges():
        s = e @ 0
        f = e @ 1
        if ((abs(s.X - (-3.3)) < 0.02 and abs(s.Y - 0.7) < 0.02 and abs(s.Z) < 0.02 and
             abs(f.X - 3.3) < 0.02 and abs(f.Y - 0.7) < 0.02 and abs(f.Z) < 0.02) or
            (abs(f.X - (-3.3)) < 0.02 and abs(f.Y - 0.7) < 0.02 and abs(f.Z) < 0.02 and
             abs(s.X - 3.3) < 0.02 and abs(s.Y - 0.7) < 0.02 and abs(s.Z) < 0.02)):
            target_edge = e
            break
    if target_edge:
        chamfer([target_edge], length=0.16)
    else:
        print("Chamfer edge not found")

    # Helper to find and chamfer an edge by endpoints
    def find_and_chamfer(pt1, pt2, length, tol=0.02):
        for e in part.edges():
            s = e @ 0
            f = e @ 1
            if ((abs(s.X - pt1[0]) < tol and abs(s.Y - pt1[1]) < tol and abs(s.Z - pt1[2]) < tol and
                 abs(f.X - pt2[0]) < tol and abs(f.Y - pt2[1]) < tol and abs(f.Z - pt2[2]) < tol) or
                (abs(f.X - pt1[0]) < tol and abs(f.Y - pt1[1]) < tol and abs(f.Z - pt1[2]) < tol and
                 abs(s.X - pt2[0]) < tol and abs(s.Y - pt2[1]) < tol and abs(s.Z - pt2[2]) < tol)):
                try:
                    chamfer([e], length=length)
                    return True
                except ValueError as ex:
                    print(f"Chamfer failed at {pt1}->{pt2} with length {length}: {ex}")
                    return False
        print(f"Edge not found: {pt1} -> {pt2}")
        return False

    # Chamfer (-1.3, 5.0, 0) to (1.3, 5.0, 0) by 0.16
    find_and_chamfer((-1.3, 5.0, 0.0), (1.3, 5.0, 0.0), 0.16)

    # Triangle profile in YZ plane at X=-1.3, extrude to X=-3.3 (subtract)
    sk13 = Plane(origin=(-1.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk13):
        with BuildLine():
            Line((4.2, -0.23), (4.2, 0.0))
            Line((4.2, 0.0), (4.43, 0.0))
            Line((4.43, 0.0), (4.2, -0.23))
        make_face()
    extrude(amount=-2.0, mode=Mode.SUBTRACT)

    # Mirror: +X side at X=1.3, extrude to X=3.3
    sk14 = Plane(origin=(1.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk14):
        with BuildLine():
            Line((4.2, -0.23), (4.2, 0.0))
            Line((4.2, 0.0), (4.43, 0.0))
            Line((4.43, 0.0), (4.2, -0.23))
        make_face()
    extrude(amount=2.0, mode=Mode.SUBTRACT)

    # 3 pin bodies with subtract+add, top right X at 2.25, 0.25, -1.75
    am3 = arc_mid_from_centre((3.35, -5.9), (2.75, -6.5), (2.75, -5.90), 0.6)
    am4 = arc_mid_from_centre((0.57, -6.5), (0.47, -6.596), (0.57, -6.60), 0.10)
    am5 = arc_mid_from_centre((-0.03, -6.574), (0.57, -6.0), (0.57, -6.60), 0.60)

    x_rights = [2.25, 0.25, -1.75]

    for xr in x_rights:
        xl = xr - 0.5
        xc = xr - 0.25  # centre X

        for mode in [Mode.SUBTRACT, Mode.ADD]:
            # 11-point profile
            skp = Plane(origin=(xr, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
            with BuildSketch(skp):
                with BuildLine():
                    Line((3.35, -1.35), (3.35, -5.9))
                    ThreePointArc((3.35, -5.9), am3, (2.75, -6.5))
                    Line((2.75, -6.5), (0.57, -6.5))
                    ThreePointArc((0.57, -6.5), am4, (0.47, -6.596))
                    Line((0.47, -6.596), (0.4, -8.205))
                    Line((0.4, -8.205), (-0.1, -8.183))
                    Line((-0.1, -8.183), (-0.03, -6.574))
                    ThreePointArc((-0.03, -6.574), am5, (0.57, -6.0))
                    Line((0.57, -6.0), (2.85, -6.0))
                    Line((2.85, -6.0), (2.85, -1.35))
                    Line((2.85, -1.35), (3.35, -1.35))
                make_face()
            extrude(amount=-0.5, mode=mode)

            # Top loft
            with BuildSketch(Plane.XY.offset(-0.95)):
                with BuildLine():
                    Line((xc + 0.143, 3.25), (xc + 0.143, 2.95))
                    Line((xc + 0.143, 2.95), (xc - 0.143, 2.95))
                    Line((xc - 0.143, 2.95), (xc - 0.143, 3.25))
                    Line((xc - 0.143, 3.25), (xc + 0.143, 3.25))
                make_face()

            with BuildSketch(Plane.XY.offset(-1.35)):
                with BuildLine():
                    Line((xr, 3.35), (xr, 2.85))
                    Line((xr, 2.85), (xl, 2.85))
                    Line((xl, 2.85), (xl, 3.35))
                    Line((xl, 3.35), (xr, 3.35))
                make_face()

            loft(mode=mode)

            # Bottom loft
            with BuildSketch(Plane.XY.offset(-8.6)):
                with BuildLine():
                    Line((xc + 0.143, 0.282), (xc - 0.143, 0.282))
                    Line((xc - 0.143, 0.282), (xc - 0.143, -0.018))
                    Line((xc - 0.143, -0.018), (xc + 0.143, -0.018))
                    Line((xc + 0.143, -0.018), (xc + 0.143, 0.282))
                make_face()

            with BuildSketch(Plane.XY.offset(-8.194)):
                with BuildLine():
                    Line((xr, 0.4), (xl, 0.4))
                    Line((xl, 0.4), (xl, -0.1))
                    Line((xl, -0.1), (xr, -0.1))
                    Line((xr, -0.1), (xr, 0.4))
                make_face()

            loft(mode=mode)

    # 14-point profile in YZ plane, subtract+add, +X and -X sides
    # +X side: X=4.45, extrude to X=4.05 (amount=-0.4)
    # -X side: X=-4.45, extrude to X=-4.05 (amount=0.4)
    side_configs = [
        (4.45, -0.4),   # +X side
        (-4.45, 0.4),   # -X side (mirror)
    ]

    for x_origin, amt in side_configs:
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            skp = Plane(origin=(x_origin, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
            with BuildSketch(skp):
                with BuildLine():
                    Line((2.1, 0.0), (2.1, -2.9))
                    Line((2.1, -2.9), (0.1, -2.9))
                    Line((0.1, -2.9), (-0.1, -2.7))
                    Line((-0.1, -2.7), (-0.1, -1.271))
                    Line((-0.1, -1.271), (0.0, -1.171))
                    Line((0.0, -1.171), (0.0, -1.044))
                    Line((0.0, -1.044), (-0.1, -0.944))
                    Line((-0.1, -0.944), (-0.1, -0.2))
                    Line((-0.1, -0.2), (0.1, 0.0))
                    Line((0.1, 0.0), (1.298, 0.0))
                    Line((1.298, 0.0), (1.298, -0.08))
                    Line((1.298, -0.08), (1.71, -0.08))
                    Line((1.71, -0.08), (1.71, 0.0))
                    Line((1.71, 0.0), (2.1, 0.0))
                make_face()
            extrude(amount=amt, mode=mode)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_S3B-PH-SM4-TB_LF__SN_.stl")