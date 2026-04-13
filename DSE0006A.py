from build123d import *

# Part: DSE0006A

with BuildPart() as part:
    # Rect in XZ plane at Y=0.0 (1.5 x 1.5), extrude to Y=0.775
    sketch_plane = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sketch_plane):
        with BuildLine():
            Line((0.75, 0.75), (0.75, -0.75))
            Line((0.75, -0.75), (-0.75, -0.75))
            Line((-0.75, -0.75), (-0.75, 0.75))
            Line((-0.75, 0.75), (0.75, 0.75))
        make_face()
    extrude(amount=0.775)

    # 5 rect bodies in XZ plane, extrude from Y=0.102 to Y=-0.025 (amount=0.127)
    # Each body: 0.25 wide (X), 0.35 tall (Z)
    left_corners = [
        (-0.625, 0.75),   # P1: X=-0.625, Z=0.75
        (-0.125, 0.75),   # P2: X=-0.125, Z=0.75
        (0.375, 0.75),    # P3: X=0.375, Z=0.75
        (-0.625, -0.4),   # P4: X=-0.625, Z=-0.4
        (-0.125, -0.4),   # P5: X=-0.125, Z=-0.4
    ]

    for lx, lz in left_corners:
        sk = Plane(origin=(0, 0.102-0.08, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk):
            with BuildLine():
                Line((lx, lz), (lx, lz - 0.35))
                Line((lx, lz - 0.35), (lx + 0.25, lz - 0.35))
                Line((lx + 0.25, lz - 0.35), (lx + 0.25, lz))
                Line((lx + 0.25, lz), (lx, lz))
            make_face()
        extrude(amount=0.127, mode=Mode.SUBTRACT)

        with BuildSketch(sk):
            with BuildLine():
                Line((lx, lz), (lx, lz - 0.35))
                Line((lx, lz - 0.35), (lx + 0.25, lz - 0.35))
                Line((lx + 0.25, lz - 0.35), (lx + 0.25, lz))
                Line((lx + 0.25, lz), (lx, lz))
            make_face()
        extrude(amount=0.127)

    # 5-point profile in XZ plane at Y=0.102, subtract then add
    sk3 = Plane(origin=(0, 0.102-0.08, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((0.375, -0.3), (0.375, -0.75))
            Line((0.375, -0.75), (0.625, -0.75))
            Line((0.625, -0.75), (0.625, -0.4))
            Line((0.625, -0.4), (0.525, -0.3))
            Line((0.525, -0.3), (0.375, -0.3))
        make_face()
    extrude(amount=0.127, mode=Mode.SUBTRACT)

    with BuildSketch(sk3):
        with BuildLine():
            Line((0.375, -0.3), (0.375, -0.75))
            Line((0.375, -0.75), (0.625, -0.75))
            Line((0.625, -0.75), (0.625, -0.4))
            Line((0.625, -0.4), (0.525, -0.3))
            Line((0.525, -0.3), (0.375, -0.3))
        make_face()
    extrude(amount=0.127)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_DSE0006A.stl")
