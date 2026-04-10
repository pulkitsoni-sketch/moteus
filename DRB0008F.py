from build123d import *

# Part: DRB0008F

with BuildPart() as part:
    # Rect at Z=0.775 (3.0 x 3.0), extrude down to Z=0.08
    with BuildSketch(Plane.XY.offset(0.775)):
        with BuildLine():
            Line((-1.5, -1.5), (-1.5, 1.5))
            Line((-1.5, 1.5), (1.5, 1.5))
            Line((1.5, 1.5), (1.5, -1.5))
            Line((1.5, -1.5), (-1.5, -1.5))
        make_face()
    extrude(amount=-0.695)

    # Rect at Z=0.08 (2.9 x 3.0), extrude down to Z=0.025
    with BuildSketch(Plane.XY.offset(0.08)):
        with BuildLine():
            Line((-1.45, -1.5), (-1.45, 1.5))
            Line((-1.45, 1.5), (1.45, 1.5))
            Line((1.45, 1.5), (1.45, -1.5))
            Line((1.45, -1.5), (-1.45, -1.5))
        make_face()
    extrude(amount=-0.055)

    # Rect at Z=0.2 (1.9 x 2.7), subtract then add
    with BuildSketch(Plane.XY.offset(0.2)):
        with BuildLine():
            Line((-0.95, -1.35), (-0.95, 1.35))
            Line((-0.95, 1.35), (0.95, 1.35))
            Line((0.95, 1.35), (0.95, -1.35))
            Line((0.95, -1.35), (-0.95, -1.35))
        make_face()
    extrude(amount=-0.1, mode=Mode.SUBTRACT)

    with BuildSketch(Plane.XY.offset(0.2)):
        with BuildLine():
            Line((-0.95, -1.35), (-0.95, 1.35))
            Line((-0.95, 1.35), (0.95, 1.35))
            Line((0.95, 1.35), (0.95, -1.35))
            Line((0.95, -1.35), (-0.95, -1.35))
        make_face()
    extrude(amount=-0.1)

    # 5-point profile at Z=0.1, subtract then add
    with BuildSketch(Plane.XY.offset(0.1)):
        with BuildLine():
            Line((0.8, -1.2), (-0.8, -1.2))
            Line((-0.8, -1.2), (-0.8, 0.9))
            Line((-0.8, 0.9), (-0.5, 1.2))
            Line((-0.5, 1.2), (0.8, 1.2))
            Line((0.8, 1.2), (0.8, -1.2))
        make_face()
    extrude(amount=-0.1, mode=Mode.SUBTRACT)

    with BuildSketch(Plane.XY.offset(0.1)):
        with BuildLine():
            Line((0.8, -1.2), (-0.8, -1.2))
            Line((-0.8, -1.2), (-0.8, 0.9))
            Line((-0.8, 0.9), (-0.5, 1.2))
            Line((-0.5, 1.2), (0.8, 1.2))
            Line((0.8, 1.2), (0.8, -1.2))
        make_face()
    extrude(amount=-0.1)

    # Profile with arc at Z=0.2, extrude down to Z=0.0
    import numpy as np

    def arc_mid_from_centre(p1, p2, centre, r):
        c = np.array(centre)
        a = np.array(p1)
        b = np.array(p2)
        va = a - c
        vb = b - c
        mid_dir = va / np.linalg.norm(va) + vb / np.linalg.norm(vb)
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
        mid = c + mid_dir * r
        return tuple(mid)

    # 4 arc bodies with cuts at different Y positions
    y_corners = [-1.125, -0.475, 0.175, 0.825]

    for yc in y_corners:
        # Subtract arc body from main
        with BuildSketch(Plane.XY.offset(0.2)):
            with BuildLine():
                Line((-1.25, yc + 0.3), (-1.5, yc + 0.3))
                Line((-1.5, yc + 0.3), (-1.5, yc))
                Line((-1.5, yc), (-1.25, yc))
                ThreePointArc((-1.25, yc), (-1.1, yc + 0.15), (-1.25, yc + 0.3))
            make_face()
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Add arc body back
        with BuildSketch(Plane.XY.offset(0.2)):
            with BuildLine():
                Line((-1.25, yc + 0.3), (-1.5, yc + 0.3))
                Line((-1.5, yc + 0.3), (-1.5, yc))
                Line((-1.5, yc), (-1.25, yc))
                ThreePointArc((-1.25, yc), (-1.1, yc + 0.15), (-1.25, yc + 0.3))
            make_face()
        extrude(amount=-0.2)

        # Cut extrude for each body
        with BuildSketch(Plane.XY.offset(0.08)):
            with BuildLine():
                Line((-1.45, yc), (-1.5, yc))
                Line((-1.5, yc), (-1.5, yc + 0.3))
                Line((-1.5, yc + 0.3), (-1.45, yc + 0.3))
                Line((-1.45, yc + 0.3), (-1.45, yc))
            make_face()
        extrude(amount=-0.08, mode=Mode.SUBTRACT)

    # Mirrored +X side: 4 arc bodies with cuts
    for yc in y_corners:
        # Subtract arc body from main
        with BuildSketch(Plane.XY.offset(0.2)):
            with BuildLine():
                Line((1.25, yc + 0.3), (1.5, yc + 0.3))
                Line((1.5, yc + 0.3), (1.5, yc))
                Line((1.5, yc), (1.25, yc))
                ThreePointArc((1.25, yc), (1.1, yc + 0.15), (1.25, yc + 0.3))
            make_face()
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Add arc body back
        with BuildSketch(Plane.XY.offset(0.2)):
            with BuildLine():
                Line((1.25, yc + 0.3), (1.5, yc + 0.3))
                Line((1.5, yc + 0.3), (1.5, yc))
                Line((1.5, yc), (1.25, yc))
                ThreePointArc((1.25, yc), (1.1, yc + 0.15), (1.25, yc + 0.3))
            make_face()
        extrude(amount=-0.2)

        with BuildSketch(Plane.XY.offset(0.08)):
            with BuildLine():
                Line((1.45, yc), (1.5, yc))
                Line((1.5, yc), (1.5, yc + 0.3))
                Line((1.5, yc + 0.3), (1.45, yc + 0.3))
                Line((1.45, yc + 0.3), (1.45, yc))
            make_face()
        extrude(amount=-0.08, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_DRB0008F.stl")