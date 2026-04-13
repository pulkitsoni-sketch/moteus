from build123d import *

# Part: IND_DFE252012_MUR

with BuildPart() as part:
    # Profile 1: YZ plane at X=-1.346, extrude to X=-0.533 (amount=0.813)
    sk1 = Plane(origin=(-1.346, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((1.105, 0.0), (1.105, 1.194))
            Line((1.105, 1.194), (-1.105, 1.194))
            Line((-1.105, 1.194), (-1.105, 0.0))
            Line((-1.105, 0.0), (1.105, 0.0))
        make_face()
    extrude(amount=0.813)

    # Profile 2: YZ plane at X=0.533, extrude to X=1.346 (amount=0.813)
    sk2 = Plane(origin=(0.533, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk2):
        with BuildLine():
            Line((1.105, 0.0), (1.105, 1.194))
            Line((1.105, 1.194), (-1.105, 1.194))
            Line((-1.105, 1.194), (-1.105, 0.0))
            Line((-1.105, 0.0), (1.105, 0.0))
        make_face()
    extrude(amount=0.813)

    # Profile 3: YZ plane at X=-0.533, extrude to X=0.533 (amount=1.066)
    sk3 = Plane(origin=(-0.533, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((1.066, 0.038), (1.066, 1.155))
            Line((1.066, 1.155), (-1.066, 1.155))
            Line((-1.066, 1.155), (-1.066, 0.038))
            Line((-1.066, 0.038), (1.066, 0.038))
        make_face()
    extrude(amount=1.066)

    # Frame profile: YZ plane at X=-0.427, extrude to X=-0.32 (amount=0.107)
    # Outer rect minus inner rect (offset 0.003 inward)
    sk4 = Plane(origin=(-0.427, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk4):
        # Outer rect
        with BuildLine():
            Line((-1.069, 1.158), (-1.069, 0.036))
            Line((-1.069, 0.036), (1.069, 0.036))
            Line((1.069, 0.036), (1.069, 1.158))
            Line((1.069, 1.158), (-1.069, 1.158))
        make_face()
        # Inner rect (0.003 inward) - subtract
        with BuildLine(mode=Mode.SUBTRACT):
            Line((-1.066, 1.155), (-1.066, 0.039))
            Line((-1.066, 0.039), (1.066, 0.039))
            Line((1.066, 0.039), (1.066, 1.155))
            Line((1.066, 1.155), (-1.066, 1.155))
        make_face(mode=Mode.SUBTRACT)
    extrude(amount=0.107)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_IND_DFE252012_MUR.stl")