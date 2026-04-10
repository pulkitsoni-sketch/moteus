from build123d import *

# Part: DDA0008E

with BuildPart() as part:
    # Rect 1 at Z=0.1 (3.686 x 4.686) with 0.1mm corner fillet
    with BuildSketch(Plane.XY.offset(0.1)):
        RectangleRounded(3.686, 4.686, 0.1)

    # Rect 2 at Z=0.8 (3.9 x 4.9) with 0.1mm corner fillet
    with BuildSketch(Plane.XY.offset(0.8)):
        RectangleRounded(3.9, 4.9, 0.1)

    loft()

    # Extrude top face at Z=0.8 up to Z=1.0
    top_face = part.faces().sort_by(Axis.Z)[-1]
    extrude(top_face, amount=0.2)

    # Loft from top face at Z=1.0 to rect at Z=1.418
    with BuildSketch(Plane.XY.offset(1.0)):
        RectangleRounded(3.9, 4.9, 0.1)

    with BuildSketch(Plane.XY.offset(1.418)):
        RectangleRounded(3.71, 4.72, 0.1)

    loft()

    # Loft from top face at Z=1.418 to rect at Z=1.7
    # Top rect: centre (0.082, 0), 3.322 x 4.486, corners R=0.1
    with BuildSketch(Plane.XY.offset(1.418)):
        RectangleRounded(3.71, 4.72, 0.1)

    with BuildSketch(Plane.XY.offset(1.7)):
        with Locations([(0.082, 0.0)]):
            RectangleRounded(3.322, 4.486, 0.1)

    loft()

    # Fillet bottom face edges (Z=0.1) by 0.1mm
    bottom_face = part.faces().sort_by(Axis.Z)[0]
    fillet(bottom_face.edges(), radius=0.1)

    # Fillet top face edges (Z=1.7) by 0.1mm
    top_face_final = part.faces().sort_by(Axis.Z)[-1]
    fillet(top_face_final.edges(), radius=0.1)

    # Fillet edge at X≈-1.855, Z≈1.418 running along Y by 0.1mm
    target_edge = None
    best_len = 0
    for e in part.edges():
        s = e @ 0
        f = e @ 1
        # Edge should be at X≈-1.855, Z≈1.418, running along Y (long edge)
        mid = e @ 0.5
        if (abs(mid.X - (-1.855)) < 0.05 and abs(mid.Z - 1.418) < 0.05):
            edge_len = e.length
            if edge_len > best_len:
                best_len = edge_len
                target_edge = e
    if target_edge:
        fillet([target_edge], radius=0.1)
    else:
        print("Edge not found at X=-1.855, Z=1.418")

    # Cut extrude: rect 2.026 x 2.876 from Z=0.1 to Z=0.25 (subtract)
    with BuildSketch(Plane.XY.offset(0.1)):
        with BuildLine():
            Line((-1.013, 1.438), (-1.013, -1.438))
            Line((-1.013, -1.438), (1.013, -1.438))
            Line((1.013, -1.438), (1.013, 1.438))
            Line((1.013, 1.438), (-1.013, 1.438))
        make_face()
    extrude(amount=0.15, mode=Mode.SUBTRACT)

    # Add extrude: same rect from Z=0.1 to Z=0.25 (new body)
    with BuildSketch(Plane.XY.offset(0.1)):
        with BuildLine():
            Line((-1.013, 1.438), (-1.013, -1.438))
            Line((-1.013, -1.438), (1.013, -1.438))
            Line((1.013, -1.438), (1.013, 1.438))
            Line((1.013, 1.438), (-1.013, 1.438))
        make_face()
    extrude(amount=0.15)

    # Side profiles at -X side, 4 bodies at different Y positions, extruded 0.41 along -Y
    import numpy as np

    def arc_mid_from_centre(p1, p2, centre, r):
        """Compute arc midpoint given endpoints and centre in 2D"""
        c = np.array(centre)
        a = np.array(p1)
        b = np.array(p2)
        va = a - c
        vb = b - c
        mid_dir = va / np.linalg.norm(va) + vb / np.linalg.norm(vb)
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
        mid = c + mid_dir * r
        return tuple(mid)

    # Arc midpoints (same for all bodies)
    m1 = arc_mid_from_centre((-1.984, 0.8), (-2.083, 0.717), (-1.984, 0.70), 0.1)
    m2 = arc_mid_from_centre((-2.159, 0.287), (-2.433, 0.04), (-2.454, 0.339), 0.3)
    m3 = arc_mid_from_centre((-2.447, 0.239), (-2.355, 0.322), (-2.454, 0.339), 0.1)
    m4 = arc_mid_from_centre((-2.28, 0.752), (-1.984, 1.0), (-1.984, 0.70), 0.3)

    y_positions = [2.11, 0.84, -0.43, -1.7]

    for y_pos in y_positions:
        sk_plane = Plane(origin=(0, y_pos, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_plane):
            with BuildLine():
                Line((-1.95, 0.8), (-1.984, 0.8))
                ThreePointArc((-1.984, 0.8), m1, (-2.083, 0.717))
                Line((-2.083, 0.717), (-2.159, 0.287))
                ThreePointArc((-2.159, 0.287), m2, (-2.433, 0.04))
                Line((-2.433, 0.04), (-3.0, 0.0))
                Line((-3.0, 0.0), (-3.014, 0.2))
                Line((-3.014, 0.2), (-2.447, 0.239))
                ThreePointArc((-2.447, 0.239), m3, (-2.355, 0.322))
                Line((-2.355, 0.322), (-2.28, 0.752))
                ThreePointArc((-2.28, 0.752), m4, (-1.984, 1.0))
                Line((-1.984, 1.0), (-1.95, 1.0))
                Line((-1.95, 1.0), (-1.95, 0.8))
            make_face()
        extrude(amount=0.41)

    # Mirrored +X side: negate all X coordinates
    m1n = arc_mid_from_centre((1.984, 0.8), (2.083, 0.717), (1.984, 0.70), 0.1)
    m2n = arc_mid_from_centre((2.159, 0.287), (2.433, 0.04), (2.454, 0.339), 0.3)
    m3n = arc_mid_from_centre((2.447, 0.239), (2.355, 0.322), (2.454, 0.339), 0.1)
    m4n = arc_mid_from_centre((2.28, 0.752), (1.984, 1.0), (1.984, 0.70), 0.3)

    for y_pos in y_positions:
        sk_plane = Plane(origin=(0, y_pos, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_plane):
            with BuildLine():
                Line((1.95, 0.8), (1.984, 0.8))
                ThreePointArc((1.984, 0.8), m1n, (2.083, 0.717))
                Line((2.083, 0.717), (2.159, 0.287))
                ThreePointArc((2.159, 0.287), m2n, (2.433, 0.04))
                Line((2.433, 0.04), (3.0, 0.0))
                Line((3.0, 0.0), (3.014, 0.2))
                Line((3.014, 0.2), (2.447, 0.239))
                ThreePointArc((2.447, 0.239), m3n, (2.355, 0.322))
                Line((2.355, 0.322), (2.28, 0.752))
                ThreePointArc((2.28, 0.752), m4n, (1.984, 1.0))
                Line((1.984, 1.0), (1.95, 1.0))
                Line((1.95, 1.0), (1.95, 0.8))
            make_face()
        extrude(amount=0.41)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_DDA0008E.stl")