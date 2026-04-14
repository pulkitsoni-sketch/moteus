from build123d import *
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

# Part: SM07B-GHS-TB-LF--SN---3DModel-STEP-56544
with BuildPart() as part:
    # 1. Base Rect in XZ plane at Y=4.35
    sk_base = Plane(origin=(0, 4.35, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk_base):
        with BuildLine():
            Line((-6.0, 2.425), (6.0, 2.425))
            Line((6.0, 2.425), (6.0, -1.625))
            Line((6.0, -1.625), (-6.0, -1.625))
            Line((-6.0, -1.625), (-6.0, 2.425))
        make_face()
    extrude(amount=4.25)

    # 2. 6-point profile in YZ plane at X=6.0, extrude to X=-6.0 (subtract)
    sk_cut1 = Plane(origin=(6.0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk_cut1):
        with BuildLine():
            Line((1.05, -1.625), (1.05, -1.125))
            Line((1.05, -1.125), (0.3, -1.125))
            Line((0.3, -1.125), (0.3, -0.975))
            Line((0.3, -0.975), (0.1, -0.975))
            Line((0.1, -0.975), (0.1, -1.625))
            Line((0.1, -1.625), (1.05, -1.625))
        make_face()
    extrude(amount=-12.0, mode=Mode.SUBTRACT)

    # 3. Rectangular cutout in XY plane at Z=-1.625 (subtract)
    sk_cut2 = Plane(origin=(0, 0, -1.625), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_cut2):
        with BuildLine():
            Line((-4.1, 3.95), (4.1, 3.95))
            Line((4.1, 3.95), (4.1, 2.55))
            Line((4.1, 2.55), (-4.1, 2.55))
            Line((-4.1, 2.55), (-4.1, 3.95))
        make_face()
    extrude(amount=3.85, mode=Mode.SUBTRACT)

    # 4. Rectangular body in XY plane at Z=1.625 (add)
    sk_add1 = Plane(origin=(0, 0, 1.625), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_add1):
        with BuildLine():
            Line((-3.125, 2.95), (3.1, 2.95))
            Line((3.1, 2.95), (3.1, 2.55))
            Line((3.1, 2.55), (-3.125, 2.55))
            Line((-3.125, 2.55), (-3.125, 2.95))
        make_face()
    extrude(amount=-1.0, mode=Mode.ADD)

    # 5. Lofted Cut between Z=2.425 and Z=2.225 (subtract)
    sk_loft_top = Plane(origin=(0, 0, 2.425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_loft_top):
        with BuildLine():
            Line((-4.1, 4.15), (4.1, 4.15))
            Line((4.1, 4.15), (4.1, 2.35))
            Line((4.1, 2.35), (-4.1, 2.35))
            Line((-4.1, 2.35), (-4.1, 4.15))
        make_face()

    sk_loft_bot = Plane(origin=(0, 0, 2.225), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_loft_bot):
        with BuildLine():
            Line((-4.1, 3.95), (4.1, 3.95))
            Line((4.1, 3.95), (4.1, 2.55))
            Line((4.1, 2.55), (-4.1, 2.55))
            Line((-4.1, 2.55), (-4.1, 3.95))
        make_face()
    loft(mode=Mode.SUBTRACT)

    # 6. Side Cutouts (X=5.9 and X=-5.9)
    for x_pos, amt in [(5.9, 0.1), (-5.9, -0.1)]:
        sk_side = Plane(origin=(x_pos, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_side):
            with BuildLine():
                Line((3.45, 2.425), (3.45, 0.65))
                Line((3.45, 0.65), (2.4, 0.65))
                Line((2.4, 0.65), (2.4, 2.425))
                Line((2.4, 2.425), (3.45, 2.425))
            make_face()
        extrude(amount=amt, mode=Mode.SUBTRACT)

    # 7 & 10. Mirroring slot cuts
    for x_pos, amt in [(5.0, 1.0), (-5.0, -1.0)]:
        sk_slot = Plane(origin=(x_pos, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_slot):
            with BuildLine():
                Line((4.35, -1.625), (4.35, -1.375))
                Line((4.35, -1.375), (2.1, -1.375))
                Line((2.1, -1.375), (2.1, -1.625))
                Line((2.1, -1.625), (4.35, -1.625))
            make_face()
        extrude(amount=amt, mode=Mode.SUBTRACT)

    # 8 & 11. Complex side cuts
    for x_pos, amt in [(5.5, 0.5), (-5.5, -0.5)]:
        sk_comp = Plane(origin=(x_pos, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_comp):
            with BuildLine():
                Line((4.243, 0.275), (4.243, -1.375))
                Line((4.243, -1.375), (2.1, -1.375))
                Line((2.1, -1.375), (2.1, -1.025))
                Line((2.1, -1.025), (3.65, -1.025))
                Line((3.65, -1.025), (3.75, -0.925))
                Line((3.75, -0.925), (3.75, 0.275))
                Line((3.75, 0.275), (4.243, 0.275))
            make_face()
        extrude(amount=amt, mode=Mode.SUBTRACT)

    # 9 & 12. Secondary Loft
    for x_sign in [1, -1]:
        sk_l2_top = Plane(origin=(0, 4.35, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_l2_top):
            with BuildLine():
                Line((x_sign*5.45, 0.325), (x_sign*6.0, 0.325))
                Line((x_sign*6.0, 0.325), (x_sign*6.0, -1.375))
                Line((x_sign*6.0, -1.375), (x_sign*5.45, -1.375))
                Line((x_sign*5.45, -1.375), (x_sign*5.45, 0.325))
            make_face()
        sk_l2_bot = Plane(origin=(0, 4.243, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_l2_bot):
            with BuildLine():
                Line((x_sign*5.5, 0.275), (x_sign*6.0, 0.275))
                Line((x_sign*6.0, 0.275), (x_sign*6.0, -1.375))
                Line((x_sign*6.0, -1.375), (x_sign*5.5, -1.375))
                Line((x_sign*5.5, -1.375), (x_sign*5.5, 0.275))
            make_face()
        loft(mode=Mode.SUBTRACT)

    # 13. Comb Extrude
    sk_comb_str = Plane(origin=(0, 0, 2.225), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_comb_str):
        with BuildLine():
            Line((-5.0, 2.75), (-4.5, 2.75))
            Line((-4.5, 2.75), (-4.5, 2.25))
            Line((-4.5, 2.25), (-4.1, 2.25))
            Line((-4.1, 2.25), (-4.1, 1.85))
            Line((-4.1, 1.85), (-3.4, 1.85))
            Line((-3.4, 1.85), (-3.4, 2.25))
            Line((-3.4, 2.25), (-2.85, 2.25))
            Line((-2.85, 2.25), (-2.85, 1.85))
            Line((-2.85, 1.85), (-2.15, 1.85))
            Line((-2.15, 1.85), (-2.15, 2.25))
            Line((-2.15, 2.25), (-1.6, 2.25))
            Line((-1.6, 2.25), (-1.6, 1.85))
            Line((-1.6, 1.85), (-0.9, 1.85))
            Line((-0.9, 1.85), (-0.9, 2.25))
            Line((-0.9, 2.25), (-0.35, 2.25))
            Line((-0.35, 2.25), (-0.35, 1.85))
            Line((-0.35, 1.85), (0.35, 1.85))
            Line((0.35, 1.85), (0.35, 2.25))
            Line((0.35, 2.25), (0.9, 2.25))
            Line((0.9, 2.25), (0.9, 1.85))
            Line((0.9, 1.85), (1.6, 1.85))
            Line((1.6, 1.85), (1.6, 2.25))
            Line((1.6, 2.25), (2.15, 2.25))
            Line((2.15, 2.25), (2.15, 1.85))
            Line((2.15, 1.85), (2.85, 1.85))
            Line((2.85, 1.85), (2.85, 2.25))
            Line((2.85, 2.25), (3.4, 2.25))
            Line((3.4, 2.25), (3.4, 1.85))
            Line((3.4, 1.85), (4.1, 1.85))
            Line((4.1, 1.85), (4.1, 2.25))
            Line((4.1, 2.25), (4.5, 2.25))
            Line((4.5, 2.25), (4.5, 2.75))
            Line((4.5, 2.75), (5.0, 2.75))
            Line((5.0, 2.75), (5.0, 0.7))
            Line((5.0, 0.7), (-5.0, 0.7))
            Line((-5.0, 0.7), (-5.0, 2.75))
        make_face()
    extrude(amount=-2.4, mode=Mode.SUBTRACT)

    # 14. Comb Loft
    sk_comb_t = Plane(origin=(0, 0, 2.425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_comb_t):
        with BuildLine():
            Line((-5.2, 2.95), (-4.3, 2.95))
            Line((-4.3, 2.95), (-4.3, 2.25))
            Line((-4.3, 2.25), (-4.1, 2.25))
            Line((-4.1, 2.25), (-4.1, 2.05))
            Line((-4.1, 2.05), (-3.4, 2.05))
            Line((-3.4, 2.05), (-3.4, 2.25))
            Line((-3.4, 2.25), (-2.85, 2.25))
            Line((-2.85, 2.25), (-2.85, 2.05))
            Line((-2.85, 2.05), (-2.15, 2.05))
            Line((-2.15, 2.05), (-2.15, 2.25))
            Line((-2.15, 2.25), (-1.6, 2.25))
            Line((-1.6, 2.25), (-1.6, 2.05))
            Line((-1.6, 2.05), (-0.9, 2.05))
            Line((-0.9, 2.05), (-0.9, 2.25))
            Line((-0.9, 2.25), (-0.35, 2.25))
            Line((-0.35, 2.25), (-0.35, 2.05))
            Line((-0.35, 2.05), (0.35, 2.05))
            Line((0.35, 2.05), (0.35, 2.25))
            Line((0.35, 2.25), (0.9, 2.25))
            Line((0.9, 2.25), (0.9, 2.05))
            Line((0.9, 2.05), (1.6, 2.05))
            Line((1.6, 2.05), (1.6, 2.25))
            Line((1.6, 2.25), (2.15, 2.25))
            Line((2.15, 2.25), (2.15, 2.05))
            Line((2.15, 2.05), (2.85, 2.05))
            Line((2.85, 2.05), (2.85, 2.25))
            Line((2.85, 2.25), (3.4, 2.25))
            Line((3.4, 2.25), (3.4, 2.05))
            Line((3.4, 2.05), (4.1, 2.05))
            Line((4.1, 2.05), (4.1, 2.25))
            Line((4.1, 2.25), (4.3, 2.25))
            Line((4.3, 2.25), (4.3, 2.95))
            Line((4.3, 2.95), (5.2, 2.95))
            Line((5.2, 2.95), (5.2, 0.5))
            Line((5.2, 0.5), (-5.2, 0.5))
            Line((-5.2, 0.5), (-5.2, 2.95))
        make_face()
    sk_comb_b = Plane(origin=(0, 0, 2.225), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_comb_b):
        with BuildLine():
            Line((-5.0, 2.75), (-4.5, 2.75))
            Line((-4.5, 2.75), (-4.5, 2.25))
            Line((-4.5, 2.25), (-4.1, 2.25))
            Line((-4.1, 2.25), (-4.1, 1.85))
            Line((-4.1, 1.85), (-3.4, 1.85))
            Line((-3.4, 1.85), (-3.4, 2.25))
            Line((-3.4, 2.25), (-2.85, 2.25))
            Line((-2.85, 2.25), (-2.85, 1.85))
            Line((-2.85, 1.85), (-2.15, 1.85))
            Line((-2.15, 1.85), (-2.15, 2.25))
            Line((-2.15, 2.25), (-1.6, 2.25))
            Line((-1.6, 2.25), (-1.6, 1.85))
            Line((-1.6, 1.85), (-0.9, 1.85))
            Line((-0.9, 1.85), (-0.9, 2.25))
            Line((-0.9, 2.25), (-0.35, 2.25))
            Line((-0.35, 2.25), (-0.35, 1.85))
            Line((-0.35, 1.85), (0.35, 1.85))
            Line((0.35, 1.85), (0.35, 2.25))
            Line((0.35, 2.25), (0.9, 2.25))
            Line((0.9, 2.25), (0.9, 1.85))
            Line((0.9, 1.85), (1.6, 1.85))
            Line((1.6, 1.85), (1.6, 2.25))
            Line((1.6, 2.25), (2.15, 2.25))
            Line((2.15, 2.25), (2.15, 1.85))
            Line((2.15, 1.85), (2.85, 1.85))
            Line((2.85, 1.85), (2.85, 2.25))
            Line((2.85, 2.25), (3.4, 2.25))
            Line((3.4, 2.25), (3.4, 1.85))
            Line((3.4, 1.85), (4.1, 1.85))
            Line((4.1, 1.85), (4.1, 2.25))
            Line((4.1, 2.25), (4.5, 2.25))
            Line((4.5, 2.25), (4.5, 2.75))
            Line((4.5, 2.75), (5.0, 2.75))
            Line((5.0, 2.75), (5.0, 0.7))
            Line((5.0, 0.7), (-5.0, 0.7))
            Line((-5.0, 0.7), (-5.0, 2.75))
        make_face()
    loft(mode=Mode.SUBTRACT)

    # Safety overshoot constant
    overlap = 0.01

    # 15. 14 Internal Locking Cutouts
    top_x = [-3.85, -2.6, -1.35, -0.1, 1.15, 2.4, 3.65]
    for lx in top_x:
        sk_slot = Plane(origin=(lx - overlap, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_slot):
            with BuildLine():
                Line((2.007, 2.382), (1.85, 2.225))
                Line((1.85, 2.225), (1.85, -0.175))
                Line((1.85, -0.175), (2.007, -0.175))
                Line((2.007, -0.175), (2.007, 2.382))
            make_face()
        extrude(amount=0.2 + (2 * overlap), mode=Mode.SUBTRACT)

    bot_x = [3.85, 2.6, 1.35, 0.1, -1.15, -2.4, -3.65]
    for lx in bot_x:
        sk_slot = Plane(origin=(lx + overlap, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_slot):
            with BuildLine():
                Line((0.542, 2.482), (0.7, 2.325))
                Line((0.7, 2.325), (0.7, -0.175))
                Line((0.7, -0.175), (0.542, -0.175))
                Line((0.542, -0.175), (0.542, 2.482))
            make_face()
        extrude(amount=-0.2 - (2 * overlap), mode=Mode.SUBTRACT)

    # 16. Profile Extrusion (P1-P6 to P7)
    sk_new = Plane(origin=(0, 0, 0.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    with BuildSketch(sk_new):
        with BuildLine():
            Line((-6.0, 0.7), (-5.5, 0.7))
            Line((-5.5, 0.7), (-5.5, 0.45))
            Line((-5.5, 0.45), (-5.4, 0.45))
            Line((-5.4, 0.45), (-5.05, 0.1))
            Line((-5.05, 0.1), (-6.0, 0.1))
            Line((-6.0, 0.1), (-6.0, 0.7))
        make_face()
    extrude(amount=2.25, mode=Mode.SUBTRACT)

    # 17. Profile in XZ plane at Y=2.05, extrude to Y=0.45 (subtract)
    sk17 = Plane(origin=(0, 2.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk17):
        with BuildLine():
            Line((-6.0, 1.775), (-6.0, 2.325))
            Line((-6.0, 2.325), (-5.5, 2.325))
            Line((-5.5, 2.325), (-5.5, 0.225))
            Line((-5.5, 0.225), (-5.7, 0.225))
            Line((-5.7, 0.225), (-5.7, 1.775))
            Line((-5.7, 1.775), (-6.0, 1.775))
        make_face()
    extrude(amount=1.6, mode=Mode.SUBTRACT)

    # 18. Loft between two rects (subtract)
    # Rect at Z=2.425 (X: -6.0→-5.4, Y: 0.45→2.15)
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((-6.0, 2.15), (-5.4, 2.15))
            Line((-5.4, 2.15), (-5.4, 0.45))
            Line((-5.4, 0.45), (-6.0, 0.45))
            Line((-6.0, 0.45), (-6.0, 2.15))
        make_face()

    # Rect at Z=2.325 (X: -6.0→-5.5, Y: 0.45→2.05)
    with BuildSketch(Plane.XY.offset(2.325)):
        with BuildLine():
            Line((-6.0, 2.05), (-5.5, 2.05))
            Line((-5.5, 2.05), (-5.5, 0.45))
            Line((-5.5, 0.45), (-6.0, 0.45))
            Line((-6.0, 0.45), (-6.0, 2.05))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # 16m. Mirror: Profile Extrusion (+X side)
    with BuildSketch(Plane(origin=(0, 0, 0.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
        with BuildLine():
            Line((6.0, 0.7), (5.5, 0.7))
            Line((5.5, 0.7), (5.5, 0.45))
            Line((5.5, 0.45), (5.4, 0.45))
            Line((5.4, 0.45), (5.05, 0.1))
            Line((5.05, 0.1), (6.0, 0.1))
            Line((6.0, 0.1), (6.0, 0.7))
        make_face()
    extrude(amount=2.25, mode=Mode.SUBTRACT)

    # 17m. Mirror: Profile in XZ plane at Y=2.05 (+X side)
    with BuildSketch(Plane(origin=(0, 2.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with BuildLine():
            Line((6.0, 1.775), (6.0, 2.325))
            Line((6.0, 2.325), (5.5, 2.325))
            Line((5.5, 2.325), (5.5, 0.225))
            Line((5.5, 0.225), (5.7, 0.225))
            Line((5.7, 0.225), (5.7, 1.775))
            Line((5.7, 1.775), (6.0, 1.775))
        make_face()
    extrude(amount=1.6, mode=Mode.SUBTRACT)

    # 18m. Mirror: Loft between two rects (+X side)
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((6.0, 2.15), (5.4, 2.15))
            Line((5.4, 2.15), (5.4, 0.45))
            Line((5.4, 0.45), (6.0, 0.45))
            Line((6.0, 0.45), (6.0, 2.15))
        make_face()

    with BuildSketch(Plane.XY.offset(2.325)):
        with BuildLine():
            Line((6.0, 2.05), (5.5, 2.05))
            Line((5.5, 2.05), (5.5, 0.45))
            Line((5.5, 0.45), (6.0, 0.45))
            Line((6.0, 0.45), (6.0, 2.05))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # 19. 14-point profile in YZ plane with semicircles, +X and -X sides
    # Semicircle midpoints (bulge -Z)
    sc1 = (0.75, 2.285)   # P8→P9 semicircle midpoint
    sc2 = (1.3, 2.285)    # P12→P13 semicircle midpoint

    for x_orig, amt in [(5.7, -0.2), (-5.7, 0.2)]:
        sk_pin = Plane(origin=(x_orig, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_pin):
            with BuildLine():
                Line((2.05, 2.425), (2.05, 0.225))
                Line((2.05, 0.225), (0.1, 0.225))
                Line((0.1, 0.225), (0.0, 0.325))
                Line((0.0, 0.325), (0.0, 2.325))
                Line((0.0, 2.325), (0.1, 2.425))
                Line((0.1, 2.425), (0.65, 2.425))
                Line((0.65, 2.425), (0.65, 2.385))
                ThreePointArc((0.65, 2.385), sc1, (0.85, 2.385))
                Line((0.85, 2.385), (0.85, 2.425))
                Line((0.85, 2.425), (1.2, 2.425))
                Line((1.2, 2.425), (1.2, 2.385))
                ThreePointArc((1.2, 2.385), sc2, (1.4, 2.385))
                Line((1.4, 2.385), (1.4, 2.425))
                Line((1.4, 2.425), (2.05, 2.425))
            make_face()
        extrude(amount=amt, mode=Mode.ADD)

    # 20. Three profiles per body, 7 bodies
    body_x = [3.85, 2.6, 1.35, 0.1, -1.15, -2.4, -3.65]

    for bx in body_x:
        sk20 = Plane(origin=(bx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))

        # Profile A
        with BuildSketch(sk20):
            with BuildLine():
                Line((2.007, 2.382), (2.007, -0.175))
                Line((2.007, -0.175), (1.607, -0.175))
                Line((1.607, -0.175), (1.607, 2.083))
                Line((1.607, 2.083), (1.907, 2.382))
                Line((1.907, 2.382), (2.007, 2.382))
            make_face()
        extrude(amount=-0.2)

        # Profile B
        with BuildSketch(sk20):
            with BuildLine():
                Line((0.942, 2.182), (0.742, 2.382))
                Line((0.742, 2.382), (0.542, 2.382))
                Line((0.542, 2.382), (0.542, -0.175))
                Line((0.542, -0.175), (0.942, -0.175))
                Line((0.942, -0.175), (0.942, 2.182))
            make_face()
        extrude(amount=-0.2)

        # Profile C (with arc)
        am_c3 = arc_mid_from_centre((0.3, -1.725), (0.5, -1.525), (0.5, -1.725), 0.2)
        with BuildSketch(sk20):
            with BuildLine():
                Line((1.05, -1.125), (0.3, -1.125))
                Line((0.3, -1.125), (0.0, -1.425))
                Line((0.0, -1.425), (0.0, -2.425))
                Line((0.0, -2.425), (0.3, -2.425))
                Line((0.3, -2.425), (0.3, -1.725))
                ThreePointArc((0.3, -1.725), am_c3, (0.5, -1.525))
                Line((0.5, -1.525), (1.05, -1.525))
                Line((1.05, -1.525), (1.05, -1.125))
            make_face()
        extrude(amount=-0.2)

from ocp_vscode import show
show(part)

export_stl(part.part, "output_SM07B-GHS-TB.stl")