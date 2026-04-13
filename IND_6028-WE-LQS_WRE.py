from build123d import *

# Part: IND_6028-WE-LQS_WRE

with BuildPart() as part:
    # Rect at Z=0.051 (6.198 x 6.3), extrude up to Z=2.794
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((-3.099, 3.15), (3.099, 3.15))
            Line((3.099, 3.15), (3.099, -3.15))
            Line((3.099, -3.15), (-3.099, -3.15))
            Line((-3.099, -3.15), (-3.099, 3.15))
        make_face()
    extrude(amount=2.743)

    # -X side L-profile in XZ plane at Y=2.85, extrude to Y=-2.85
    sk1 = Plane(origin=(0, 2.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((-3.099, 0.381), (-3.15, 0.381))
            Line((-3.15, 0.381), (-3.15, 0.0))
            Line((-3.15, 0.0), (-1.4, 0.0))
            Line((-1.4, 0.0), (-1.4, 0.051))
            Line((-1.4, 0.051), (-3.099, 0.051))
            Line((-3.099, 0.051), (-3.099, 0.381))
        make_face()
    extrude(amount=5.7)

    # +X side L-profile in XZ plane at Y=2.85, extrude to Y=-2.85
    with BuildSketch(sk1):
        with BuildLine():
            Line((3.15, 0.381), (3.099, 0.381))
            Line((3.099, 0.381), (3.099, 0.051))
            Line((3.099, 0.051), (1.4, 0.051))
            Line((1.4, 0.051), (1.4, 0.0))
            Line((1.4, 0.0), (3.15, 0.0))
            Line((3.15, 0.0), (3.15, 0.381))
        make_face()
    extrude(amount=5.7)

    # Circle at (-2.479, 0.0, 2.794), dia 0.31, extrude 0.003 in Z
    with BuildSketch(Plane.XY.offset(2.794)):
        with Locations([(-2.479, 0.0)]):
            Circle(radius=0.31 / 2)
    extrude(amount=0.003)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_IND_6028-WE-LQS_WRE.stl")