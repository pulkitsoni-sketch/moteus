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

# Part: XT30PW-M

with BuildPart() as part:
    # Main profile at Z=6.05, extrude to Z=-2.95
    a2 = arc_mid_from_centre((4.95, 4.0), (3.95, 5.0), (3.95, 4.0), 1.0)
    a8 = arc_mid_from_centre((-3.95, 5.0), (-4.95, 4.0), (-3.95, 4.0), 1.0)

    with BuildSketch(Plane.XY.offset(6.05)):
        with BuildLine():
            Line((-3.95, 5.0), (3.95, 5.0))
            ThreePointArc((3.95, 5.0), a2, (4.95, 4.0))
            Line((4.95, 4.0), (4.95, 0.1))
            Line((4.95, 0.1), (4.85, 0.1))
            Line((4.85, 0.1), (-4.85, 0.1))
            Line((-4.85, 0.1), (-4.95, 0.1))
            Line((-4.95, 0.1), (-4.95, 4.0))
            ThreePointArc((-4.95, 4.0), a8, (-3.95, 5.0))
        make_face()
    extrude(amount=-9.0)

    # Fillet front and back face edges by 0.1, except bottom lines (Y=0.1)
    front_back_edges = [
        e for e in part.edges()
        if (abs(e.center().Z - 6.05) < 0.01 or abs(e.center().Z - (-2.95)) < 0.01)
        and abs(e.center().Y - 0.1) > 0.01
    ]
    fillet(front_back_edges, radius=0.1)

    # 8-edge profile at Z=-2.8, extrude to Z=3.05 (subtract)
    a2s = arc_mid_from_centre((-4.45, 4.0), (-3.95, 4.5), (-3.95, 4.0), 0.5)
    a4s = arc_mid_from_centre((-3.95, 0.6), (-4.45, 1.1), (-3.95, 1.1), 0.5)

    with BuildSketch(Plane.XY.offset(-2.8)):
        with BuildLine():
            Line((-3.95, 4.5), (3.45, 4.5))
            Line((3.45, 4.5), (4.45, 3.5))
            Line((4.45, 3.5), (4.45, 1.6))
            Line((4.45, 1.6), (3.45, 0.6))
            Line((3.45, 0.6), (-3.95, 0.6))
            ThreePointArc((-3.95, 0.6), a4s, (-4.45, 1.1))
            Line((-4.45, 1.1), (-4.45, 4.0))
            ThreePointArc((-4.45, 4.0), a2s, (-3.95, 4.5))
        make_face()
    extrude(amount=5.85, mode=Mode.SUBTRACT)

    # Loft between Z=-2.95 (outer) and Z=-2.8 (inner) in subtract mode
    a2_outer = arc_mid_from_centre((-3.95, 4.65), (-4.6, 4.0), (-3.95, 4.0), 0.65)
    a4_outer = arc_mid_from_centre((-4.6, 1.1), (-3.95, 0.45), (-3.95, 1.1), 0.65)

    with BuildSketch(Plane.XY.offset(-2.95)):
        with BuildLine():
            Line((3.512, 4.65), (-3.95, 4.65))
            ThreePointArc((-3.95, 4.65), a2_outer, (-4.6, 4.0))
            Line((-4.6, 4.0), (-4.6, 1.1))
            ThreePointArc((-4.6, 1.1), a4_outer, (-3.95, 0.45))
            Line((-3.95, 0.45), (3.512, 0.45))
            Line((3.512, 0.45), (4.6, 1.538))
            Line((4.6, 1.538), (4.6, 3.562))
            Line((4.6, 3.562), (3.512, 4.65))
        make_face()

    with BuildSketch(Plane.XY.offset(-2.8)):
        with BuildLine():
            Line((-3.95, 4.5), (3.45, 4.5))
            Line((3.45, 4.5), (4.45, 3.5))
            Line((4.45, 3.5), (4.45, 1.6))
            Line((4.45, 1.6), (3.45, 0.6))
            Line((3.45, 0.6), (-3.95, 0.6))
            ThreePointArc((-3.95, 0.6), a4s, (-4.45, 1.1))
            Line((-4.45, 1.1), (-4.45, 4.0))
            ThreePointArc((-4.45, 4.0), a2s, (-3.95, 4.5))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # Two pin profiles at Z=2.85, extrude to Z=3.05
    p1_a2 = arc_mid_from_centre((-0.358, 2.85), (-0.552, 3.005), (-0.358, 3.05), 0.2)
    p1_a3 = arc_mid_from_centre((-0.552, 3.005), (-1.276, 4.131), (-2.5, 2.55), 2.0)
    p1_a4 = arc_mid_from_centre((-1.276, 4.131), (-1.184, 4.4), (-1.184, 4.25), 0.15)
    p1_a6 = arc_mid_from_centre((1.184, 4.4), (1.276, 4.131), (1.184, 4.25), 0.15)
    p1_a7 = arc_mid_from_centre((1.276, 4.131), (0.552, 3.005), (2.5, 2.55), 2.0)
    p1_a8 = arc_mid_from_centre((0.552, 3.005), (0.358, 2.85), (0.358, 3.05), 0.2)

    p2_a10 = arc_mid_from_centre((-0.552, 2.095), (-0.358, 2.25), (-0.358, 2.05), 0.2)
    p2_a11 = arc_mid_from_centre((-1.276, 0.969), (-0.552, 2.095), (-2.5, 2.55), 2.0)
    p2_a12 = arc_mid_from_centre((-1.184, 0.7), (-1.276, 0.969), (-1.184, 0.85), 0.15)
    p2_a14 = arc_mid_from_centre((1.276, 0.969), (1.184, 0.7), (1.184, 0.85), 0.15)
    p2_a15 = arc_mid_from_centre((0.552, 2.095), (1.276, 0.969), (2.5, 2.55), 2.0)
    p2_a16 = arc_mid_from_centre((0.358, 2.25), (0.552, 2.095), (0.358, 2.05), 0.2)

    with BuildSketch(Plane.XY.offset(2.85)):
        with BuildLine():
            Line((0.358, 2.85), (-0.358, 2.85))
            ThreePointArc((-0.358, 2.85), p1_a2, (-0.552, 3.005))
            ThreePointArc((-0.552, 3.005), p1_a3, (-1.276, 4.131))
            ThreePointArc((-1.276, 4.131), p1_a4, (-1.184, 4.4))
            Line((-1.184, 4.4), (1.184, 4.4))
            ThreePointArc((1.184, 4.4), p1_a6, (1.276, 4.131))
            ThreePointArc((1.276, 4.131), p1_a7, (0.552, 3.005))
            ThreePointArc((0.552, 3.005), p1_a8, (0.358, 2.85))
        make_face()

        with BuildLine():
            Line((-0.358, 2.25), (0.358, 2.25))
            ThreePointArc((0.358, 2.25), p2_a16, (0.552, 2.095))
            ThreePointArc((0.552, 2.095), p2_a15, (1.276, 0.969))
            ThreePointArc((1.276, 0.969), p2_a14, (1.184, 0.7))
            Line((1.184, 0.7), (-1.184, 0.7))
            ThreePointArc((-1.184, 0.7), p2_a12, (-1.276, 0.969))
            ThreePointArc((-1.276, 0.969), p2_a11, (-0.552, 2.095))
            ThreePointArc((-0.552, 2.095), p2_a10, (-0.358, 2.25))
        make_face()
    extrude(amount=0.2)

    # -X side pin profile in XZ plane at Y=0.1, extrude to Y=3.5
    a_s2 = arc_mid_from_centre((-5.05, 1.25), (-4.95, 1.35), (-5.05, 1.35), 0.1)
    a_s4 = arc_mid_from_centre((-5.65, 1.25), (-6.65, 0.25), (-5.65, 0.25), 1.0)
    a_s6 = arc_mid_from_centre((-6.65, -0.25), (-5.65, -1.25), (-5.65, -0.25), 1.0)
    a_s8 = arc_mid_from_centre((-4.95, -1.35), (-5.05, -1.25), (-5.05, -1.35), 0.1)

    sk_side = Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk_side):
        with BuildLine():
            Line((-4.95, 1.35), (-4.95, -1.35))
            ThreePointArc((-4.95, -1.35), a_s8, (-5.05, -1.25))
            Line((-5.05, -1.25), (-5.65, -1.25))
            ThreePointArc((-5.65, -1.25), a_s6, (-6.65, -0.25))
            Line((-6.65, -0.25), (-6.65, 0.25))
            ThreePointArc((-6.65, 0.25), a_s4, (-5.65, 1.25))
            Line((-5.65, 1.25), (-5.05, 1.25))
            ThreePointArc((-5.05, 1.25), a_s2, (-4.95, 1.35))
        make_face()
    extrude(amount=-3.4)

    # Fillet -X side pin top face
    top_face = [f for f in part.faces() if abs(f.center().Y - 3.5) < 0.02 and f.center().X < -4.8]
    if top_face:
        tf_edges = top_face[0].edges()
        for e in tf_edges:
            try:
                fillet([e], radius=0.099)
            except ValueError:
                continue

    # -X side: Loft top circles subtract
    with BuildSketch(Plane(origin=(0, 3.50, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.50, 0.0)]):
            Circle(radius=0.50)
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.50, 0.0)]):
            Circle(radius=0.45)
    loft(mode=Mode.SUBTRACT)

    # -X side: Base profile at Y=0.0, extrude to Y=0.1
    a_b4 = arc_mid_from_centre((-6.65, -0.25), (-5.65, -1.25), (-5.65, -0.25), 1.0)
    a_b6 = arc_mid_from_centre((-5.65, 1.25), (-6.65, 0.25), (-5.65, 0.25), 1.0)

    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with BuildLine():
            Line((-5.65, 1.25), (-3.65, 1.25))
            Line((-3.65, 1.25), (-3.65, -1.25))
            Line((-3.65, -1.25), (-5.65, -1.25))
            ThreePointArc((-5.65, -1.25), a_b4, (-6.65, -0.25))
            Line((-6.65, -0.25), (-6.65, 0.25))
            ThreePointArc((-6.65, 0.25), a_b6, (-5.65, 1.25))
        make_face()
    extrude(amount=-0.1)

    # -X side: Loft bottom circles subtract
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.50, 0.0)]):
            Circle(radius=0.50)
    with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.50, 0.0)]):
            Circle(radius=0.45)
    loft(mode=Mode.SUBTRACT)

    # -X side: Extrude circle dia 0.9 subtract
    with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.50, 0.0)]):
            Circle(radius=0.45)
    extrude(amount=-3.4, mode=Mode.SUBTRACT)

    # -X side: Loft circle 1->2
    with BuildSketch(Plane(origin=(0, -2.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.3695)
    with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.45)
    loft()

    # -X side: Loft circle 2->3
    with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.45)
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.45)
    loft()

    # -X side: Loft circle 3->4
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.45)
    with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-5.5, 0.0)]):
            Circle(radius=0.40)
    loft()

    # +X side pin profile in XZ plane at Y=0.1, extrude to Y=3.5
    a_s2m = arc_mid_from_centre((5.05, 1.25), (4.95, 1.35), (5.05, 1.35), 0.1)
    a_s4m = arc_mid_from_centre((5.65, 1.25), (6.65, 0.25), (5.65, 0.25), 1.0)
    a_s6m = arc_mid_from_centre((6.65, -0.25), (5.65, -1.25), (5.65, -0.25), 1.0)
    a_s8m = arc_mid_from_centre((4.95, -1.35), (5.05, -1.25), (5.05, -1.35), 0.1)

    with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with BuildLine():
            Line((4.95, 1.35), (4.95, -1.35))
            ThreePointArc((4.95, -1.35), a_s8m, (5.05, -1.25))
            Line((5.05, -1.25), (5.65, -1.25))
            ThreePointArc((5.65, -1.25), a_s6m, (6.65, -0.25))
            Line((6.65, -0.25), (6.65, 0.25))
            ThreePointArc((6.65, 0.25), a_s4m, (5.65, 1.25))
            Line((5.65, 1.25), (5.05, 1.25))
            ThreePointArc((5.05, 1.25), a_s2m, (4.95, 1.35))
        make_face()
    extrude(amount=-3.4)

    # Fillet +X side pin top face
    top_face_m = [f for f in part.faces() if abs(f.center().Y - 3.5) < 0.02 and f.center().X > 4.8]
    if top_face_m:
        tf_edges_m = top_face_m[0].edges()
        for e in tf_edges_m:
            try:
                fillet([e], radius=0.099)
            except ValueError:
                continue

    # +X side: Loft top circles subtract
    with BuildSketch(Plane(origin=(0, 3.50, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.50, 0.0)]):
            Circle(radius=0.50)
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.50, 0.0)]):
            Circle(radius=0.45)
    loft(mode=Mode.SUBTRACT)

    # +X side: Base profile at Y=0.0, extrude to Y=0.1
    a_b4m = arc_mid_from_centre((6.65, -0.25), (5.65, -1.25), (5.65, -0.25), 1.0)
    a_b6m = arc_mid_from_centre((5.65, 1.25), (6.65, 0.25), (5.65, 0.25), 1.0)

    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with BuildLine():
            Line((5.65, 1.25), (3.65, 1.25))
            Line((3.65, 1.25), (3.65, -1.25))
            Line((3.65, -1.25), (5.65, -1.25))
            ThreePointArc((5.65, -1.25), a_b4m, (6.65, -0.25))
            Line((6.65, -0.25), (6.65, 0.25))
            ThreePointArc((6.65, 0.25), a_b6m, (5.65, 1.25))
        make_face()
    extrude(amount=-0.1)

    # +X side: Loft bottom circles subtract
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.50, 0.0)]):
            Circle(radius=0.50)
    with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.50, 0.0)]):
            Circle(radius=0.45)
    loft(mode=Mode.SUBTRACT)

    # +X side: Extrude circle dia 0.9 subtract
    with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.50, 0.0)]):
            Circle(radius=0.45)
    extrude(amount=-3.4, mode=Mode.SUBTRACT)

    # +X side: Loft circle 1->2
    with BuildSketch(Plane(origin=(0, -2.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.3695)
    with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.45)
    loft()

    # +X side: Loft circle 2->3
    with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.45)
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.45)
    loft()

    # +X side: Loft circle 3->4
    with BuildSketch(Plane(origin=(0, 3.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.45)
    with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(5.5, 0.0)]):
            Circle(radius=0.40)
    loft()

    # -X side: Circle at (-2.50, 2.55, 3.05), dia 2.50, extrude to Z=2.30
    with BuildSketch(Plane.XY.offset(3.05)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.25)
    extrude(amount=-0.75)

    # -X side: Loft from Z=2.30 to Z=2.05
    with BuildSketch(Plane.XY.offset(2.30)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.25)
    with BuildSketch(Plane.XY.offset(2.05)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.0)
    loft()

    # -X side: Extrude circle dia 2.0 from Z=2.05 to Z=-1.95
    with BuildSketch(Plane.XY.offset(2.05)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.0)
    extrude(amount=-4.0)

    # -X side: Fillet circle edge at Z=-1.95
    bottom_circle_edges = [
        e for e in part.edges()
        if abs(e.center().Z - (-1.95)) < 0.02
        and abs(e.center().X - (-2.50)) < 1.1
        and abs(e.center().Y - 2.55) < 1.1
    ]
    if bottom_circle_edges:
        fillet(bottom_circle_edges, radius=0.5)

    # +X side: Circle at (2.50, 2.55, 3.05), dia 2.50, extrude to Z=2.30
    with BuildSketch(Plane.XY.offset(3.05)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.25)
    extrude(amount=-0.75)

    # +X side: Loft from Z=2.30 to Z=2.05
    with BuildSketch(Plane.XY.offset(2.30)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.25)
    with BuildSketch(Plane.XY.offset(2.05)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.0)
    loft()

    # +X side: Extrude circle dia 2.0 from Z=2.05 to Z=-1.95
    with BuildSketch(Plane.XY.offset(2.05)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.0)
    extrude(amount=-4.0)

    # +X side: Fillet bottom circle edge at Z=-1.95
    bottom_circle_edges_m = [
        e for e in part.edges()
        if abs(e.center().Z - (-1.95)) < 0.02
        and abs(e.center().Y - 2.55) < 1.1
        and e.center().X > 1.0
    ]
    if bottom_circle_edges_m:
        fillet(bottom_circle_edges_m, radius=0.5)

    # -X side: Cross profile at Z=2.05, subtract
    with BuildSketch(Plane.XY.offset(2.05)):
        with BuildLine():
            RadiusArc((-2.359, 3.54), (-2.641, 3.54), -0.99)
            RadiusArc((-2.641, 3.54), (-2.55, 3.461), 0.09)
            Line((-2.55, 3.461), (-2.55, 2.6))
            Line((-2.55, 2.6), (-3.411, 2.6))
            RadiusArc((-3.411, 2.6), (-3.49, 2.691), 0.09)
            RadiusArc((-3.49, 2.691), (-3.49, 2.409), -0.99)
            RadiusArc((-3.49, 2.409), (-3.411, 2.5), 0.09)
            Line((-3.411, 2.5), (-2.55, 2.5))
            Line((-2.55, 2.5), (-2.55, 1.639))
            RadiusArc((-2.55, 1.639), (-2.641, 1.56), 0.09)
            RadiusArc((-2.641, 1.56), (-2.359, 1.56), -0.99)
            RadiusArc((-2.359, 1.56), (-2.45, 1.639), 0.09)
            Line((-2.45, 1.639), (-2.45, 2.5))
            Line((-2.45, 2.5), (-1.589, 2.5))
            RadiusArc((-1.589, 2.5), (-1.51, 2.409), 0.09)
            RadiusArc((-1.51, 2.409), (-1.51, 2.691), -0.99)
            RadiusArc((-1.51, 2.691), (-1.589, 2.6), 0.09)
            Line((-1.589, 2.6), (-2.45, 2.6))
            Line((-2.45, 2.6), (-2.45, 3.461))
            RadiusArc((-2.45, 3.461), (-2.359, 3.54), 0.09)
        make_face()
    extrude(amount=-4.0, mode=Mode.SUBTRACT)

    # +X side: Cross profile at Z=2.05, subtract
    with BuildSketch(Plane.XY.offset(2.05)):
        with BuildLine():
            RadiusArc((2.359, 3.54), (2.641, 3.54), 0.99)
            RadiusArc((2.641, 3.54), (2.55, 3.461), -0.09)
            Line((2.55, 3.461), (2.55, 2.6))
            Line((2.55, 2.6), (3.411, 2.6))
            RadiusArc((3.411, 2.6), (3.49, 2.691), -0.09)
            RadiusArc((3.49, 2.691), (3.49, 2.409), 0.99)
            RadiusArc((3.49, 2.409), (3.411, 2.5), -0.09)
            Line((3.411, 2.5), (2.55, 2.5))
            Line((2.55, 2.5), (2.55, 1.639))
            RadiusArc((2.55, 1.639), (2.641, 1.56), -0.09)
            RadiusArc((2.641, 1.56), (2.359, 1.56), 0.99)
            RadiusArc((2.359, 1.56), (2.45, 1.639), -0.09)
            Line((2.45, 1.639), (2.45, 2.5))
            Line((2.45, 2.5), (1.589, 2.5))
            RadiusArc((1.589, 2.5), (1.51, 2.409), -0.09)
            RadiusArc((1.51, 2.409), (1.51, 2.691), 0.99)
            RadiusArc((1.51, 2.691), (1.589, 2.6), -0.09)
            Line((1.589, 2.6), (2.45, 2.6))
            Line((2.45, 2.6), (2.45, 3.461))
            RadiusArc((2.45, 3.461), (2.359, 3.54), -0.09)
        make_face()
    extrude(amount=-4.0, mode=Mode.SUBTRACT)

    # -X side: Circle at (-2.50, 2.55, 6.05), dia 2.50, extrude +2.0
    with BuildSketch(Plane.XY.offset(6.05)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.25)
    extrude(amount=2.0)

    # -X side: Fillet top face edge at Z=8.05
    top_cyl_edges = [
        e for e in part.edges()
        if abs(e.center().Z - 8.05) < 0.02
        and abs(e.center().X - (-2.50)) < 1.3
        and abs(e.center().Y - 2.55) < 1.3
    ]
    if top_cyl_edges:
        fillet(top_cyl_edges, radius=0.1)

    # -X side: Circle at (-2.50, 2.55, 8.05), dia 2.0, extrude +0.95
    with BuildSketch(Plane.XY.offset(8.05)):
        with Locations([(-2.50, 2.55)]):
            Circle(radius=1.0)
    extrude(amount=0.95)

    # -X side: Fillet edge at Z=8.05
    fillet_edges_805 = [
        e for e in part.edges()
        if abs(e.center().Z - 8.05) < 0.02
        and abs(e.center().X - (-2.50)) < 1.05
        and abs(e.center().Y - 2.55) < 1.05
    ]
    if fillet_edges_805:
        fillet(fillet_edges_805, radius=0.1)

    # -X side: Sweep 90 pipe bend
    with BuildLine() as sweep_path:
        ThreePointArc(
            (-2.50, 2.55, 9.0),
            (-2.50, 2.2571, 9.7071),
            (-2.50, 1.55, 10.0),
        )
    with BuildSketch(Plane(origin=(-2.50, 2.55, 9.0), z_dir=(0, 0, 1))) as sweep_section:
        Circle(radius=1.0)
    sweep(sweep_section.sketch, path=sweep_path.wires()[0])

    # -X side: Extrude from Y=0.1 to Y=1.55
    with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=1.0)
    extrude(amount=-1.45)

    # -X side: Loft Y=0.1 to Y=0.0
    with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=1.0)
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=0.9)
    loft()

    # -X side: Extrude dia 1.5 from Y=0.0 to Y=-1.5
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=0.75)
    extrude(amount=1.5)

    # -X side: Loft Y=-1.5 to Y=-2.0
    with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=0.75)
    with BuildSketch(Plane(origin=(0, -2.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(-2.50, 10.0)]):
            Circle(radius=0.616)
    loft()

    # +X side: Circle at (2.50, 2.55, 6.05), dia 2.50, extrude +2.0
    with BuildSketch(Plane.XY.offset(6.05)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.25)
    extrude(amount=2.0)

    #import math
    #with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 1, 0), z_dir=(0, 0, 1))):
    #    with BuildLine():
    #        # Local 2D coordinates (Y, Z)
    #        p1_local = (3.8, 7.95)
    #        p2_local = (3.8, 8.05)
    #        p3_local = (3.7, 8.05)
    #        p4_local = (3.7, 7.95) # Center of the arc
    #        
    #        # Connect p1 to p2, and p2 to p3 with straight lines
    #        Line(p1_local, p2_local)
    #        Line(p2_local, p3_local)
    #        
    #        # Connect p3 back to p1 with an inward arc centered at p4
    #        # We calculate the 45-degree midpoint to ensure a flawless ThreePointArc
    #        mid_y = p4_local[0] + 0.1 * math.cos(math.radians(45))
    #        mid_z = p4_local[1] + 0.1 * math.sin(math.radians(45))
    #        
    #        ThreePointArc(p3_local, (mid_y, mid_z), p1_local)
            
    #    make_face()

    # Define the 3D axis of revolution based on the sketched line points
    # Point 1: (2.5, 2.55, 7.95), Point 2: (2.5, 2.55, 6.373)
    # The direction vector points straight down the -Z axis (0, 0, -1)
    #rev_axis = Axis(origin=(2.5, 2.55, 7.95), direction=(0, 0, -1))
    
    # Revolve the sketched profile around the axis
    #revolve(axis=rev_axis, mode=Mode.SUBTRACT)

    # +X side: Circle at (2.50, 2.55, 8.05), dia 2.0, extrude +0.95
    with BuildSketch(Plane.XY.offset(8.05)):
        with Locations([(2.50, 2.55)]):
            Circle(radius=1.0)
    extrude(amount=0.95)

    # +X side: Fillet edge at Z=8.05
    #fillet_edges_805 = [
    #    e for e in part.edges()
    #    if abs(e.center().Z - 8.05) < 0.02
    #    and abs(e.center().X - 2.50) < 1.05
    #    and abs(e.center().Y - 2.55) < 1.05
    #]
    # if fillet_edges_805:
    #    fillet(fillet_edges_805, radius=0.1)

    # +X side: Sweep 90 pipe bend
    with BuildLine() as sweep_path:
        ThreePointArc(
            (2.50, 2.55, 9.0),
            (2.50, 2.2571, 9.7071),
            (2.50, 1.55, 10.0),
        )
    with BuildSketch(Plane(origin=(2.50, 2.55, 9.0), z_dir=(0, 0, 1))) as sweep_section:
        Circle(radius=1.0)
    sweep(sweep_section.sketch, path=sweep_path.wires()[0])

    # +X side: Extrude from Y=0.1 to Y=1.55
    with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=1.0)
    extrude(amount=-1.45)

    # +X side: Loft Y=0.1 to Y=0.0
    with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=1.0)
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=0.9)
    loft()

    # +X side: Extrude dia 1.5 from Y=0.0 to Y=-1.5
    with BuildSketch(Plane(origin=(0, 0.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=0.75)
    extrude(amount=1.5)

    # +X side: Loft Y=-1.5 to Y=-2.0
    with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=0.75)
    with BuildSketch(Plane(origin=(0, -2.0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
        with Locations([(2.50, 10.0)]):
            Circle(radius=0.616)
    loft()

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_XT30PW-M.stl")
