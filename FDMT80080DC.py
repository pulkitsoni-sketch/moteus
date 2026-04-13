from build123d import *

# Part: FDMT80080DC

with BuildPart() as part:
    # Rect at Z=0.0 (8.0 x 8.0), extrude up to Z=0.85
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((4.0, 4.0), (-4.0, 4.0))
            Line((-4.0, 4.0), (-4.0, -4.0))
            Line((-4.0, -4.0), (4.0, -4.0))
            Line((4.0, -4.0), (4.0, 4.0))
        make_face()
    extrude(amount=0.85)

    # 6-point profile at Z=-0.029, extrude up to Z=0.0
    with BuildSketch(Plane.XY.offset(-0.029)):
        with BuildLine():
            Line((3.429, 4.032), (3.5, 3.938))
            Line((3.5, 3.938), (3.5, 3.41))
            Line((3.5, 3.41), (2.494, 3.41))
            Line((2.494, 3.41), (2.494, 3.938))
            Line((2.494, 3.938), (2.543, 4.032))
            Line((2.543, 4.032), (3.429, 4.032))
        make_face()
    extrude(amount=0.029)

    # 4-point profile at Z=0.25, extrude down to Z=0.0
    with BuildSketch(Plane.XY.offset(0.25)):
        with BuildLine():
            Line((3.429, 4.032), (3.453, 4.0))
            Line((3.453, 4.0), (2.526, 4.0))
            Line((2.526, 4.0), (2.543, 4.032))
            Line((2.543, 4.032), (3.429, 4.032))
        make_face()
    extrude(amount=-0.25)

    # 18-point profile at Z=-0.029, extrude up to Z=0.0
    with BuildSketch(Plane.XY.offset(-0.029)):
        with BuildLine():
            Line((1.423, 4.031), (1.495, 3.938))
            Line((1.495, 3.938), (1.495, 3.41))
            Line((1.495, 3.41), (-3.507, 3.41))
            Line((-3.507, 3.41), (-3.507, 3.938))
            Line((-3.507, 3.938), (-3.446, 4.024))
            Line((-3.446, 4.024), (-2.546, 4.024))
            Line((-2.546, 4.024), (-2.507, 3.946))
            Line((-2.507, 3.946), (-2.507, 3.804))
            Line((-2.507, 3.804), (-1.511, 3.804))
            Line((-1.511, 3.804), (-1.511, 3.938))
            Line((-1.511, 3.938), (-1.457, 4.024))
            Line((-1.457, 4.024), (-0.548, 4.017))
            Line((-0.548, 4.017), (-0.512, 3.946))
            Line((-0.512, 3.946), (-0.512, 3.804))
            Line((-0.512, 3.804), (0.499, 3.804))
            Line((0.499, 3.804), (0.499, 3.938))
            Line((0.499, 3.938), (0.534, 4.031))
            Line((0.534, 4.031), (1.423, 4.031))
        make_face()
    extrude(amount=0.029)

    # 4-point trapezoid at Z=0.25, extrude down to Z=0.0
    with BuildSketch(Plane.XY.offset(0.25)):
        with BuildLine():
            Line((1.423, 4.031), (1.447, 4.0))
            Line((1.447, 4.0), (0.522, 4.0))
            Line((0.522, 4.0), (0.534, 4.031))
            Line((0.534, 4.031), (1.423, 4.031))
        make_face()
    extrude(amount=-0.25)

    # 4-point trapezoid at Z=0.25, extrude down to Z=0.0
    with BuildSketch(Plane.XY.offset(0.25)):
        with BuildLine():
            Line((-0.548, 4.017), (-0.54, 4.0))
            Line((-0.54, 4.0), (-1.472, 4.0))
            Line((-1.472, 4.0), (-1.457, 4.024))
            Line((-1.457, 4.024), (-0.548, 4.017))
        make_face()
    extrude(amount=-0.25)

    # 4-point trapezoid at Z=0.25, extrude down to Z=0.0
    with BuildSketch(Plane.XY.offset(0.25)):
        with BuildLine():
            Line((-2.546, 4.024), (-2.534, 4.0))
            Line((-2.534, 4.0), (-3.463, 4.0))
            Line((-3.463, 4.0), (-3.446, 4.024))
            Line((-3.446, 4.024), (-2.546, 4.024))
        make_face()
    extrude(amount=-0.25)

    # 60-point profile at Z=-0.029, extrude up to Z=0.0 (amount=0.029)
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
            # Points are diametrically opposite, use perpendicular
            perp = np.array([-va[1], va[0]])
            mid_dir = perp / np.linalg.norm(perp)
        else:
            mid_dir = mid_dir / norm
        mid = c + mid_dir * r
        return tuple(mid)

    # All points (XY in sketch coords)
    pts = [
        (4.035, 1.379),    # 0  P1
        (3.543, 1.379),    # 1  P2
        (3.45, 1.472),     # 2  P3
        (3.45, 1.53),      # 3  P4
        (3.138, 1.829),    # 4  P5
        (-3.354, 1.829),   # 5  P6
        (-3.45, 1.733),    # 6  P7
        (-3.45, 1.497),    # 7  P8
        (-3.568, 1.379),   # 8  P9
        (-4.035, 1.379),   # 9  P10
        (-4.035, 1.027),   # 10 P11
        (-3.544, 1.027),   # 11 P12
        (-3.45, 0.934),    # 12 P13
        (-3.45, -2.507),   # 13 P14
        (-3.539, -2.596),  # 14 P15
        (-4.035, -2.596),  # 15 P16
        (-4.035, -2.951),  # 16 P17
        (-3.524, -2.951),  # 17 P18
        (-3.45, -3.026),   # 18 P19
        (-3.45, -3.361),   # 19 P20
        (-3.503, -3.42),   # 20 P21
        (-3.503, -3.929),  # 21 P22
        (-3.426, -4.032),  # 22 P23
        (-2.561, -4.032),  # 23 P24
        (-2.496, -3.929),  # 24 P25
        (-2.496, -3.482),  # 25 P26
        (-2.412, -3.398),  # 26 P27
        (-1.56, -3.398),   # 27 P28
        (-1.491, -3.467),  # 28 P29
        (-1.491, -3.929),  # 29 P30
        (-1.424, -4.032),  # 30 P31
        (-0.546, -4.032),  # 31 P32
        (-0.497, -3.929),  # 32 P33
        (-0.497, -3.472),  # 33 P34
        (-0.423, -3.398),  # 34 P35
        (0.423, -3.398),   # 35 P36
        (0.497, -3.472),   # 36 P37
        (0.497, -3.929),   # 37 P38
        (0.546, -4.032),   # 38 P39
        (1.424, -4.032),   # 39 P40
        (1.491, -3.929),   # 40 P41
        (1.491, -3.467),   # 41 P42
        (1.56, -3.398),    # 42 P43
        (2.412, -3.398),   # 43 P44
        (2.496, -3.482),   # 44 P45
        (2.496, -3.929),   # 45 P46
        (2.561, -4.032),   # 46 P47
        (3.426, -4.032),   # 47 P48
        (3.503, -3.929),   # 48 P49
        (3.503, -3.42),    # 49 P50
        (3.45, -3.361),    # 50 P51
        (3.45, -3.026),    # 51 P52
        (3.524, -2.951),   # 52 P53
        (4.035, -2.951),   # 53 P54
        (4.035, -2.596),   # 54 P55
        (3.539, -2.596),   # 55 P56
        (3.45, -2.507),    # 56 P57
        (3.45, 0.935),     # 57 P58
        (3.542, 1.027),    # 58 P59
        (4.035, 1.027),    # 59 P60
    ]

    # Arc definitions: (from_idx, to_idx, centre, radius)
    arcs = {
        (1, 2): ((3.543, 1.472), 0.093),
        (5, 6): ((-3.354, 1.733), 0.096),
        (7, 8): ((-3.568, 1.497), 0.117),
        (11, 12): ((-3.544, 0.934), 0.094),
        (13, 14): ((-3.539, -2.507), 0.089),
        (17, 18): ((-3.524, -3.026), 0.074),
        (25, 26): ((-2.412, -3.482), 0.085),
        (27, 28): ((-1.56, -3.467), 0.069),
        (33, 34): ((-0.423, -3.472), 0.075),
        (35, 36): ((0.423, -3.472), 0.075),
        (41, 42): ((1.56, -3.467), 0.069),
        (43, 44): ((2.412, -3.482), 0.085),
        (51, 52): ((3.524, -3.026), 0.074),
        (55, 56): ((3.539, -2.507), 0.089),
        (57, 58): ((3.542, 0.935), 0.092),
    }

    with BuildSketch(Plane.XY.offset(-0.029)):
        with BuildLine():
            n = len(pts)
            for i in range(n):
                j = (i + 1) % n
                if (i, j) in arcs:
                    centre, r = arcs[(i, j)]
                    mid = arc_mid_from_centre(pts[i], pts[j], centre, r)
                    ThreePointArc(pts[i], mid, pts[j])
                else:
                    Line(pts[i], pts[j])
        make_face()
    extrude(amount=0.029)

    # 8 trapezoid/rect profiles at Z=0.25, extrude down to Z=0.0
    profiles = [
        [(4.035, 1.379), (4.035, 1.027), (4.0, 1.027), (4.0, 1.379)],
        [(4.035, -2.596), (4.035, -2.951), (4.0, -2.951), (4.0, -2.596)],
        [(2.561, -4.032), (2.541, -4.0), (3.45, -4.0), (3.426, -4.032)],
        [(1.424, -4.032), (0.546, -4.032), (0.531, -4.0), (1.445, -4.0)],
        [(-0.546, -4.032), (-1.424, -4.032), (-1.445, -4.0), (-0.531, -4.0)],
        [(-2.561, -4.032), (-3.426, -4.032), (-3.45, -4.0), (-2.541, -4.0)],
        [(-4.035, -2.951), (-4.035, -2.596), (-4.0, -2.596), (-4.0, -2.951)],
        [(-4.035, 1.027), (-4.035, 1.379), (-4.0, 1.379), (-4.0, 1.027)],
    ]

    for prof in profiles:
        with BuildSketch(Plane.XY.offset(0.25)):
            with BuildLine():
                Line(prof[0], prof[1])
                Line(prof[1], prof[2])
                Line(prof[2], prof[3])
                Line(prof[3], prof[0])
            make_face()
        extrude(amount=-0.25)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_FDMT80080DC.stl")