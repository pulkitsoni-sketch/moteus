from build123d import *

# Part: SOP_Advance

with BuildPart() as part:
    # Loft from Z=0.0 to Z=0.95
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            Line((2.5, 2.5), (-2.5, 2.5))
            Line((-2.5, 2.5), (-2.5, -2.5))
            Line((-2.5, -2.5), (2.5, -2.5))
            Line((2.5, -2.5), (2.5, 2.5))
        make_face()

    with BuildSketch(Plane.XY.offset(0.95)):
        with BuildLine():
            Line((2.417, 2.417), (-2.417, 2.417))
            Line((-2.417, 2.417), (-2.417, -2.417))
            Line((-2.417, -2.417), (2.417, -2.417))
            Line((2.417, -2.417), (2.417, 2.417))
        make_face()

    loft()

    # 4 pad bodies, subtract+add
    pad_x_starts = [2.105, 0.835, -0.435, -1.705]
    for px in pad_x_starts:
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(Plane.XY.offset(0.0)):
                with BuildLine():
                    Line((px, -2.4), (px - 0.4, -2.4))
                    Line((px - 0.4, -2.4), (px - 0.4, -3.0))
                    Line((px - 0.4, -3.0), (px, -3.0))
                    Line((px, -3.0), (px, -2.4))
                make_face()
            extrude(amount=0.166, mode=mode)

    # 36-point profile at Z=0.0, extrude to Z=0.166, subtract+add
    for mode in [Mode.SUBTRACT, Mode.ADD]:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((2.65, 0.1), (2.325, 0.1))
                Line((2.325, 0.1), (2.325, 0.2))
                Line((2.325, 0.2), (2.125, 0.2))
                Line((2.125, 0.2), (2.125, 2.2))
                Line((2.125, 2.2), (2.105, 2.2))
                Line((2.105, 2.2), (2.105, 3.0))
                Line((2.105, 3.0), (1.705, 3.0))
                Line((1.705, 3.0), (1.705, 2.2))
                Line((1.705, 2.2), (0.835, 2.2))
                Line((0.835, 2.2), (0.835, 3.0))
                Line((0.835, 3.0), (0.435, 3.0))
                Line((0.435, 3.0), (0.435, 2.2))
                Line((0.435, 2.2), (-0.435, 2.2))
                Line((-0.435, 2.2), (-0.435, 3.0))
                Line((-0.435, 3.0), (-0.835, 3.0))
                Line((-0.835, 3.0), (-0.835, 2.2))
                Line((-0.835, 2.2), (-1.705, 2.2))
                Line((-1.705, 2.2), (-1.705, 3.0))
                Line((-1.705, 3.0), (-2.105, 3.0))
                Line((-2.105, 3.0), (-2.105, 2.2))
                Line((-2.105, 2.2), (-2.125, 2.2))
                Line((-2.125, 2.2), (-2.125, 0.2))
                Line((-2.125, 0.2), (-2.325, 0.2))
                Line((-2.325, 0.2), (-2.325, 0.1))
                Line((-2.325, 0.1), (-2.65, 0.1))
                Line((-2.65, 0.1), (-2.65, -0.1))
                Line((-2.65, -0.1), (-2.325, -0.1))
                Line((-2.325, -0.1), (-2.325, -0.2))
                Line((-2.325, -0.2), (-2.125, -0.2))
                Line((-2.125, -0.2), (-2.125, -1.3))
                Line((-2.125, -1.3), (2.125, -1.3))
                Line((2.125, -1.3), (2.125, -0.2))
                Line((2.125, -0.2), (2.325, -0.2))
                Line((2.325, -0.2), (2.325, -0.1))
                Line((2.325, -0.1), (2.65, -0.1))
                Line((2.65, -0.1), (2.65, 0.1))
            make_face()
        extrude(amount=0.166, mode=mode)

    # Circle at (-1.25, -1.25, 0.95), dia 1.25, extrude -0.1
    with BuildSketch(Plane.XY.offset(0.95)):
        with Locations([(-1.25, -1.25)]):
            Circle(radius=0.625)
    extrude(amount=-0.1, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_SOP_Advance.stl")