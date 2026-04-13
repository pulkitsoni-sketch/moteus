from build123d import *

# Part: S6B-ZR-SM4A-TF_LF__SN_

with BuildPart() as part:
    # Rect at Z=6.0 (12.0 x 3.7), extrude down to Z=0.0
    with BuildSketch(Plane.XY.offset(6.0)):
        with BuildLine():
            Line((6.0, 3.7), (-6.0, 3.7))
            Line((-6.0, 3.7), (-6.0, 0.0))
            Line((-6.0, 0.0), (6.0, 0.0))
            Line((6.0, 0.0), (6.0, 3.7))
        make_face()
    extrude(amount=-6.0)

    # Subtract rect in XZ plane at Y=3.7 (X: 5.35→6.0, Z: 3.2→4.9), extrude to Y=0.0
    sk1 = Plane(origin=(0, 3.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((5.35, 4.9), (6.0, 4.9))
            Line((6.0, 4.9), (6.0, 3.2))
            Line((6.0, 3.2), (5.35, 3.2))
            Line((5.35, 3.2), (5.35, 4.9))
        make_face()
    extrude(amount=3.7, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(sk1):
        with BuildLine():
            Line((-5.35, 4.9), (-6.0, 4.9))
            Line((-6.0, 4.9), (-6.0, 3.2))
            Line((-6.0, 3.2), (-5.35, 3.2))
            Line((-5.35, 3.2), (-5.35, 4.9))
        make_face()
    extrude(amount=3.7, mode=Mode.SUBTRACT)

    # Loft between two 12-point profiles in subtract mode
    # Outer profile at Z=6.0
    with BuildSketch(Plane.XY.offset(6.0)):
        with BuildLine():
            Line((-5.35, 3.0), (-4.95, 3.0))
            Line((-4.95, 3.0), (-4.95, 3.5))
            Line((-4.95, 3.5), (4.95, 3.5))
            Line((4.95, 3.5), (4.95, 3.0))
            Line((4.95, 3.0), (5.35, 3.0))
            Line((5.35, 3.0), (5.35, 1.8))
            Line((5.35, 1.8), (4.95, 1.8))
            Line((4.95, 1.8), (4.95, 0.4))
            Line((4.95, 0.4), (-4.95, 0.4))
            Line((-4.95, 0.4), (-4.95, 1.8))
            Line((-4.95, 1.8), (-5.35, 1.8))
            Line((-5.35, 1.8), (-5.35, 3.0))
        make_face()

    # Inner profile at Z=5.8
    with BuildSketch(Plane.XY.offset(5.8)):
        with BuildLine():
            Line((-5.35, 2.8), (-4.75, 2.8))
            Line((-4.75, 2.8), (-4.75, 3.3))
            Line((-4.75, 3.3), (4.75, 3.3))
            Line((4.75, 3.3), (4.75, 2.8))
            Line((4.75, 2.8), (5.35, 2.8))
            Line((5.35, 2.8), (5.35, 2.0))
            Line((5.35, 2.0), (4.75, 2.0))
            Line((4.75, 2.0), (4.75, 0.6))
            Line((4.75, 0.6), (-4.75, 0.6))
            Line((-4.75, 0.6), (-4.75, 2.0))
            Line((-4.75, 2.0), (-5.35, 2.0))
            Line((-5.35, 2.0), (-5.35, 2.8))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # Straight extrude inner profile from Z=5.8 down to Z=2.9
    with BuildSketch(Plane.XY.offset(5.8)):
        with BuildLine():
            Line((-5.35, 2.8), (-4.75, 2.8))
            Line((-4.75, 2.8), (-4.75, 3.3))
            Line((-4.75, 3.3), (4.75, 3.3))
            Line((4.75, 3.3), (4.75, 2.8))
            Line((4.75, 2.8), (5.35, 2.8))
            Line((5.35, 2.8), (5.35, 2.0))
            Line((5.35, 2.0), (4.75, 2.0))
            Line((4.75, 2.0), (4.75, 0.6))
            Line((4.75, 0.6), (-4.75, 0.6))
            Line((-4.75, 0.6), (-4.75, 2.0))
            Line((-4.75, 2.0), (-5.35, 2.0))
            Line((-5.35, 2.0), (-5.35, 2.8))
        make_face()
    extrude(amount=-2.9, mode=Mode.SUBTRACT)

    # Subtract rect in XZ plane at Y=3.7 (X: 4.05→4.75, Z: 3.2→4.2), extrude to Y=3.3
    sk2 = Plane(origin=(0, 3.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk2):
        with BuildLine():
            Line((4.05, 3.2), (4.75, 3.2))
            Line((4.75, 3.2), (4.75, 4.2))
            Line((4.75, 4.2), (4.05, 4.2))
            Line((4.05, 4.2), (4.05, 3.2))
        make_face()
    extrude(amount=0.4, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(sk2):
        with BuildLine():
            Line((-4.05, 3.2), (-4.75, 3.2))
            Line((-4.75, 3.2), (-4.75, 4.2))
            Line((-4.75, 4.2), (-4.05, 4.2))
            Line((-4.05, 4.2), (-4.05, 3.2))
        make_face()
    extrude(amount=0.4, mode=Mode.SUBTRACT)

    # Subtract rect in XZ plane at Y=0.0 (X: -5.5→5.5, Z: 0.0→1.0), extrude to Y=3.7
    sk3 = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((-5.5, 0.0), (5.5, 0.0))
            Line((5.5, 0.0), (5.5, 1.0))
            Line((5.5, 1.0), (-5.5, 1.0))
            Line((-5.5, 1.0), (-5.5, 0.0))
        make_face()
    extrude(amount=-3.7, mode=Mode.SUBTRACT)

    # Subtract triangle in YZ plane at X=6.0, extrude to X=-6.0
    sk4 = Plane(origin=(6.0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk4):
        with BuildLine():
            Line((3.7, 1.0), (2.1, 1.0))
            Line((2.1, 1.0), (1.5, 0.0))
            Line((1.5, 0.0), (3.7, 0.0))
            Line((3.7, 0.0), (3.7, 1.0))
        make_face()
    extrude(amount=-12.0, mode=Mode.SUBTRACT)

    # 8-point profile in YZ plane at X=5.55, extrude to X=5.35
    sk5 = Plane(origin=(5.55, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5):
        with BuildLine():
            Line((3.65, 4.9), (3.65, 3.2))
            Line((3.65, 3.2), (0.75, 3.2))
            Line((0.75, 3.2), (0.75, 3.3))
            Line((0.75, 3.3), (0.25, 3.3))
            Line((0.25, 3.3), (0.25, 4.8))
            Line((0.25, 4.8), (0.75, 4.8))
            Line((0.75, 4.8), (0.75, 4.9))
            Line((0.75, 4.9), (3.65, 4.9))
        make_face()
    extrude(amount=-0.2)

    # Mirror: 8-point profile on -X side at X=-5.55, extrude to X=-5.35
    sk5m = Plane(origin=(-5.55, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5m):
        with BuildLine():
            Line((3.65, 4.9), (3.65, 3.2))
            Line((3.65, 3.2), (0.75, 3.2))
            Line((0.75, 3.2), (0.75, 3.3))
            Line((0.75, 3.3), (0.25, 3.3))
            Line((0.25, 3.3), (0.25, 4.8))
            Line((0.25, 4.8), (0.75, 4.8))
            Line((0.75, 4.8), (0.75, 4.9))
            Line((0.75, 4.9), (3.65, 4.9))
        make_face()
    extrude(amount=0.2)

    # 6-point profile with 2 arcs at Z=4.8, extrude to Z=3.3
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

    am1 = arc_mid_from_centre((5.55, 0.25), (5.6, 0.2), (5.60, 0.25), 0.05)
    am2 = arc_mid_from_centre((5.6, 0.0), (5.35, 0.25), (5.60, 0.25), 0.25)

    with BuildSketch(Plane.XY.offset(4.8)):
        with BuildLine():
            ThreePointArc((5.55, 0.25), am1, (5.6, 0.2))
            Line((5.6, 0.2), (5.95, 0.2))
            Line((5.95, 0.2), (5.95, 0.0))
            Line((5.95, 0.0), (5.6, 0.0))
            ThreePointArc((5.6, 0.0), am2, (5.35, 0.25))
            Line((5.35, 0.25), (5.55, 0.25))
        make_face()
    extrude(amount=-1.5)

    # Mirror: -X side
    am1n = arc_mid_from_centre((-5.55, 0.25), (-5.6, 0.2), (-5.60, 0.25), 0.05)
    am2n = arc_mid_from_centre((-5.6, 0.0), (-5.35, 0.25), (-5.60, 0.25), 0.25)

    with BuildSketch(Plane.XY.offset(4.8)):
        with BuildLine():
            ThreePointArc((-5.55, 0.25), am1n, (-5.6, 0.2))
            Line((-5.6, 0.2), (-5.95, 0.2))
            Line((-5.95, 0.2), (-5.95, 0.0))
            Line((-5.95, 0.0), (-5.6, 0.0))
            ThreePointArc((-5.6, 0.0), am2n, (-5.35, 0.25))
            Line((-5.35, 0.25), (-5.55, 0.25))
        make_face()
    extrude(amount=-1.5)

    # 6 cylinder + loft pin bodies
    pin_x = [3.75, 2.25, 0.75, -0.75, -2.25, -3.75]

    for px in pin_x:
        # Cylinder: circle dia 0.5 at Z=2.9, extrude +2.18 to Z=5.08
        with BuildSketch(Plane.XY.offset(2.9)):
            with Locations([(px, 2.4)]):
                Circle(radius=0.25)
        extrude(amount=2.18)

        # Loft from Z=5.08 (dia 0.5) to Z=5.3 (dia 0.34)
        with BuildSketch(Plane.XY.offset(5.08)):
            with Locations([(px, 2.4)]):
                Circle(radius=0.25)

        with BuildSketch(Plane.XY.offset(5.3)):
            with Locations([(px, 2.4)]):
                Circle(radius=0.17)

        loft()

    # 6 downward pin bodies (cylinder + bottom loft + spline top)
    pin_x_down = [3.75, 2.25, 0.75, -0.75, -2.25, -3.75]

    spline_base = [
        (0.0, 0.318), (0.065, 0.305), (0.115, 0.278), (0.151, 0.249),
        (0.19, 0.204), (0.218, 0.159), (0.233, 0.125), (0.243, 0.088),
        (0.25, 0.038), (0.246, -0.019), (0.228, -0.083), (0.199, -0.133),
        (0.147, -0.185), (0.061, -0.226), (-0.022, -0.233), (-0.109, -0.208),
        (-0.208, -0.118), (-0.247, -0.012), (-0.24, 0.1), (-0.211, 0.171),
        (-0.16, 0.24), (-0.074, 0.301), (0.0, 0.318),
    ]

    for px in pin_x_down:
        # Cylinder: dia 0.5 at Z=0.85, extrude -1.13 to Z=-0.28
        with BuildSketch(Plane.XY.offset(0.85)):
            with Locations([(px, 0.25)]):
                Circle(radius=0.25)
        extrude(amount=-1.13)

        # Bottom loft: Z=-0.28 (dia 0.5) to Z=-0.5 (dia 0.34)
        with BuildSketch(Plane.XY.offset(-0.28)):
            with Locations([(px, 0.25)]):
                Circle(radius=0.25)

        with BuildSketch(Plane.XY.offset(-0.5)):
            with Locations([(px, 0.25)]):
                Circle(radius=0.17)

        loft()

        # Spline top: extrude from Z=1.0 down to Z=0.85
        spline_pts = [(px + dx, 0.25 + dy) for dx, dy in spline_base]

        with BuildSketch(Plane.XY.offset(1.0)):
            with BuildLine():
                Spline(spline_pts)
            make_face()
        extrude(amount=-0.15)

    # Subtract profile in YZ plane at X=-4.75, extrude to X=4.75
    sk6 = Plane(origin=(-4.75, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6):
        with BuildLine():
            Line((1.95, 2.9), (1.65, 2.6))
            Line((1.65, 2.6), (0.6, 2.6))
            Line((0.6, 2.6), (0.6, 2.9))
            Line((0.6, 2.9), (1.95, 2.9))
        make_face()
    extrude(amount=9.5, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_S6B-ZR-SM4A-TF_LF__SN_.stl")