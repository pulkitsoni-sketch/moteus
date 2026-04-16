from build123d import *

# Part: 20200729-moteus-controller-r45-mechanical

with BuildPart() as part:
    # ---------------------------------------------------------
    # 1. Main Plate Profile (XZ Plane, Y: 1.65 down to 0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(1.65)):
        with BuildLine():
            p1 = (15.0, 43.0)
            p2 = (16.0, 42.0)
            p3 = (16.0, 37.0)
            p4 = (17.046, 35.493)
            p5 = (20.869, 34.069)
            p6 = (23.0, 31.0)
            p7 = (23.0, -7.0)
            p8 = (20.0, -10.0)
            p9 = (-20.0, -10.0)
            p10 = (-23.0, -7.0)
            p11 = (-23.0, 31.0)
            p12 = (-20.869, 34.069)
            p13 = (-17.046, 35.493)
            p14 = (-16.0, 37.0)
            p15 = (-16.0, 42.0)
            p16 = (-15.0, 43.0)

            RadiusArc(p1, p2, 1.0)
            Line(p2, p3)
            RadiusArc(p3, p4, -1.608)
            Line(p4, p5)
            RadiusArc(p5, p6, 3.275)
            Line(p6, p7)
            RadiusArc(p7, p8, 3.0)
            Line(p8, p9)
            RadiusArc(p9, p10, 3.0)
            Line(p10, p11)
            RadiusArc(p11, p12, 3.275)
            Line(p12, p13)
            RadiusArc(p13, p14, -1.608)
            Line(p14, p15)
            RadiusArc(p15, p16, 1.0)
            Line(p16, p1)
        make_face()
    extrude(amount=-1.65)

   # ---------------------------------------------------------
    # 2. 40 Additive Rectangular Bodies (XZ Plane)
    # ---------------------------------------------------------
    # Data Format: (x1, z1, x2, z2, y_start, y_end)
    rect_data_40 = [
        (13.0, 43.0, 3.0, 33.85, 7.15, 1.65),     # Rect 1
        (-3.0, 43.0, -13.0, 33.85, 7.15, 1.65),   # Rect 2
        (15.0, 40.8, 13.0, 38.8, 6.4, 1.65),      # Rect 3
        (3.0, 40.8, 1.0, 38.8, 6.4, 1.65),        # Rect 4
        (-1.0, 40.8, -3.0, 38.8, 6.4, 1.65),      # Rect 5
        (-13.0, 40.8, -15.0, 38.8, 6.4, 1.65),    # Rect 6
        (11.75, 33.85, 9.25, 28.45, 6.4, 1.65),   # Rect 7
        (6.75, 33.85, 4.25, 28.45, 6.4, 1.65),    # Rect 8
        (-4.25, 33.85, -6.75, 28.45, 6.4, 1.65),  # Rect 9
        (-9.25, 33.85, -11.75, 28.45, 6.4, 1.65), # Rect 10
        (17.5, 24.8, 12.5, 19.2, 2.65, 1.65),     # Rect 11
        (11.5, 24.8, 6.5, 19.2, 2.65, 1.65),      # Rect 12
        (5.5, 24.8, 0.5, 19.2, 2.65, 1.65),       # Rect 13
        (-0.5, 24.8, -5.5, 19.2, 2.65, 1.65),     # Rect 14
        (-6.5, 24.8, -11.5, 19.2, 2.65, 1.65),    # Rect 15
        (-12.5, 24.8, -17.5, 19.2, 2.65, 1.65),   # Rect 16
        (-18.0, 26.6, -19.7, 23.3, 3.45, 1.65),   # Rect 17
        (-18.0, 22.1, -19.7, 18.8, 3.45, 1.65),   # Rect 18
        (-18.0, 17.46, -19.7, 14.16, 3.45, 1.65), # Rect 19
        (-18.0, 12.9, -19.7, 9.6, 3.45, 1.65),    # Rect 20
        (-11.5, 9.9, -19.3, 2.5, 3.95, 1.65),     # Rect 21
        (-3.65, 9.78, -10.65, 2.78, 2.65, 1.65),  # Rect 22
        (-2.7, -5.0, -14.7, -10.0, 5.45, 1.65),   # Rect 23
        (11.9, 0.7, 4.7, -6.5, 2.25, 1.65),       # Rect 24
        (23.0, 5.8, 18.0, -3.2, 5.45, 1.65),      # Rect 25
        (18.35, 13.05, 16.65, 9.75, 3.45, 1.65),  # Rect 26
        (16.0, 12.25, 14.3, 8.95, 3.45, 1.65),    # Rect 27
        (18.35, 17.6, 16.65, 14.3, 3.45, 1.65),   # Rect 28
        (19.7, 22.1, 18.0, 18.8, 3.45, 1.65),     # Rect 29
        (19.7, 26.6, 18.0, 23.3, 3.45, 1.65),     # Rect 30
        (15.75, 17.8, 14.05, 14.4, 2.45, 1.65),   # Rect 31
        (11.05, 17.46, 9.35, 14.16, 3.45, 1.65),  # Rect 32
        (8.65, 17.46, 6.95, 14.16, 3.45, 1.65),   # Rect 33
        (5.05, 17.46, 3.35, 14.16, 3.45, 1.65),   # Rect 34
        (2.65, 17.46, 0.95, 14.16, 3.45, 1.65),   # Rect 35
        (-1.2, 16.95, -4.6, 15.25, 2.45, 1.65),   # Rect 36
        (-6.55, 17.9, -8.25, 14.5, 2.45, 1.65),   # Rect 37
        (-12.95, 17.46, -14.65, 14.16, 3.45, 1.65),# Rect 38
        (-15.415, 17.46, -17.115, 14.16, 3.45, 1.65),# Rect 39
        (-15.65, 12.9, -17.35, 9.9, 3.45, 1.65)   # Rect 40
    ]

    for x1, z1, x2, z2, ys, ye in rect_data_40:
        with BuildSketch(Plane.XZ.offset(ys)):
            with Locations((min(x1, x2), min(z1, z2))):
                Rectangle(abs(x2 - x1), abs(z2 - z1), align=(Align.MIN, Align.MIN))
        extrude(amount=(ye - ys))
    # ---------------------------------------------------------
    # 3. Subtractive Mounting Holes (XZ Plane)
    # ---------------------------------------------------------
    hole_centers = [(-20.0, 31.0), (-20.0, -7.0), (20.0, -7.0), (20.0, 31.0)]
    with BuildSketch(Plane.XZ.offset(1.65)):
        with Locations(hole_centers):
            Circle(radius=1.3) # Dia 2.60mm
    extrude(amount=-1.65, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 4. Subtractive Circular Features (XZ Plane)
    # ---------------------------------------------------------
    centers_150 = [(14.50, 28.20), (0.00, 28.20), (-14.50, 28.20)]
    with BuildSketch(Plane.XZ.offset(1.65)):
        with Locations(centers_150):
            Circle(radius=0.75) # Dia 1.50mm
    extrude(amount=-1.65, mode=Mode.SUBTRACT)

    centers_080 = [(-8.20, 27.00), (-2.90, 27.00), (9.60, 27.00)]
    with BuildSketch(Plane.XZ.offset(1.65)):
        with Locations(centers_080):
            Circle(radius=0.40) # Dia 0.80mm
    extrude(amount=-1.65, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 5. 4 Additional Additive Rectangular Bodies (XZ Plane)
    # ---------------------------------------------------------
    new_rect_data_4 = [
        (-13.0, 42.8, -3.0, 35.05, -6.2, 0.0),   # Rect 1
        (3.0, 42.8, 13.0, 35.05, -6.2, 0.0),    # Rect 2
        (-2.6, 10.9, 2.6, 5.1, -1.4, 0.0),      # Rect 3
    ]
    for x1, z1, x2, z2, ys, ye in new_rect_data_4:
        with BuildSketch(Plane.XZ.offset(ys)):
            with Locations((min(x1, x2), min(z1, z2))):
                Rectangle(abs(x2 - x1), abs(z2 - z1), align=(Align.MIN, Align.MIN))
        extrude(amount=(ye - ys))

    # ---------------------------------------------------------
    # 6. New Subtractive Rectangle (XZ Plane)
    # ---------------------------------------------------------
    # P1(-19, 0, 24), P2(19, 0, 18), Extrude to P3(y=0.05)
    with BuildSketch(Plane.XZ.offset(0.0)):
        with Locations((min(-19.0, 19.0), min(24.0, 18.0))):
            Rectangle(abs(19.0 - (-19.0)), abs(18.0 - 24.0), align=(Align.MIN, Align.MIN))
    extrude(amount=0.05, mode=Mode.SUBTRACT)
    
    # ---------------------------------------------------------
    # 7. Two Subtractive XY Profiles (XY Plane, Z: 43 to 34)
    # ---------------------------------------------------------
    # Y values in points negated
    with BuildSketch(Plane.XY.offset(43.0)):
        # Profile 1
        with BuildLine():
            Polyline([(-12.5, -2.15), (-3.5, -2.15), (-3.5, -6.65), (-12.146, -6.65), (-12.5, -6.296)], close=True)
        make_face()
        # Profile 2
        with BuildLine():
            Polyline([(3.5, -2.15), (12.5, -2.15), (12.5, -6.65), (3.854, -6.65), (3.5, -6.296)], close=True)
        make_face()
    extrude(amount=(34.0 - 43.0), mode=Mode.SUBTRACT)
    
    # ---------------------------------------------------------
    # 8. Two New Subtractive Profiles (XY Plane, Z: 42.8 to 35.8)
    # ---------------------------------------------------------
    # Y-coordinates flipped from prompt (negative -> positive)
    
    # Profile 1 (p1-p8)
    with BuildSketch(Plane.XY.offset(42.8)):
        with BuildLine():
            Polyline([
                (12.0, 4.95), (9.0, 4.95), (9.0, 5.7), (7.0, 5.7), 
                (7.0, 4.95), (4.0, 4.95), (4.0, 1.0), (12.0, 1.0)
            ], close=True)
        make_face()
    extrude(amount=(35.8 - 42.8), mode=Mode.SUBTRACT)

    # Profile 2 (p10-p17) - CORRECTED ORIENTATION
    with BuildSketch(Plane.XY.offset(42.8)):
        with BuildLine():
            Polyline([
                (-4.0, 4.95), (-7.0, 4.95), (-7.0, 5.7), (-9.0, 5.7), 
                (-9.0, 4.95), (-12.0, 4.95), (-12.0, 1.0), (-4.0, 1.0)
            ], close=True)
        make_face()
    extrude(amount=(35.8 - 42.8), mode=Mode.SUBTRACT)
if __name__ == "__main__":
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        part.part.export_step("20200729-moteus-controller-r43-mechanical.step")