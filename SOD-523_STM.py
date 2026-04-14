from build123d import *

# Part: SOD-523_STM

with BuildPart() as part:
    # Rect at Z=0.051, extrude to Z=0.234
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((0.648, 0.444), (-0.648, 0.444))
            Line((-0.648, 0.444), (-0.648, -0.444))
            Line((-0.648, -0.444), (0.648, -0.444))
            Line((0.648, -0.444), (0.648, 0.444))
        make_face()
    extrude(amount=0.183)

    # Loft from Z=0.234 to Z=0.711
    with BuildSketch(Plane.XY.offset(0.234)):
        with BuildLine():
            Line((0.648, 0.444), (-0.648, 0.444))
            Line((-0.648, 0.444), (-0.648, -0.444))
            Line((-0.648, -0.444), (0.648, -0.444))
            Line((0.648, -0.444), (0.648, 0.444))
        make_face()

    with BuildSketch(Plane.XY.offset(0.711)):
        with BuildLine():
            Line((0.566, 0.362), (-0.566, 0.362))
            Line((-0.566, 0.362), (-0.566, -0.362))
            Line((-0.566, -0.362), (0.566, -0.362))
            Line((0.566, -0.362), (0.566, 0.362))
        make_face()

    loft()

    # 6-point profile in XZ plane at Y=0.178, extrude to Y=-0.178, and mirror
    sk1 = Plane(origin=(0, 0.178, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((0.394, 0.0), (0.851, 0.0))
            Line((0.851, 0.0), (0.851, 0.152))
            Line((0.851, 0.152), (0.648, 0.152))
            Line((0.648, 0.152), (0.648, 0.051))
            Line((0.648, 0.051), (0.394, 0.051))
            Line((0.394, 0.051), (0.394, 0.0))
        make_face()
    extrude(amount=0.356)

    # Mirror: -X side
    with BuildSketch(sk1):
        with BuildLine():
            Line((-0.394, 0.0), (-0.851, 0.0))
            Line((-0.851, 0.0), (-0.851, 0.152))
            Line((-0.851, 0.152), (-0.648, 0.152))
            Line((-0.648, 0.152), (-0.648, 0.051))
            Line((-0.648, 0.051), (-0.394, 0.051))
            Line((-0.394, 0.051), (-0.394, 0.0))
        make_face()
    extrude(amount=0.356)

    # Rect at Z=0.711, extrude to Z=0.718
    with BuildSketch(Plane.XY.offset(0.711)):
        with BuildLine():
            Line((0.385, 0.313), (0.502, 0.313))
            Line((0.502, 0.313), (0.502, -0.313))
            Line((0.502, -0.313), (0.385, -0.313))
            Line((0.385, -0.313), (0.385, 0.313))
        make_face()
    extrude(amount=0.007)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_SOD-523_STM.stl")