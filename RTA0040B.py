from build123d import *
import numpy as np

# Part: RTA0040B

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

# Collect all pin data first
pin_data = []

# Top side (Y=3.0): 10 pins
for lx in [-2.36, -1.86, -1.36, -0.86, -0.36, 0.14, 0.64, 1.14, 1.64, 2.14]:
    pin_data.append(((lx, 3.0), (lx + 0.22, 3.0), (lx + 0.22, 2.709),
        (lx + 0.111, 2.6), (lx + 0.109, 2.6), (lx, 2.709),
        (lx + 0.111, 2.709), (lx + 0.109, 2.709)))

# Right side (X=3.0): 10 pins
for ly in [2.36, 1.86, 1.36, 0.86, 0.36, -0.14, -0.64, -1.14, -1.64, -2.14]:
    pin_data.append(((3.0, ly), (3.0, ly - 0.22), (2.709, ly - 0.22),
        (2.6, ly - 0.111), (2.6, ly - 0.109), (2.709, ly),
        (2.709, ly - 0.111), (2.709, ly - 0.109)))

# Bottom side (Y=-3.0): 10 pins
for lx in [2.36, 1.86, 1.36, 0.86, 0.36, -0.14, -0.64, -1.14, -1.64, -2.14]:
    pin_data.append(((lx, -3.0), (lx - 0.22, -3.0), (lx - 0.22, -2.709),
        (lx - 0.111, -2.6), (lx - 0.109, -2.6), (lx, -2.709),
        (lx - 0.111, -2.709), (lx - 0.109, -2.709)))

# Left side (X=-3.0): 10 pins
for ly in [-2.36, -1.86, -1.36, -0.86, -0.36, 0.14, 0.64, 1.14, 1.64, 2.14]:
    pin_data.append(((-3.0, ly), (-3.0, ly + 0.22), (-2.709, ly + 0.22),
        (-2.6, ly + 0.111), (-2.6, ly + 0.109), (-2.709, ly),
        (-2.709, ly + 0.111), (-2.709, ly + 0.109)))

corner_profiles = [
    [(-3.0, 2.725), (-2.725, 2.725), (-2.725, 3.0), (-2.875, 3.0), (-2.875, 2.875), (-3.0, 2.875)],
    [(2.725, 3.0), (2.725, 2.725), (3.0, 2.725), (3.0, 2.875), (2.875, 2.875), (2.875, 3.0)],
    [(3.0, -2.725), (2.725, -2.725), (2.725, -3.0), (2.875, -3.0), (2.875, -2.875), (3.0, -2.875)],
    [(-2.725, -3.0), (-2.725, -2.725), (-3.0, -2.725), (-3.0, -2.875), (-2.875, -2.875), (-2.875, -3.0)],
]

with BuildPart() as part:
    # Main body: Rect at Z=0.025 (6.0 x 6.0), extrude up to Z=1.0
    with BuildSketch(Plane.XY.offset(0.025)):
        with BuildLine():
            Line((-3.0, -3.0), (3.0, -3.0))
            Line((3.0, -3.0), (3.0, 3.0))
            Line((3.0, 3.0), (-3.0, 3.0))
            Line((-3.0, 3.0), (-3.0, -3.0))
        make_face()
    extrude(amount=0.975)

    # 5-point profile, subtract then add
    for mode in [Mode.SUBTRACT, Mode.ADD]:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((-1.775, 2.075), (-2.075, 1.775))
                Line((-2.075, 1.775), (-2.075, -2.075))
                Line((-2.075, -2.075), (2.075, -2.075))
                Line((2.075, -2.075), (2.075, 2.075))
                Line((2.075, 2.075), (-1.775, 2.075))
            make_face()
        extrude(amount=0.2, mode=mode)

    # 40 pin bodies, subtract then add
    for p1, p2, p3, p4, p5, p6, c1, c2 in pin_data:
        m1 = arc_mid_from_centre(p3, p4, c1, 0.109)
        m2 = arc_mid_from_centre(p5, p6, c2, 0.109)
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(Plane.XY.offset(0.0)):
                with BuildLine():
                    Line(p1, p2)
                    Line(p2, p3)
                    ThreePointArc(p3, m1, p4)
                    Line(p4, p5)
                    ThreePointArc(p5, m2, p6)
                    Line(p6, p1)
                make_face()
            extrude(amount=0.2, mode=mode)

    # 4 corner bodies, subtract then add
    for prof in corner_profiles:
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(Plane.XY.offset(0.1)):
                with BuildLine():
                    for i in range(len(prof)):
                        Line(prof[i], prof[(i + 1) % len(prof)])
                make_face()
            extrude(amount=0.1, mode=mode)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_RTA0040B.stl")