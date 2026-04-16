from build123d import *

# Part: 20230226-moteus-n1-mechanical

with BuildPart() as part:
    # ---------------------------------------------------------
    # 1. Main Plate (XZ Plane, Sketch @ Y=1.6, Extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(1.6)):
        with BuildLine():
            Line((20.0, 23.0), (-20.0, 23.0))
            ThreePointArc((-20.0, 23.0), (-22.121, 22.121), (-23.0, 20.0))
            Line((-23.0, 20.0), (-23.0, -20.0))
            ThreePointArc((-23.0, -20.0), (-22.121, -22.121), (-20.0, -23.0))
            Line((-20.0, -23.0), (20.0, -23.0))
            ThreePointArc((20.0, -23.0), (22.121, -22.121), (23.0, -20.0))
            Line((23.0, -20.0), (23.0, 20.0))
            ThreePointArc((23.0, 20.0), (22.121, 22.121), (20.0, 23.0))
        make_face()
    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # 2. Corner Holes (XZ Plane, Subtractive)
    # ---------------------------------------------------------
    hole_centers = [(-20.0, 20.0), (-20.0, -20.0), (20.0, -20.0), (20.0, 20.0)]
    for cx, cz in hole_centers:
        with BuildSketch(Plane.XZ.offset(1.6)):
            with BuildLine():
                ThreePointArc((cx + 1.3, cz), (cx, cz + 1.3), (cx - 1.3, cz))
                ThreePointArc((cx - 1.3, cz), (cx, cz - 1.3), (cx + 1.3, cz))
            make_face()
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 3. 5 Side Pocket Features (XZ Plane, Subtractive)
    # ---------------------------------------------------------
    side_pockets = [(-19.355, 12.26), (-19.355, 7.18), (-19.355, 2.1), (-19.355, -2.98), (-19.355, -8.06)]
    for tx, tz in side_pockets:
        with BuildSketch(Plane.XZ.offset(1.6)):
            with BuildLine():
                Line((tx, tz), (tx - 3.45, tz))
                Line((tx - 3.45, tz), (tx - 3.45, tz - 4.2))
                Line((tx - 3.45, tz - 4.2), (tx, tz - 4.2))
                Line((tx, tz - 4.2), (tx, tz))
            make_face()
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        cx, cz = tx - 1.725, tz - 2.1
        with BuildSketch(Plane.XZ.offset(1.55)):
            with BuildLine():
                ThreePointArc((cx + 1.0, cz), (cx, cz + 1.0), (cx - 1.0, cz))
                ThreePointArc((cx - 1.0, cz), (cx, cz - 1.0), (cx + 1.0, cz))
            make_face()
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 4. 12 Additive Rectangular Bodies (XZ Plane)
    # ---------------------------------------------------------
    rect_data = [
        (-13.9, -23.0, -1.9, -19.0, 5.85, 1.6),
        (1.475, -23.0, 14.725, -19.0, 5.85, 1.6),
        (17.0, -16.0, 23.0, -4.0, 5.4, 1.6),
        (18.0, 5.3, 23.0, 16.3, 5.8, 1.6),
        (5.3, 14.0, 15.3, 23.0, 6.7, 1.6),
        (-8.3, 15.3, 1.7, 23.0, 7.2, 1.6),
        (-17.6, 12.03, -11.6, 17.1, 2.7, 1.6),
        (-17.6, 6.204, -11.6, 11.274, 2.7, 1.6),
        (-17.6, 0.378, -11.6, 5.448, 2.7, 1.6),
        (-17.6, -5.448, -11.6, -0.378, 2.7, 1.6),
        (-17.6, -11.274, -11.6, -6.204, 2.7, 1.6),
        (-17.6, -17.1, -11.6, -12.03, 2.7, 1.6)
    ]
    for x1, z1, x2, z2, ys, ye in rect_data:
        with BuildSketch(Plane.XZ.offset(ys)):
            with BuildLine():
                Line((x1, z1), (x2, z1))
                Line((x2, z1), (x2, z2))
                Line((x2, z2), (x1, z2))
                Line((x1, z2), (x1, z1))
            make_face()
        extrude(amount=(ye - ys))

    # ---------------------------------------------------------
    # 5. Additive Diamond Profile (XZ Plane)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(2.4)):
        with BuildLine():
            Line((1.39, -6.243), (5.633, -2.0))
            Line((5.633, -2.0), (1.39, 2.243))
            Line((1.39, 2.243), (-2.853, -2.0))
            Line((-2.853, -2.0), (1.39, -6.243))
        make_face()
    extrude(amount=(1.6 - 2.4))

    # ---------------------------------------------------------
    # 6. 2 Rectangular Subtractions (XZ Plane, Y Extrusion)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(6.7)):
        with BuildLine():
            Line((-7.8, 23.0), (1.2, 23.0))
            Line((1.2, 23.0), (1.2, 16.3))
            Line((1.2, 16.3), (-7.8, 16.3))
            Line((-7.8, 16.3), (-7.8, 23.0))
        make_face()
    extrude(amount=(2.1 - 6.7), mode=Mode.SUBTRACT)

    with BuildSketch(Plane.XZ.offset(6.2)):
        with BuildLine():
            Line((5.8, 23.0), (14.8, 23.0))
            Line((14.8, 23.0), (14.8, 15.0))
            Line((14.8, 15.0), (5.8, 15.0))
            Line((5.8, 15.0), (5.8, 23.0))
        make_face()
    extrude(amount=(2.1 - 6.2), mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 7. 7 New Additive Rectangular Bodies (XZ Plane)
    # ---------------------------------------------------------
    # Format: (x1, z1, x2, z2, y_start, y_end)
    new_rect_data = [
        (-17.4, 17.0, -13.8, -17.0, -1.8, 0.0),
        (-13.3, 17.0, -9.7, -17.0, -1.8, 0.0),
        (-9.1, 8.0, -4.7, -17.0, -1.8, 0.0),
        (-3.5, 2.6, 3.5, -2.6, -1.0, 0.0),
        (5.7, -5.44, 12.7, -12.44, -0.6, 0.0),
        (16.9, -14.4, 20.3, -16.0, -1.8, 0.0),
        (15.0, 13.8, 22.2, -3.2, -1.8, 0.0)
    ]
    for x1, z1, x2, z2, ys, ye in new_rect_data:
        with BuildSketch(Plane.XZ.offset(ys)):
            with BuildLine():
                Line((x1, z1), (x2, z1))
                Line((x2, z1), (x2, z2))
                Line((x2, z2), (x1, z2))
                Line((x1, z2), (x1, z1))
            make_face()
        extrude(amount=(ye - ys))

if __name__ == "__main__":
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        part.part.export_step("20230226-moteus-n1-mechanical.step")