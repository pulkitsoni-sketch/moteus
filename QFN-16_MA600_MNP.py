from build123d import *

# Part: QFN-16_MA600_MNP

with BuildPart() as part:
    # Rect at Z=0.051 (3.098 x 3.098), extrude up to Z=0.94
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.549, 1.549), (-1.549, 1.549))
            Line((-1.549, 1.549), (-1.549, -1.549))
            Line((-1.549, -1.549), (1.549, -1.549))
            Line((1.549, -1.549), (1.549, 1.549))
        make_face()
    extrude(amount=0.889)

    # Rect at Z=0.0 (1.7 x 1.7), extrude up to Z=0.051
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((0.85, 0.85), (0.85, -0.85))
            Line((0.85, -0.85), (-0.85, -0.85))
            Line((-0.85, -0.85), (-0.85, 0.85))
            Line((-0.85, 0.85), (0.85, 0.85))
        make_face()
    extrude(amount=0.051)

    # 8 cuboids (0.457 x 0.304) at Z=0.0, extrude up 0.051
    # +X side: X from 1.549 to 1.092
    # -X side: X from -1.092 to -1.549
    left_corners = [
        (1.549, -0.902),   # P1
        (1.549, -0.402),   # P2
        (1.549, 0.098),    # P3
        (1.549, 0.598),    # P4
        (-1.092, 0.598),   # P5
        (-1.092, 0.098),   # P6
        (-1.092, -0.402),  # P7
        (-1.092, -0.902),  # P8
    ]

    for lx, ly in left_corners:
        if lx > 0:
            # +X side: X goes from lx to lx - 0.457
            x1, x2 = lx, lx - 0.457
        else:
            # -X side: X goes from lx to lx - 0.457
            x1, x2 = lx, lx - 0.457
        y1, y2 = ly, ly + 0.304
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((x1, y1), (x2, y1))
                Line((x2, y1), (x2, y2))
                Line((x2, y2), (x1, y2))
                Line((x1, y2), (x1, y1))
            make_face()
        extrude(amount=0.051)

    # 8 cuboids (0.304 x 0.457) at Z=0.0, extrude up 0.051
    # -Y side: Y from -1.549 to -1.092
    # +Y side: Y from 1.092 to 1.549
    left_corners_2 = [
        (0.902, -1.549),   # P1
        (0.402, -1.549),   # P2
        (-0.098, -1.549),  # P3
        (-0.598, -1.549),  # P4
        (0.902, 1.092),    # P5
        (0.402, 1.092),    # P6
        (-0.098, 1.092),   # P7
        (-0.598, 1.092),   # P8
    ]

    for lx, ly in left_corners_2:
        x1, x2 = lx, lx - 0.304
        if ly < 0:
            # -Y side: Y from ly to ly + 0.457
            y1, y2 = ly, ly + 0.457
        else:
            # +Y side: Y from ly to ly + 0.457
            y1, y2 = ly, ly + 0.457
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((x1, y1), (x2, y1))
                Line((x2, y1), (x2, y2))
                Line((x2, y2), (x1, y2))
                Line((x1, y2), (x1, y1))
            make_face()
        extrude(amount=0.051)

    # Circle at (-1.24, 0.75, 0.94), dia 0.155, extrude +0.002 in Z
    with BuildSketch(Plane.XY.offset(0.94)):
        with Locations([(-1.24, 0.75)]):
            Circle(radius=0.155 / 2)
    extrude(amount=0.002)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_QFN-16_MA600_MNP.stl")