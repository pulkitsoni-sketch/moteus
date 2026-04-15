from build123d import *

# Part: TSON_Advance

with BuildPart() as part:
    # Loft from Z=0.0 to Z=0.85
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((1.55, 1.55), (-1.55, 1.55))
            Line((-1.55, 1.55), (-1.55, -1.55))
            Line((-1.55, -1.55), (1.55, -1.55))
            Line((1.55, -1.55), (1.55, 1.55))
        make_face()

    with BuildSketch(Plane.XY.offset(0.85)):
        with BuildLine():
            Line((1.431, 1.431), (-1.431, 1.431))
            Line((-1.431, 1.431), (-1.431, -1.431))
            Line((-1.431, -1.431), (1.431, -1.431))
            Line((1.431, -1.431), (1.431, 1.431))
        make_face()

    loft()

    # 4 pad bodies, subtract+add
    pad_x = [1.135, 0.485, -0.165, -0.815]
    for px in pad_x:
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(Plane.XY.offset(0.0)):
                with BuildLine():
                    Line((px, -1.4), (px - 0.32, -1.4))
                    Line((px - 0.32, -1.4), (px - 0.32, -1.65))
                    Line((px - 0.32, -1.65), (px, -1.65))
                    Line((px, -1.65), (px, -1.4))
                make_face()
            extrude(amount=0.17, mode=mode)

    # 32-edge profile at Z=0.0, extrude to Z=0.17, subtract+add
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

    a3 = arc_mid_from_centre((1.245, 0.35), (1.495, 0.1), (1.495, 0.35), 0.25)
    a23 = arc_mid_from_centre((-1.495, 0.1), (-1.245, 0.35), (-1.495, 0.35), 0.25)
    a27 = arc_mid_from_centre((-1.245, -0.35), (-1.495, -0.1), (-1.495, -0.35), 0.25)
    a31 = arc_mid_from_centre((1.495, -0.1), (1.245, -0.35), (1.495, -0.35), 0.25)

    for mode in [Mode.SUBTRACT, Mode.ADD]:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((1.65, 0.1), (1.65, -0.1))
                Line((1.65, -0.1), (1.495, -0.1))
                ThreePointArc((1.495, -0.1), a31, (1.245, -0.35))
                Line((1.245, -0.35), (1.245, -0.7))
                Line((1.245, -0.7), (-1.245, -0.7))
                Line((-1.245, -0.7), (-1.245, -0.35))
                ThreePointArc((-1.245, -0.35), a27, (-1.495, -0.1))
                Line((-1.495, -0.1), (-1.65, -0.1))
                Line((-1.65, -0.1), (-1.65, 0.1))
                Line((-1.65, 0.1), (-1.495, 0.1))
                ThreePointArc((-1.495, 0.1), a23, (-1.245, 0.35))
                Line((-1.245, 0.35), (-1.245, 1.4))
                Line((-1.245, 1.4), (-1.135, 1.4))
                Line((-1.135, 1.4), (-1.135, 1.65))
                Line((-1.135, 1.65), (-0.815, 1.65))
                Line((-0.815, 1.65), (-0.815, 1.4))
                Line((-0.815, 1.4), (-0.485, 1.4))
                Line((-0.485, 1.4), (-0.485, 1.65))
                Line((-0.485, 1.65), (-0.165, 1.65))
                Line((-0.165, 1.65), (-0.165, 1.4))
                Line((-0.165, 1.4), (0.165, 1.4))
                Line((0.165, 1.4), (0.165, 1.65))
                Line((0.165, 1.65), (0.485, 1.65))
                Line((0.485, 1.65), (0.485, 1.4))
                Line((0.485, 1.4), (0.815, 1.4))
                Line((0.815, 1.4), (0.815, 1.65))
                Line((0.815, 1.65), (1.135, 1.65))
                Line((1.135, 1.65), (1.135, 1.4))
                Line((1.135, 1.4), (1.245, 1.4))
                Line((1.245, 1.4), (1.245, 0.35))
                ThreePointArc((1.245, 0.35), a3, (1.495, 0.1))
                Line((1.495, 0.1), (1.65, 0.1))
            make_face()
        extrude(amount=0.17, mode=mode)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_TSON_Advance.stl")