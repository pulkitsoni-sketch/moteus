from build123d import *

# Part: IND_4018-WE-LQS-_WRE

with BuildPart() as part:
    # Rect at Z=0.051 (3.81 x 4.192), extrude up to Z=1.803
    with BuildSketch(Plane.XY.offset(0.051)):
        with BuildLine():
            Line((1.905, 2.096), (-1.905, 2.096))
            Line((-1.905, 2.096), (-1.905, -2.096))
            Line((-1.905, -2.096), (1.905, -2.096))
            Line((1.905, -2.096), (1.905, 2.096))
        make_face()
    extrude(amount=1.752)

    # 6-point profile in XZ plane at Y=-1.8, extrude to Y=1.8 (amount=3.6)
    # Use x_dir=(1,0,0), z_dir=(0,-1,0) so sketch Y = world Z
    sk = Plane(origin=(0, -1.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk):
        with BuildLine():
            Line((1.905, 0.381), (1.956, 0.381))
            Line((1.956, 0.381), (1.956, 0.0))
            Line((1.956, 0.0), (0.775, 0.0))
            Line((0.775, 0.0), (0.775, 0.051))
            Line((0.775, 0.051), (1.905, 0.051))
            Line((1.905, 0.051), (1.905, 0.381))
        make_face()
    extrude(amount=-3.6)

    # 6-point profile in XZ plane at Y=-1.8 (-X side), extrude to Y=1.8
    sk2 = Plane(origin=(0, -1.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk2):
        with BuildLine():
            Line((-1.905, 0.381), (-1.905, 0.051))
            Line((-1.905, 0.051), (-0.775, 0.051))
            Line((-0.775, 0.051), (-0.775, 0.0))
            Line((-0.775, 0.0), (-1.956, 0.0))
            Line((-1.956, 0.0), (-1.956, 0.381))
            Line((-1.956, 0.381), (-1.905, 0.381))
        make_face()
    extrude(amount=-3.6)

    # Circle at (-1.524, 0.0, 1.803), dia 0.191, extrude -0.003 in Z
    with BuildSketch(Plane.XY.offset(1.803)):
        with Locations([(-1.524, 0.0)]):
            Circle(radius=0.191 / 2)
    extrude(amount=0.003)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_IND_4018-WE-LQS-_WRE.stl")