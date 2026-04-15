from build123d import *

# Part: UFQFPN-48_7X7X0P55MM

with BuildPart() as part:
    # Rect at Z=0.051, extrude to Z=0.61
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((3.556, 3.556), (-3.556, 3.556))
            Line((-3.556, 3.556), (-3.556, -3.556))
            Line((-3.556, -3.556), (3.556, -3.556))
            Line((3.556, -3.556), (3.556, 3.556))
        make_face()
    extrude(amount=0.559)

    # Rect at Z=0.0, extrude to Z=0.051
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((2.845, 2.845), (-2.845, 2.845))
            Line((-2.845, 2.845), (-2.845, -2.845))
            Line((-2.845, -2.845), (2.845, -2.845))
            Line((2.845, -2.845), (2.845, 2.845))
        make_face()
    extrude(amount=0.051)

    # 48 pads at Z=0.0, extrude to Z=0.051
    # Top edge (Y=3.556): pads 0.304 wide x 0.508 tall, top-left corners
    top_pads = [2.902, 2.402, 1.902, 1.402, 0.902, 0.402, -0.098, -0.598, -1.098, -1.598, -2.098, -2.598]
    for px in top_pads:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((px, 3.556), (px - 0.304, 3.556))
                Line((px - 0.304, 3.556), (px - 0.304, 3.048))
                Line((px - 0.304, 3.048), (px, 3.048))
                Line((px, 3.048), (px, 3.556))
            make_face()
        extrude(amount=0.051)

    # Left edge (X=-3.556): pads 0.508 wide x 0.304 tall
    left_pads = [2.902, 2.402, 1.902, 1.402, 0.902, 0.402, -0.098, -0.598, -1.098, -1.598, -2.098, -2.598]
    for py in left_pads:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((-3.556, py), (-3.048, py))
                Line((-3.048, py), (-3.048, py - 0.304))
                Line((-3.048, py - 0.304), (-3.556, py - 0.304))
                Line((-3.556, py - 0.304), (-3.556, py))
            make_face()
        extrude(amount=0.051)

    # Bottom edge (Y=-3.556): pads 0.304 wide x 0.508 tall
    bot_pads = [-2.902, -2.402, -1.902, -1.402, -0.902, -0.402, 0.098, 0.598, 1.098, 1.598, 2.098, 2.598]
    for px in bot_pads:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((px, -3.556), (px + 0.304, -3.556))
                Line((px + 0.304, -3.556), (px + 0.304, -3.048))
                Line((px + 0.304, -3.048), (px, -3.048))
                Line((px, -3.048), (px, -3.556))
            make_face()
        extrude(amount=0.051)

    # Right edge (X=3.556): pads 0.508 wide x 0.304 tall
    right_pads = [-2.902, -2.402, -1.902, -1.402, -0.902, -0.402, 0.098, 0.598, 1.098, 1.598, 2.098, 2.598]
    for py in right_pads:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((3.556, py), (3.048, py))
                Line((3.048, py), (3.048, py + 0.304))
                Line((3.048, py + 0.304), (3.556, py + 0.304))
                Line((3.556, py + 0.304), (3.556, py))
            make_face()
        extrude(amount=0.051)

    # Circle at (-2.845, 2.75, 0.612), dia 0.356, extrude -0.002
    with BuildSketch(Plane.XY.offset(0.612)):
        with Locations([(-2.845, 2.75)]):
            Circle(radius=0.178)
    extrude(amount=-0.002)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_UFQFPN-48_7X7X0P55MM.stl")