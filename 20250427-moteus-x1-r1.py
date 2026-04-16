from build123d import *

# Part: 20250427-moteus-x1-r1

with BuildPart() as part:
    # ---------------------------------------------------------
    # Main Body
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(1.55)):
        with BuildLine():
            Line((28.0, 25.0), (28.0, -25.0))
            ThreePointArc((28.0, -25.0), (27.121, -27.121), (25.0, -28.0))
            Line((25.0, -28.0), (-25.0, -28.0))
            ThreePointArc((-25.0, -28.0), (-27.121, -27.121), (-28.0, -25.0))
            Line((-28.0, -25.0), (-28.0, 25.0))
            ThreePointArc((-28.0, 25.0), (-27.121, 27.121), (-25.0, 28.0))
            Line((-25.0, 28.0), (25.0, 28.0))
            ThreePointArc((25.0, 28.0), (27.121, 27.121), (28.0, 25.0))
        make_face()
    extrude(amount=-1.55)

    # ---------------------------------------------------------
    # 4 Corner Subtracted Holes (Dia 3.0mm)
    # ---------------------------------------------------------
    corner_centers = [
        (25.0, 25.0),
        (25.0, -25.0),
        (-25.0, -25.0),
        (-25.0, 25.0)
    ]
    
    for cx, cy in corner_centers:
        with BuildSketch(Plane.XY.offset(1.55)):
            with BuildLine():
                ThreePointArc((cx + 1.5, cy), (cx, cy + 1.5), (cx - 1.5, cy))
                ThreePointArc((cx - 1.5, cy), (cx, cy - 1.5), (cx + 1.5, cy))
            make_face()
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 5 Top Subtracted Holes (Dia 2.0mm)
    # ---------------------------------------------------------
    top_centers = [
        (-10.16, 25.20),
        (-5.08, 25.20),
        (0.00, 25.20),
        (5.08, 25.20),
        (10.16, 25.20)
    ]
    
    for cx, cy in top_centers:
        with BuildSketch(Plane.XY.offset(1.55)):
            with BuildLine():
                ThreePointArc((cx + 1.0, cy), (cx, cy + 1.0), (cx - 1.0, cy))
                ThreePointArc((cx - 1.0, cy), (cx, cy - 1.0), (cx + 1.0, cy))
            make_face()
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 26 Array Subtracted Holes (Dia 0.9mm)
    # ---------------------------------------------------------
    array_centers = [
        (16.51, 26.47), (16.51, 23.93),
        (11.43, 26.47), (11.43, 23.93),
        (8.89, 26.47),  (8.89, 23.93),
        (6.35, 26.47),  (6.35, 23.93),
        (3.81, 26.47),  (3.81, 23.93),
        (1.27, 26.47),  (1.27, 23.93),
        (-1.27, 26.47), (-1.27, 23.93),
        (-3.81, 26.47), (-3.81, 23.93),
        (-6.35, 26.47), (-6.35, 23.93),
        (-8.89, 26.47), (-8.89, 23.93),
        (-11.43, 26.47), (-11.43, 23.93),
        (-16.51, 26.47), (-16.51, 23.93),
        (-19.05, 26.47), (-19.05, 23.93)
    ]
    
    for cx, cy in array_centers:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                ThreePointArc((cx + 0.45, cy), (cx, cy + 0.45), (cx - 0.45, cy))
                ThreePointArc((cx - 0.45, cy), (cx, cy - 0.45), (cx + 0.45, cy))
            make_face()
        extrude(amount=1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 5 Bottom Subtracted Holes (Dia 0.8mm)
    # ---------------------------------------------------------
    bottom_centers = [
        (-5.10, -14.40),
        (-5.10, -16.40),
        (-1.10, -16.40),
        (0.90, -16.40),
        (2.90, -16.40)
    ]
    
    for cx, cy in bottom_centers:
        with BuildSketch(Plane.XY.offset(1.55)):
            with BuildLine():
                ThreePointArc((cx + 0.40, cy), (cx, cy + 0.40), (cx - 0.40, cy))
                ThreePointArc((cx - 0.40, cy), (cx, cy - 0.40), (cx + 0.40, cy))
            make_face()
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 12 Side Subtracted Holes (Dia 0.65mm)
    # ---------------------------------------------------------
    side_centers = [
        (18.73, 0.20), (20.00, 0.20),
        (18.73, -1.07), (20.00, -1.07),
        (18.73, -2.34), (20.00, -2.34),
        (18.73, -3.61), (20.00, -3.61),
        (20.00, -9.69),
        (20.00, -10.96),
        (20.00, -12.23),
        (20.00, -13.50)
    ]

    for cx, cy in side_centers:
        with BuildSketch(Plane.XY.offset(1.55)):
            with BuildLine():
                ThreePointArc((cx + 0.325, cy), (cx, cy + 0.325), (cx - 0.325, cy))
                ThreePointArc((cx - 0.325, cy), (cx, cy - 0.325), (cx + 0.325, cy))
            make_face()
        extrude(amount=-1.55, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 6 Top Rectangular Bodies (Additive)
    # ---------------------------------------------------------
    rect_top_lefts = [
        (-26.75, 19.4),
        (-17.65, 19.4),
        (-8.55, 19.4),
        (0.55, 19.4),
        (9.65, 19.4),
        (18.75, 19.4)
    ]

    for tx, ty in rect_top_lefts:
        with BuildSketch(Plane.XY.offset(2.45)):
            with BuildLine():
                Line((tx, ty), (tx + 8.0, ty))
                Line((tx + 8.0, ty), (tx + 8.0, ty - 8.0))
                Line((tx + 8.0, ty - 8.0), (tx, ty - 8.0))
                Line((tx, ty - 8.0), (tx, ty))
            make_face()
        extrude(amount=-0.9)

    # ---------------------------------------------------------
    # 3 Rectangular Bodies (Additive)
    # ---------------------------------------------------------
    rect3_top_lefts = [
        (-26.85, 9.6),
        (1.8, 9.6),
        (9.5, 9.6)
    ]

    for tx, ty in rect3_top_lefts:
        with BuildSketch(Plane.XY.offset(2.75)):
            with BuildLine():
                Line((tx, ty), (tx + 6.8, ty))
                Line((tx + 6.8, ty), (tx + 6.8, ty - 3.2))
                Line((tx + 6.8, ty - 3.2), (tx, ty - 3.2))
                Line((tx, ty - 3.2), (tx, ty))
            make_face()
        extrude(amount=-1.2)

    # ---------------------------------------------------------
    # 8 Custom Rectangular Bodies (Additive)
    # ---------------------------------------------------------
    custom_rects = [
        (-28.0, 4.7, -22.86, -7.3, 5.35, 1.55 - 5.35),
        (-28.0, -9.05, -23.37, -19.55, 5.95, 1.55 - 5.95),
        (-16.62, -4.661, -7.92, -11.361, 3.25, 1.55 - 3.25),
        (-16.7, -14.0, -6.7, -28.0, 6.65, 1.55 - 6.65),
        (-4.2, -20.15, 5.8, -28.0, 7.15, 1.55 - 7.15),
        (6.6, -20.15, 16.6, -28.0, 7.15, 1.55 - 7.15),
        (23.37, -7.31, 28.0, -20.81, 5.95, 1.55 - 5.95),
        (23.37, 5.65, 28.0, -6.35, 5.95, 1.55 - 5.95)
    ]

    for x1, y1, x2, y2, z_start, ext_amt in custom_rects:
        with BuildSketch(Plane.XY.offset(z_start)):
            with BuildLine():
                Line((x1, y1), (x2, y1))
                Line((x2, y1), (x2, y2))
                Line((x2, y2), (x1, y2))
                Line((x1, y2), (x1, y1))
            make_face()
        extrude(amount=ext_amt)

    # ---------------------------------------------------------
    # 1 Custom Polygon Body (Additive) - Fixed
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(2.6)):
        with BuildLine():
            Line((6.6, 3.743), (10.843, -0.5))
            Line((10.843, -0.5), (6.6, -4.743))
            Line((6.6, -4.743), (2.357, -0.5))
            Line((2.357, -0.5), (6.6, 3.743))
        make_face()
    extrude(amount=(1.55 - 2.6))

    # ---------------------------------------------------------
    # 13 Bottom Rectangular Bodies (Additive)
    # ---------------------------------------------------------
    # Format: (p1_x, p1_y, p2_x, p2_y, start_z, extrude_amount)
    # Extrude up to Z=0.0 means amount = 0.0 - start_z = abs(start_z)
    bottom_rects = [
        (26.0, 19.6, 12.6, 16.0, -1.7, 1.7),
        (26.0, 14.4, 12.6, 10.8, -1.7, 1.7),
        (-11.5, 19.6, -24.9, 16.0, -1.7, 1.7),
        (4.6, 14.4, -24.9, 10.8, -1.7, 1.7),
        (-3.3, 9.9, -14.4, 6.3, -1.7, 1.7),
        (-18.05, 5.3, -23.65, 1.7, -2.4, 2.4),
        (-21.2, -1.3, -27.2, -7.3, -2.8, 2.8),
        (-16.9, -5.15, -20.1, -7.75, -2.6, 2.6),
        (-19.763, -11.23, -22.963, -13.83, -2.6, 2.6),
        (-18.1, -15.052, -20.7, -18.252, -2.6, 2.6),
        (-7.33, -17.95, -12.73, -20.85, -2.4, 2.4),
        (5.05, -20.3, -1.45, -25.3, -1.6, 1.6),
        (1.5, 1.5, -1.5, -1.5, -0.9, 0.9)
    ]

    for x1, y1, x2, y2, z_start, ext_amt in bottom_rects:
        with BuildSketch(Plane.XY.offset(z_start)):
            with BuildLine():
                Line((x1, y1), (x2, y1))
                Line((x2, y1), (x2, y2))
                Line((x2, y2), (x1, y2))
                Line((x1, y2), (x1, y1))
            make_face()
        extrude(amount=ext_amt)

if __name__ == "__main__":
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        part.part.export_step("20250427-moteus-x1-r1.step")