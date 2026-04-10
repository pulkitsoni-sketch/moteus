from build123d import *

# Part: 21-0664E_1233-1C_MXM
# Base Z = 0.051, Top Z = 0.813, Height = 0.762

with BuildPart() as part:
    # Feature 1: Main body rect
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, 1.524), (1.524, 1.524))
            Line((1.524, 1.524), (1.524, -1.524))
            Line((1.524, -1.524), (-1.524, -1.524))
            Line((-1.524, -1.524), (-1.524, 1.524))
        make_face()
    extrude(amount=0.762)

    # Feature 2: Rect extrude down from Z=0.051 to Z=0.0
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, 1.402), (-1.067, 1.402))
            Line((-1.067, 1.402), (-1.067, 1.098))
            Line((-1.067, 1.098), (-1.524, 1.098))
            Line((-1.524, 1.098), (-1.524, 1.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 2b: Left corner (-1.524, 0.902)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, 0.902), (-1.067, 0.902))
            Line((-1.067, 0.902), (-1.067, 0.598))
            Line((-1.067, 0.598), (-1.524, 0.598))
            Line((-1.524, 0.598), (-1.524, 0.902))
        make_face()
    extrude(amount=-0.051)

    # Feature 2c: Left corner (-1.524, 0.402)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, 0.402), (-1.067, 0.402))
            Line((-1.067, 0.402), (-1.067, 0.098))
            Line((-1.067, 0.098), (-1.524, 0.098))
            Line((-1.524, 0.098), (-1.524, 0.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 2d: Left corner (-1.524, -0.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, -0.098), (-1.067, -0.098))
            Line((-1.067, -0.098), (-1.067, -0.402))
            Line((-1.067, -0.402), (-1.524, -0.402))
            Line((-1.524, -0.402), (-1.524, -0.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2e: Left corner (-1.524, -0.598)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, -0.598), (-1.067, -0.598))
            Line((-1.067, -0.598), (-1.067, -0.902))
            Line((-1.067, -0.902), (-1.524, -0.902))
            Line((-1.524, -0.902), (-1.524, -0.598))
        make_face()
    extrude(amount=-0.051)

    # Feature 2f: Left corner (-1.524, -1.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-1.524, -1.098), (-1.067, -1.098))
            Line((-1.067, -1.098), (-1.067, -1.402))
            Line((-1.067, -1.402), (-1.524, -1.402))
            Line((-1.524, -1.402), (-1.524, -1.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2g: Left corner (1.067, -1.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, -1.098), (1.524, -1.098))
            Line((1.524, -1.098), (1.524, -1.402))
            Line((1.524, -1.402), (1.067, -1.402))
            Line((1.067, -1.402), (1.067, -1.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2h: Left corner (1.067, -0.598)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, -0.598), (1.524, -0.598))
            Line((1.524, -0.598), (1.524, -0.902))
            Line((1.524, -0.902), (1.067, -0.902))
            Line((1.067, -0.902), (1.067, -0.598))
        make_face()
    extrude(amount=-0.051)

    # Feature 2i: Left corner (1.067, -0.098)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, -0.098), (1.524, -0.098))
            Line((1.524, -0.098), (1.524, -0.402))
            Line((1.524, -0.402), (1.067, -0.402))
            Line((1.067, -0.402), (1.067, -0.098))
        make_face()
    extrude(amount=-0.051)

    # Feature 2j: Left corner (1.067, 0.402)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, 0.402), (1.524, 0.402))
            Line((1.524, 0.402), (1.524, 0.098))
            Line((1.524, 0.098), (1.067, 0.098))
            Line((1.067, 0.098), (1.067, 0.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 2k: Left corner (1.067, 0.902)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, 0.902), (1.524, 0.902))
            Line((1.524, 0.902), (1.524, 0.598))
            Line((1.524, 0.598), (1.067, 0.598))
            Line((1.067, 0.598), (1.067, 0.902))
        make_face()
    extrude(amount=-0.051)

    # Feature 2l: Left corner (1.067, 1.402)
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.067, 1.402), (1.524, 1.402))
            Line((1.524, 1.402), (1.524, 1.098))
            Line((1.524, 1.098), (1.067, 1.098))
            Line((1.067, 1.098), (1.067, 1.402))
        make_face()
    extrude(amount=-0.051)

    # Feature 3: Center rect from Z=0.051 down to Z=0.0
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-0.902, 1.295), (0.902, 1.295))
            Line((0.902, 1.295), (0.902, -1.295))
            Line((0.902, -1.295), (-0.902, -1.295))
            Line((-0.902, -1.295), (-0.902, 1.295))
        make_face()
    extrude(amount=-0.051)

    # Feature 4: Circle at (-1.219, 1.25, 0.815), dia 0.152, extrude -0.002 in Z
    with BuildSketch(Plane.XY.offset(0.815)):
        with Locations([(-1.219, 1.25)]):
            Circle(radius=0.152 / 2)
    extrude(amount=-0.002)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_21-0664E_1233-1C_MXM.stl")