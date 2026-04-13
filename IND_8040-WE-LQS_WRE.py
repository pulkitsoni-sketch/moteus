from build123d import *

# Part: IND_8040-WE-LQS_WRE

with BuildPart() as part:
    # Rect at Z=0.051 (8.204 x 8.306), extrude up to Z=4.191
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((4.102, -4.153), (-4.102, -4.153))
            Line((-4.102, -4.153), (-4.102, 4.153))
            Line((-4.102, 4.153), (4.102, 4.153))
            Line((4.102, 4.153), (4.102, -4.153))
        make_face()
    extrude(amount=4.14)

    # +X side L-profile in XZ plane at Y=-3.75, extrude to Y=3.75
    sk1 = Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((4.102, 0.381), (4.153, 0.381))
            Line((4.153, 0.381), (4.153, 0.0))
            Line((4.153, 0.0), (1.9, 0.0))
            Line((1.9, 0.0), (1.9, 0.051))
            Line((1.9, 0.051), (4.102, 0.051))
            Line((4.102, 0.051), (4.102, 0.381))
        make_face()
    extrude(amount=-7.5)

    # -X side L-profile in XZ plane at Y=-3.75, extrude to Y=3.75
    with BuildSketch(sk1):
        with BuildLine():
            Line((-4.153, 0.381), (-4.102, 0.381))
            Line((-4.102, 0.381), (-4.102, 0.051))
            Line((-4.102, 0.051), (-1.9, 0.051))
            Line((-1.9, 0.051), (-1.9, 0.0))
            Line((-1.9, 0.0), (-4.153, 0.0))
            Line((-4.153, 0.0), (-4.153, 0.381))
        make_face()
    extrude(amount=-7.5)

    # Circle at (-3.282, 0.0, 4.191), dia 0.41, extrude +0.003 in Z
    with BuildSketch(Plane.XY.offset(4.191)):
        with Locations([(-3.282, 0.0)]):
            Circle(radius=0.41 / 2)
    extrude(amount=0.003)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_IND_8040-WE-LQS_WRE.stl")