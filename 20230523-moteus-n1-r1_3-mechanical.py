from build123d import *

# Part: 20230523-moteus-n1-r1_3-mechanical

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
    # 2. Corner Holes (XZ Plane, Subtractive) - FIXED LOCATIONS
    # ---------------------------------------------------------
    hole_centers = [(-20.0, 20.0), (-20.0, -20.0), (20.0, -20.0), (20.0, 20.0)]
    with BuildSketch(Plane.XZ.offset(1.6)):
        with Locations(hole_centers):
            Circle(radius=1.3) # Dia 2.60mm
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 3. 5 Compound Subtractive Features (Left Side)
    # ---------------------------------------------------------
    feature_origins = [
        (-22.68, -12.26), (-22.68, -7.18), (-22.68, -2.1), 
        (-22.68, 2.98), (-22.68, 8.06)
    ]
    for tx, tz in feature_origins:
        # Step 1: Rect pocket (Depth 0.05mm)
        with BuildSketch(Plane.XZ.offset(1.6)):
            with Locations((tx, tz)):
                Rectangle(3.7, 4.2, align=(Align.MIN, Align.MIN))
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Step 2: Center circle (Dia 2.0mm)
        with BuildSketch(Plane.XZ.offset(1.55)):
            with Locations((tx + 1.85, tz + 2.1)):
                Circle(radius=1.0)
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

        # Step 3: 4 Small holes (Dia 0.95mm)
        hole_locs = [(0.58, 0.83), (3.12, 0.83), (0.58, 3.37), (3.12, 3.37)]
        with BuildSketch(Plane.XZ.offset(1.55)):
            with Locations([(tx + dx, tz + dz) for dx, dz in hole_locs]):
                Circle(radius=0.475)
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 4. 12 Additive Rectangular Bodies (XZ Plane) - FIXED LOCATIONS
    # ---------------------------------------------------------
    rect_data = [
        (-17.3, -17.2, -11.3, -12.13, 2.7, 1.6),
        (-17.3, -11.334, -11.3, -6.264, 2.7, 1.6),
        (-17.3, -5.468, -11.3, -0.398, 2.7, 1.6),
        (-17.3, 0.398, -11.3, 5.468, 2.7, 1.6),
        (-17.3, 6.264, -11.3, 11.334, 2.7, 1.6),
        (-17.3, 12.13, -11.3, 17.2, 2.7, 1.6),
        (-12.6, -23.0, -0.6, -19.0, 5.85, 1.6),
        (1.475, -23.0, 14.725, -19.0, 5.85, 1.6),
        (17.0, -16.0, 23.0, -4.0, 5.4, 1.6),
        (18.0, 5.3, 23.0, 16.3, 5.8, 1.6),
        (5.4, 14.0, 15.4, 23.0, 6.7, 1.6),
        (-8.2, 15.3, 1.8, 23.0, 7.2, 1.6)
    ]
    for x1, z1, x2, z2, ys, ye in rect_data:
        with BuildSketch(Plane.XZ.offset(ys)):
            with Locations((min(x1, x2), min(z1, z2))):
                Rectangle(abs(x2-x1), abs(z2-z1), align=(Align.MIN, Align.MIN))
        extrude(amount=(ye - ys))

    # ---------------------------------------------------------
    # 5. Diamond Profile (Additive, XZ Plane)
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
    # 6. Rectangular Subtractions (XZ Plane Methodology)
    # ---------------------------------------------------------
    # Sub 1: X(-7.7 to 1.3), Z(23.0 to 16.3). Extrude Y(6.7 down to 2.1)
    with BuildSketch(Plane.XZ.offset(6.7)):
        with BuildLine():
            Line((-7.7, 16.3), (1.3, 16.3))
            Line((1.3, 16.3), (1.3, 23.0))
            Line((1.3, 23.0), (-7.7, 23.0))
            Line((-7.7, 23.0), (-7.7, 16.3))
        make_face()
    extrude(amount=(2.1 - 6.7), mode=Mode.SUBTRACT)

    # Sub 2: X(5.9 to 14.9), Z(23.0 to 15.0). Extrude Y(6.2 down to 2.1)
    with BuildSketch(Plane.XZ.offset(6.2)):
        with BuildLine():
            Line((5.9, 23.0), (14.9, 23.0))
            Line((14.9, 23.0), (14.9, 15.0))
            Line((14.9, 15.0), (5.9, 15.0))
            Line((5.9, 15.0), (5.9, 23.0))
        make_face()
    extrude(amount=(2.1 - 6.2), mode=Mode.SUBTRACT)
    
    # ---------------------------------------------------------
    # 7. 13 Small Circular Holes (XZ Plane, Subtractive)
    # ---------------------------------------------------------
    hole_locs_13 = [
        (-15.80, -22.20), (-14.53, -22.20),
        (-15.80, -20.93), (-14.53, -20.93),
        (-15.80, -19.66), (-14.53, -19.66),
        (-15.80, -18.39), (-14.53, -18.39),
        (16.20, -20.70), (16.20, -18.70),
        (-12.00, 20.30), (-14.00, 20.30), (-16.00, 20.30)
    ]
    with BuildSketch(Plane.XZ.offset(1.6)):
        with Locations(hole_locs_13):
            Circle(radius=0.4) # Dia 0.80mm
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 8. 9 Additional Additive Rectangular Bodies (XZ Plane)
    # ---------------------------------------------------------
    # Points mapped to (x1, z1, x2, z2, y_start, y_end)
    new_rect_data_9 = [
        (-8.2, 23.0, 1.8, 14.0, -5.0, 0.0),    # Set 1 (p1, p2, p3)
        (5.4, 23.0, 15.4, 15.4, -5.6, 0.0),   # Set 2 (p4, p5, p6)
        (15.0, 13.8, 22.2, -3.2, -1.8, 0.0),  # Set 3 (p7, p8, p9)
        (5.7, -5.44, 12.7, -12.44, -0.6, 0.0),# Set 4 (p10, p11, p12)
        (16.9, -14.4, 20.3, -16.0, -1.8, 0.0),# Set 5 (p13, p14, p15)
        (-3.5, 2.6, 3.5, -2.6, -1.0, 0.0),    # Set 6 (p16, p17, p18)
        (-9.1, 8.0, -4.7, -17.0, -1.8, 0.0),  # Set 7 (p19, p20, p21)
        (-13.3, 17.0, -9.7, -17.0, -1.8, 0.0),# Set 8 (p22, p23, p24)
        (-17.4, 17.0, -13.8, -17.0, -1.8, 0.0)# Set 9 (p25, p26, p27)
    ]
    for x1, z1, x2, z2, ys, ye in new_rect_data_9:
        with BuildSketch(Plane.XZ.offset(ys)):
            with Locations((min(x1, x2), min(z1, z2))):
                Rectangle(abs(x2-x1), abs(z2-z1), align=(Align.MIN, Align.MIN))
        extrude(amount=(ye - ys))

if __name__ == "__main__":
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        part.part.export_step("20230523-moteus-n1-r1_3-mechanical.step")