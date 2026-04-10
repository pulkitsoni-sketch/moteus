from build123d import *

# Part: 21-0487A_MXM
# Base Z = 0.051, Top Z = 0.813, Height = 0.762

with BuildPart() as part:
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.029, -1.029), (-1.029, -1.029))
            Line((-1.029, -1.029), (-1.029, 1.029))
            Line((-1.029, 1.029), (1.029, 1.029))
            Line((1.029, 1.029), (1.029, -1.029))
        make_face()
    extrude(amount=0.762)

    # Feature 2: Rect extrude down from Z=0.051 to Z=0.0
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.029, -0.902), (0.572, -0.902))
            Line((0.572, -0.902), (0.572, -0.598))
            Line((0.572, -0.598), (1.029, -0.598))
            Line((1.029, -0.598), (1.029, -0.902))
        make_face()
    extrude(amount=-0.051)

    # Feature 2b: Left corner (1.029, -0.402)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.029, -0.402), (0.572, -0.402))
            Line((0.572, -0.402), (0.572, -0.098))
            Line((0.572, -0.098), (1.029, -0.098))
            Line((1.029, -0.098), (1.029, -0.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 2c: Left corner (1.029, 0.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.029, 0.098), (0.572, 0.098))
            Line((0.572, 0.098), (0.572, 0.402))
            Line((0.572, 0.402), (1.029, 0.402))
            Line((1.029, 0.402), (1.029, 0.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2d: Left corner (1.029, 0.598)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.029, 0.598), (0.572, 0.598))
            Line((0.572, 0.598), (0.572, 0.902))
            Line((0.572, 0.902), (1.029, 0.902))
            Line((1.029, 0.902), (1.029, 0.598))
        make_face()
    extrude(amount=-0.051)

    # Feature 2e: Left corner (-0.572, 0.598)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-0.572, 0.598), (-1.029, 0.598))
            Line((-1.029, 0.598), (-1.029, 0.902))
            Line((-1.029, 0.902), (-0.572, 0.902))
            Line((-0.572, 0.902), (-0.572, 0.598))
        make_face()
    extrude(amount=-0.051)

    # Feature 2f: Left corner (-0.572, 0.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-0.572, 0.098), (-1.029, 0.098))
            Line((-1.029, 0.098), (-1.029, 0.402))
            Line((-1.029, 0.402), (-0.572, 0.402))
            Line((-0.572, 0.402), (-0.572, 0.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2g: Left corner (-0.572, -0.402)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-0.572, -0.402), (-1.029, -0.402))
            Line((-1.029, -0.402), (-1.029, -0.098))
            Line((-1.029, -0.098), (-0.572, -0.098))
            Line((-0.572, -0.098), (-0.572, -0.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 2h: Left corner (-0.572, -0.902)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-0.572, -0.902), (-1.029, -0.902))
            Line((-1.029, -0.902), (-1.029, -0.598))
            Line((-1.029, -0.598), (-0.572, -0.598))
            Line((-0.572, -0.598), (-0.572, -0.902))
        make_face()
    extrude(amount=-0.051)

    # Feature 3: Circle at (-0.823, 0.75, 0.815), dia 0.103, extrude -0.002 in Z
    with BuildSketch(Plane.XY.offset(0.815)):
        with Locations([(-0.823, 0.75)]):
            Circle(radius=0.103 / 2)
    extrude(amount=-0.002)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_21-0487A_MXM.stl")