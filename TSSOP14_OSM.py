from build123d import *

# Part: TSSOP14_OSM

with BuildPart() as part:
    # Loft from Z=0.765 to Z=1.194
    with BuildSketch(Plane.XY.offset(0.765)):
        with BuildLine():
            Line((2.248, 2.553), (-2.248, 2.553))
            Line((-2.248, 2.553), (-2.248, -2.553))
            Line((-2.248, -2.553), (2.248, -2.553))
            Line((2.248, -2.553), (2.248, 2.553))
        make_face()

    with BuildSketch(Plane.XY.offset(1.194)):
        with BuildLine():
            Line((2.07, 2.528), (-2.07, 2.528))
            Line((-2.07, 2.528), (-2.07, -2.528))
            Line((-2.07, -2.528), (2.07, -2.528))
            Line((2.07, -2.528), (2.07, 2.528))
        make_face()

    loft()

    # Rect at Z=0.765, extrude to Z=0.48
    with BuildSketch(Plane.XY.offset(0.765)):
        with BuildLine():
            Line((2.248, 2.553), (-2.248, 2.553))
            Line((-2.248, 2.553), (-2.248, -2.553))
            Line((-2.248, -2.553), (2.248, -2.553))
            Line((2.248, -2.553), (2.248, 2.553))
        make_face()
    extrude(amount=-0.285)

    # Loft from Z=0.051 to Z=0.48
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((2.172, 2.502), (-2.172, 2.502))
            Line((-2.172, 2.502), (-2.172, -2.502))
            Line((-2.172, -2.502), (2.172, -2.502))
            Line((2.172, -2.502), (2.172, 2.502))
        make_face()

    with BuildSketch(Plane.XY.offset(0.48)):
        with BuildLine():
            Line((2.248, 2.553), (-2.248, 2.553))
            Line((-2.248, 2.553), (-2.248, -2.553))
            Line((-2.248, -2.553), (2.248, -2.553))
            Line((2.248, -2.553), (2.248, 2.553))
        make_face()

    loft()

    # Pin profile in XZ plane at Y=-2.102, extrude to Y=-1.798
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

    a2 = arc_mid_from_centre((2.795, 0.472), (2.433, 0.749), (2.433, 0.375), 0.374)
    a4 = arc_mid_from_centre((3.015, 0.187), (2.834, 0.326), (3.015, 0.375), 0.188)
    a8 = arc_mid_from_centre((2.653, 0.278), (3.015, 0.0), (3.015, 0.375), 0.375)
    a10 = arc_mid_from_centre((2.433, 0.562), (2.614, 0.423), (2.433, 0.375), 0.187)

    # Mirrored arcs for -X side (negate X coords)
    a2m = arc_mid_from_centre((-2.795, 0.472), (-2.433, 0.749), (-2.433, 0.375), 0.374)
    a4m = arc_mid_from_centre((-3.015, 0.187), (-2.834, 0.326), (-3.015, 0.375), 0.188)
    a8m = arc_mid_from_centre((-2.653, 0.278), (-3.015, 0.0), (-3.015, 0.375), 0.375)
    a10m = arc_mid_from_centre((-2.433, 0.562), (-2.614, 0.423), (-2.433, 0.375), 0.187)

    # +X side: 7 pins
    px_y = [-2.102, -1.452, -0.802, -0.152, 0.498, 1.148, 1.798]
    for py in px_y:
        sk_pin = Plane(origin=(0, py, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_pin):
            with BuildLine():
                Line((2.433, 0.749), (2.248, 0.749))
                Line((2.248, 0.749), (2.248, 0.562))
                Line((2.248, 0.562), (2.433, 0.562))
                ThreePointArc((2.433, 0.562), a10, (2.614, 0.423))
                Line((2.614, 0.423), (2.653, 0.278))
                ThreePointArc((2.653, 0.278), a8, (3.015, 0.0))
                Line((3.015, 0.0), (3.2, 0.0))
                Line((3.2, 0.0), (3.2, 0.187))
                Line((3.2, 0.187), (3.015, 0.187))
                ThreePointArc((3.015, 0.187), a4, (2.834, 0.326))
                Line((2.834, 0.326), (2.795, 0.472))
                ThreePointArc((2.795, 0.472), a2, (2.433, 0.749))
            make_face()
        extrude(amount=-0.304)

    # -X side: 7 pins
    mx_y = [-1.798, -1.148, -0.498, 0.152, 0.802, 1.452, 2.102]
    for py in mx_y:
        sk_pin = Plane(origin=(0, py, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_pin):
            with BuildLine():
                Line((-2.433, 0.749), (-2.248, 0.749))
                Line((-2.248, 0.749), (-2.248, 0.562))
                Line((-2.248, 0.562), (-2.433, 0.562))
                ThreePointArc((-2.433, 0.562), a10m, (-2.614, 0.423))
                Line((-2.614, 0.423), (-2.653, 0.278))
                ThreePointArc((-2.653, 0.278), a8m, (-3.015, 0.0))
                Line((-3.015, 0.0), (-3.2, 0.0))
                Line((-3.2, 0.0), (-3.2, 0.187))
                Line((-3.2, 0.187), (-3.015, 0.187))
                ThreePointArc((-3.015, 0.187), a4m, (-2.834, 0.326))
                Line((-2.834, 0.326), (-2.795, 0.472))
                ThreePointArc((-2.795, 0.472), a2m, (-2.433, 0.749))
            make_face()
        extrude(amount=-0.304)

    # Circle at (-1.61, 1.95, 1.196), dia 0.225, extrude -0.002
    with BuildSketch(Plane.XY.offset(1.196)):
        with Locations([(-1.61, 1.95)]):
            Circle(radius=0.1125)
    extrude(amount=-0.002)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_TSSOP14_OSM.stl")