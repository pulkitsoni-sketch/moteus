from build123d import *

# Part: SM08B-GHS-TB

with BuildPart() as part:
    # Rect at Z=-1.625, extrude down to Z=2.425
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((6.625, 4.25), (-6.625, 4.25))
            Line((-6.625, 4.25), (-6.625, 0.18))
            Line((-6.625, 0.18), (6.625, 0.18))
            Line((6.625, 0.18), (6.625, 4.25))
        make_face()
    extrude(amount=-4.05)

    # 6-point profile in YZ plane at X=6.625, extrude to X=-6.625
    sk1 = Plane(origin=(6.625, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((1.03, -1.625), (1.03, -1.065))
            Line((1.03, -1.065), (0.34, -1.065))
            Line((0.34, -1.065), (0.34, -0.915))
            Line((0.34, -0.915), (0.18, -0.915))
            Line((0.18, -0.915), (0.18, -1.625))
            Line((0.18, -1.625), (1.03, -1.625))
        make_face()
    extrude(amount=-13.25, mode=Mode.SUBTRACT)

    # Rect in YZ plane at X=6.625, extrude to X=6.515, and mirror
    for x_orig, amt in [(6.625, -0.11), (-6.625, 0.11)]:
        sk2 = Plane(origin=(x_orig, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk2):
            with BuildLine():
                Line((3.4, 2.425), (3.4, 0.465))
                Line((3.4, 0.465), (2.4, 0.465))
                Line((2.4, 0.465), (2.4, 2.425))
                Line((2.4, 2.425), (3.4, 2.425))
            make_face()
        extrude(amount=amt, mode=Mode.SUBTRACT)

    # Rect at Z=-1.625, extrude to Z=-0.825, and mirror
    with BuildSketch(Plane.XY.offset(-1.625)):
        with BuildLine():
            Line((5.55, 3.82), (5.19, 3.82))
            Line((5.19, 3.82), (5.19, 3.24))
            Line((5.19, 3.24), (5.55, 3.24))
            Line((5.55, 3.24), (5.55, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # Mirror
    with BuildSketch(Plane.XY.offset(-1.625)):
        with BuildLine():
            Line((-5.55, 3.82), (-5.19, 3.82))
            Line((-5.19, 3.82), (-5.19, 3.24))
            Line((-5.19, 3.24), (-5.55, 3.24))
            Line((-5.55, 3.24), (-5.55, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # Rect at Z=-1.625, extrude to Z=-0.825 (no mirror)
    with BuildSketch(Plane.XY.offset(-1.625)):
        with BuildLine():
            Line((4.55, 3.82), (-4.55, 3.82))
            Line((-4.55, 3.82), (-4.55, 2.49))
            Line((-4.55, 2.49), (4.55, 2.49))
            Line((4.55, 2.49), (4.55, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # 5-point profile in XZ plane at Y=3.325, extrude to Y=3.965, and mirror
    sk3 = Plane(origin=(0, 3.325, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((5.1, 0.465), (5.675, 0.465))
            Line((5.675, 0.465), (6.25, 1.04))
            Line((6.25, 1.04), (6.25, 2.425))
            Line((6.25, 2.425), (5.1, 2.425))
            Line((5.1, 2.425), (5.1, 0.465))
        make_face()
    extrude(amount=-0.64, mode=Mode.SUBTRACT)

    # Mirror
    with BuildSketch(sk3):
        with BuildLine():
            Line((-5.1, 0.465), (-5.675, 0.465))
            Line((-5.675, 0.465), (-6.25, 1.04))
            Line((-6.25, 1.04), (-6.25, 2.425))
            Line((-6.25, 2.425), (-5.1, 2.425))
            Line((-5.1, 2.425), (-5.1, 0.465))
        make_face()
    extrude(amount=-0.64, mode=Mode.SUBTRACT)

    # 6-point profile in YZ plane at X=5.765, extrude to X=6.625
    sk4 = Plane(origin=(5.765, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk4):
        with BuildLine():
            Line((4.25, 0.495), (4.25, -1.625))
            Line((4.25, -1.625), (1.903, -1.625))
            Line((1.903, -1.625), (1.903, -1.325))
            Line((1.903, -1.325), (4.12, -1.325))
            Line((4.12, -1.325), (4.12, 0.495))
            Line((4.12, 0.495), (4.25, 0.495))
        make_face()
    extrude(amount=0.86, mode=Mode.SUBTRACT)

    # 8-point profile in YZ plane at X=6.125, extrude to X=6.625
    sk5 = Plane(origin=(6.125, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5):
        with BuildLine():
            Line((4.12, 0.495), (4.12, -1.325))
            Line((4.12, -1.325), (1.903, -1.325))
            Line((1.903, -1.325), (1.903, -0.935))
            Line((1.903, -0.935), (3.5, -0.935))
            Line((3.5, -0.935), (3.5, 0.465))
            Line((3.5, 0.465), (3.965, 0.465))
            Line((3.965, 0.465), (3.965, 0.495))
            Line((3.965, 0.495), (4.12, 0.495))
        make_face()
    extrude(amount=0.5, mode=Mode.SUBTRACT)

    # Rect in YZ plane at X=6.25, extrude to X=6.625
    sk6 = Plane(origin=(6.25, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6):
        with BuildLine():
            Line((3.965, 0.495), (3.965, 0.465))
            Line((3.965, 0.465), (3.5, 0.465))
            Line((3.5, 0.465), (3.5, 0.495))
            Line((3.5, 0.495), (3.965, 0.495))
        make_face()
    extrude(amount=0.375, mode=Mode.SUBTRACT)

    # Mirror: 6-point profile at X=-5.765
    sk4m = Plane(origin=(-5.765, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk4m):
        with BuildLine():
            Line((4.25, 0.495), (4.25, -1.625))
            Line((4.25, -1.625), (1.903, -1.625))
            Line((1.903, -1.625), (1.903, -1.325))
            Line((1.903, -1.325), (4.12, -1.325))
            Line((4.12, -1.325), (4.12, 0.495))
            Line((4.12, 0.495), (4.25, 0.495))
        make_face()
    extrude(amount=-0.86, mode=Mode.SUBTRACT)

    # Mirror: 8-point profile at X=-6.125
    sk5m = Plane(origin=(-6.125, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5m):
        with BuildLine():
            Line((4.12, 0.495), (4.12, -1.325))
            Line((4.12, -1.325), (1.903, -1.325))
            Line((1.903, -1.325), (1.903, -0.935))
            Line((1.903, -0.935), (3.5, -0.935))
            Line((3.5, -0.935), (3.5, 0.465))
            Line((3.5, 0.465), (3.965, 0.465))
            Line((3.965, 0.465), (3.965, 0.495))
            Line((3.965, 0.495), (4.12, 0.495))
        make_face()
    extrude(amount=-0.5, mode=Mode.SUBTRACT)

    # Mirror: Rect at X=-6.25
    sk6m = Plane(origin=(-6.25, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6m):
        with BuildLine():
            Line((3.965, 0.495), (3.965, 0.465))
            Line((3.965, 0.465), (3.5, 0.465))
            Line((3.5, 0.465), (3.5, 0.495))
            Line((3.5, 0.495), (3.965, 0.495))
        make_face()
    extrude(amount=-0.375, mode=Mode.SUBTRACT)

    # 8-point profile at Z=0.125, extrude to Z=2.425
    with BuildSketch(Plane.XY.offset(0.125)):
        with BuildLine():
            Line((5.725, 0.18), (6.025, 0.48))
            Line((6.025, 0.48), (6.125, 0.48))
            Line((6.125, 0.48), (6.125, 2.21))
            Line((6.125, 2.21), (6.355, 2.21))
            Line((6.355, 2.21), (6.355, 0.78))
            Line((6.355, 0.78), (6.625, 0.78))
            Line((6.625, 0.78), (6.625, 0.18))
            Line((6.625, 0.18), (5.725, 0.18))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Rect at Z=1.725, extrude to Z=2.425
    with BuildSketch(Plane.XY.offset(1.725)):
        with BuildLine():
            Line((6.625, 2.21), (6.355, 2.21))
            Line((6.355, 2.21), (6.355, 0.78))
            Line((6.355, 0.78), (6.625, 0.78))
            Line((6.625, 0.78), (6.625, 2.21))
        make_face()
    extrude(amount=0.7, mode=Mode.SUBTRACT)

    # Profile 1: YZ plane at X=6.355, extrude to X=6.475
    sk7 = Plane(origin=(6.355, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk7):
        with BuildLine():
            Line((0.78, 0.075), (0.53, 0.075))
            Line((0.53, 0.075), (0.48, 0.125))
            Line((0.48, 0.125), (0.78, 0.125))
            Line((0.78, 0.125), (0.78, 0.075))
        make_face()
    extrude(amount=0.12, mode=Mode.SUBTRACT)

    # Profile 2: YZ plane at X=6.475, extrude to X=6.355
    sk8 = Plane(origin=(6.475, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk8):
        with BuildLine():
            Line((2.21, 1.675), (1.76, 1.675))
            Line((1.76, 1.675), (1.71, 1.725))
            Line((1.71, 1.725), (2.21, 1.725))
            Line((2.21, 1.725), (2.21, 1.675))
        make_face()
    extrude(amount=-0.12, mode=Mode.SUBTRACT)

    # Loft between two rects in subtract mode
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((6.075, 2.26), (6.625, 2.26))
            Line((6.625, 2.26), (6.625, 0.48))
            Line((6.625, 0.48), (6.075, 0.48))
            Line((6.075, 0.48), (6.075, 2.26))
        make_face()

    with BuildSketch(Plane.XY.offset(2.375)):
        with BuildLine():
            Line((6.125, 2.21), (6.625, 2.21))
            Line((6.625, 2.21), (6.625, 0.48))
            Line((6.625, 0.48), (6.125, 0.48))
            Line((6.125, 0.48), (6.125, 2.21))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # Mirror: 8-point profile at Z=0.125 (-X side)
    with BuildSketch(Plane.XY.offset(0.125)):
        with BuildLine():
            Line((-5.725, 0.18), (-6.025, 0.48))
            Line((-6.025, 0.48), (-6.125, 0.48))
            Line((-6.125, 0.48), (-6.125, 2.21))
            Line((-6.125, 2.21), (-6.355, 2.21))
            Line((-6.355, 2.21), (-6.355, 0.78))
            Line((-6.355, 0.78), (-6.625, 0.78))
            Line((-6.625, 0.78), (-6.625, 0.18))
            Line((-6.625, 0.18), (-5.725, 0.18))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Mirror: Rect at Z=1.725 (-X side)
    with BuildSketch(Plane.XY.offset(1.725)):
        with BuildLine():
            Line((-6.625, 2.21), (-6.355, 2.21))
            Line((-6.355, 2.21), (-6.355, 0.78))
            Line((-6.355, 0.78), (-6.625, 0.78))
            Line((-6.625, 0.78), (-6.625, 2.21))
        make_face()
    extrude(amount=0.7, mode=Mode.SUBTRACT)

    # Mirror: Profile 1 at X=-6.355, extrude to X=-6.475
    sk7m = Plane(origin=(-6.355, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk7m):
        with BuildLine():
            Line((0.78, 0.075), (0.53, 0.075))
            Line((0.53, 0.075), (0.48, 0.125))
            Line((0.48, 0.125), (0.78, 0.125))
            Line((0.78, 0.125), (0.78, 0.075))
        make_face()
    extrude(amount=-0.12, mode=Mode.SUBTRACT)

    # Mirror: Profile 2 at X=-6.475, extrude to X=-6.355
    sk8m = Plane(origin=(-6.475, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk8m):
        with BuildLine():
            Line((2.21, 1.675), (1.76, 1.675))
            Line((1.76, 1.675), (1.71, 1.725))
            Line((1.71, 1.725), (2.21, 1.725))
            Line((2.21, 1.725), (2.21, 1.675))
        make_face()
    extrude(amount=0.12, mode=Mode.SUBTRACT)

    # Mirror: Loft (-X side)
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((-6.075, 2.26), (-6.625, 2.26))
            Line((-6.625, 2.26), (-6.625, 0.48))
            Line((-6.625, 0.48), (-6.075, 0.48))
            Line((-6.075, 0.48), (-6.075, 2.26))
        make_face()

    with BuildSketch(Plane.XY.offset(2.375)):
        with BuildLine():
            Line((-6.125, 2.21), (-6.625, 2.21))
            Line((-6.625, 2.21), (-6.625, 0.48))
            Line((-6.625, 0.48), (-6.125, 0.48))
            Line((-6.125, 0.48), (-6.125, 2.21))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # Triangle at Y=4.25, extrude to Y=4.19
    sk9 = Plane(origin=(0, 4.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk9):
        with BuildLine():
            Line((-6.325, 2.425), (-5.938, 1.755))
            Line((-5.938, 1.755), (-5.551, 2.425))
            Line((-5.551, 2.425), (-6.325, 2.425))
        make_face()
    extrude(amount=0.06, mode=Mode.SUBTRACT)

    # 44-point comb profile at Z=2.225, extrude to Z=0.465
    with BuildSketch(Plane.XY.offset(2.225)):
        with BuildLine():
            Line((-5.114, 2.76), (-5.114, 2.255))
            Line((-5.114, 2.255), (-4.687, 2.255))
            Line((-4.687, 2.255), (-4.687, 1.855))
            Line((-4.687, 1.855), (-4.062, 1.855))
            Line((-4.062, 1.855), (-4.062, 2.76))
            Line((-4.062, 2.76), (-3.75, 2.76))
            Line((-3.75, 2.76), (-3.75, 2.255))
            Line((-3.75, 2.255), (-3.437, 2.255))
            Line((-3.437, 2.255), (-3.437, 1.855))
            Line((-3.437, 1.855), (-2.812, 1.855))
            Line((-2.812, 1.855), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.187, 2.255))
            Line((-2.187, 2.255), (-2.187, 1.855))
            Line((-2.187, 1.855), (-1.562, 1.855))
            Line((-1.562, 1.855), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.937, 2.255))
            Line((-0.937, 2.255), (-0.937, 1.855))
            Line((-0.937, 1.855), (-0.312, 1.855))
            Line((-0.312, 1.855), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 1.855))
            Line((0.313, 1.855), (0.938, 1.855))
            Line((0.938, 1.855), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 1.855))
            Line((1.562, 1.855), (2.187, 1.855))
            Line((2.187, 1.855), (2.187, 2.255))
            Line((2.187, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 1.855))
            Line((2.812, 1.855), (3.438, 1.855))
            Line((3.438, 1.855), (3.438, 2.255))
            Line((3.438, 2.255), (3.75, 2.255))
            Line((3.75, 2.255), (3.75, 2.76))
            Line((3.75, 2.76), (4.062, 2.76))
            Line((4.062, 2.76), (4.062, 1.855))
            Line((4.062, 1.855), (4.688, 1.855))
            Line((4.688, 1.855), (4.688, 2.255))
            Line((4.688, 2.255), (5.114, 2.255))
            Line((5.114, 2.255), (5.114, 2.76))
            Line((5.114, 2.76), (5.54, 2.76))
            Line((5.54, 2.76), (5.54, 0.78))
            Line((5.54, 0.78), (-5.54, 0.78))
            Line((-5.54, 0.78), (-5.54, 2.76))
            Line((-5.54, 2.76), (-5.114, 2.76))
        make_face()
    extrude(amount=-1.76, mode=Mode.SUBTRACT)

    # Comb loft: outer at Z=2.425, inner at Z=2.225
    with BuildSketch(Plane.XY.offset(2.425)):
        with BuildLine():
            Line((-4.914, 2.96), (-4.914, 2.255))
            Line((-4.914, 2.255), (-4.687, 2.255))
            Line((-4.687, 2.255), (-4.687, 2.055))
            Line((-4.687, 2.055), (-4.062, 2.055))
            Line((-4.062, 2.055), (-4.062, 2.76))
            Line((-4.062, 2.76), (-3.75, 2.76))
            Line((-3.75, 2.76), (-3.75, 2.255))
            Line((-3.75, 2.255), (-3.437, 2.255))
            Line((-3.437, 2.255), (-3.437, 2.055))
            Line((-3.437, 2.055), (-2.812, 2.055))
            Line((-2.812, 2.055), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.187, 2.255))
            Line((-2.187, 2.255), (-2.187, 2.055))
            Line((-2.187, 2.055), (-1.562, 2.055))
            Line((-1.562, 2.055), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.937, 2.255))
            Line((-0.937, 2.255), (-0.937, 2.055))
            Line((-0.937, 2.055), (-0.312, 2.055))
            Line((-0.312, 2.055), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 2.055))
            Line((0.313, 2.055), (0.938, 2.055))
            Line((0.938, 2.055), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 2.055))
            Line((1.562, 2.055), (2.187, 2.055))
            Line((2.187, 2.055), (2.187, 2.255))
            Line((2.187, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 2.055))
            Line((2.812, 2.055), (3.438, 2.055))
            Line((3.438, 2.055), (3.438, 2.255))
            Line((3.438, 2.255), (3.75, 2.255))
            Line((3.75, 2.255), (3.75, 2.76))
            Line((3.75, 2.76), (4.062, 2.76))
            Line((4.062, 2.76), (4.062, 2.055))
            Line((4.062, 2.055), (4.688, 2.055))
            Line((4.688, 2.055), (4.688, 2.255))
            Line((4.688, 2.255), (4.914, 2.255))
            Line((4.914, 2.255), (4.914, 2.96))
            Line((4.914, 2.96), (5.74, 2.96))
            Line((5.74, 2.96), (5.74, 0.58))
            Line((5.74, 0.58), (-5.74, 0.58))
            Line((-5.74, 0.58), (-5.74, 2.96))
            Line((-5.74, 2.96), (-4.914, 2.96))
        make_face()

    with BuildSketch(Plane.XY.offset(2.225)):
        with BuildLine():
            Line((-5.114, 2.76), (-5.114, 2.255))
            Line((-5.114, 2.255), (-4.687, 2.255))
            Line((-4.687, 2.255), (-4.687, 1.855))
            Line((-4.687, 1.855), (-4.062, 1.855))
            Line((-4.062, 1.855), (-4.062, 2.76))
            Line((-4.062, 2.76), (-3.75, 2.76))
            Line((-3.75, 2.76), (-3.75, 2.255))
            Line((-3.75, 2.255), (-3.437, 2.255))
            Line((-3.437, 2.255), (-3.437, 1.855))
            Line((-3.437, 1.855), (-2.812, 1.855))
            Line((-2.812, 1.855), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.187, 2.255))
            Line((-2.187, 2.255), (-2.187, 1.855))
            Line((-2.187, 1.855), (-1.562, 1.855))
            Line((-1.562, 1.855), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.937, 2.255))
            Line((-0.937, 2.255), (-0.937, 1.855))
            Line((-0.937, 1.855), (-0.312, 1.855))
            Line((-0.312, 1.855), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 1.855))
            Line((0.313, 1.855), (0.938, 1.855))
            Line((0.938, 1.855), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 1.855))
            Line((1.562, 1.855), (2.187, 1.855))
            Line((2.187, 1.855), (2.187, 2.255))
            Line((2.187, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 1.855))
            Line((2.812, 1.855), (3.438, 1.855))
            Line((3.438, 1.855), (3.438, 2.255))
            Line((3.438, 2.255), (3.75, 2.255))
            Line((3.75, 2.255), (3.75, 2.76))
            Line((3.75, 2.76), (4.062, 2.76))
            Line((4.062, 2.76), (4.062, 1.855))
            Line((4.062, 1.855), (4.688, 1.855))
            Line((4.688, 1.855), (4.688, 2.255))
            Line((4.688, 2.255), (5.114, 2.255))
            Line((5.114, 2.255), (5.114, 2.76))
            Line((5.114, 2.76), (5.54, 2.76))
            Line((5.54, 2.76), (5.54, 0.78))
            Line((5.54, 0.78), (-5.54, 0.78))
            Line((-5.54, 0.78), (-5.54, 2.76))
            Line((-5.54, 2.76), (-5.114, 2.76))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # 16 triangle profiles, subtract
    # Top side (Y=2.055)
    top_tri_x = [-4.475, -3.225, -1.975, -0.725, 0.525, 1.775, 3.025, 4.275]
    for tx in top_tri_x:
        sk_tri = Plane(origin=(tx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_tri):
            with BuildLine():
                Line((2.055, 2.425), (2.085, 2.425))
                Line((2.085, 2.425), (2.085, 2.225))
                Line((2.085, 2.225), (1.855, 2.225))
                Line((1.855, 2.225), (2.055, 2.425))
            make_face()
        extrude(amount=0.2, mode=Mode.SUBTRACT)

    # Bottom side (Y=0.58)
    bot_tri_x = [4.475, 3.225, 1.975, 0.725, -0.525, -1.775, -3.025, -4.275]
    for tx in bot_tri_x:
        sk_tri = Plane(origin=(tx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_tri):
            with BuildLine():
                Line((0.58, 2.425), (0.55, 2.425))
                Line((0.55, 2.425), (0.55, 2.225))
                Line((0.55, 2.225), (0.78, 2.225))
                Line((0.78, 2.225), (0.58, 2.425))
            make_face()
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

    # Complex profiles at X=-4.475, extrude to X=-4.275
    import numpy as np

    def arc_mid_from_centre(p1, p2, centre, r):
        c = np.array(centre)
        a = np.array(p1)
        b = np.array(p2)
        va = a - c
        vb = b - c
        mid_dir = va / np.linalg.norm(va) + vb / np.linalg.norm(vb)
        norm = np.linalg.norm(mid_dir)
        if norm < 1e-10:
            perp = np.array([-va[1], va[0]])
            mid_dir = perp / np.linalg.norm(perp)
        else:
            mid_dir = mid_dir / norm
        mid = c + mid_dir * r
        return tuple(mid)

    # Profile 1 arc midpoints
    a4 = arc_mid_from_centre((0.6, -1.625), (0.3, -1.925), (0.6, -1.925), 0.3)
    a13 = arc_mid_from_centre((1.586, 1.42), (1.63, 1.314), (1.48, 1.314), 0.15)
    a15 = arc_mid_from_centre((1.455, 1.613), (1.499, 1.507), (1.605, 1.613), 0.15)
    a17 = arc_mid_from_centre((1.499, 1.869), (1.455, 1.763), (1.605, 1.763), 0.15)
    a19 = arc_mid_from_centre((1.796, 2.166), (1.938, 2.225), (1.938, 2.025), 0.2)

    # Profile 2 arc midpoints
    b2 = arc_mid_from_centre((1.05, 1.869), (1.08, 1.779), (0.93, 1.779), 0.15)
    b7 = arc_mid_from_centre((0.681, 2.225), (0.84, 2.146), (0.681, 2.025), 0.2)

    complex_x = [-4.475, -3.225, -1.975, -0.725, 0.525, 1.775, 3.025, 4.275]

    for cx in complex_x:
        sk_p = Plane(origin=(cx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))

        for mode in [Mode.SUBTRACT, Mode.ADD]:
            # Profile 1
            with BuildSketch(sk_p):
                with BuildLine():
                    Line((2.085, 2.225), (2.085, -1.625))
                    Line((2.085, -1.625), (0.6, -1.625))
                    ThreePointArc((0.6, -1.625), a4, (0.3, -1.925))
                    Line((0.3, -1.925), (0.3, -2.425))
                    Line((0.3, -2.425), (0.0, -2.425))
                    Line((0.0, -2.425), (0.0, -1.41))
                    Line((0.0, -1.41), (0.225, -1.185))
                    Line((0.225, -1.185), (0.505, -1.185))
                    Line((0.505, -1.185), (0.625, -1.065))
                    Line((0.625, -1.065), (1.63, -1.065))
                    Line((1.63, -1.065), (1.63, 1.314))
                    ThreePointArc((1.63, 1.314), a13, (1.586, 1.42))
                    Line((1.586, 1.42), (1.499, 1.507))
                    ThreePointArc((1.499, 1.507), a15, (1.455, 1.613))
                    Line((1.455, 1.613), (1.455, 1.763))
                    ThreePointArc((1.455, 1.763), a17, (1.499, 1.869))
                    Line((1.499, 1.869), (1.796, 2.166))
                    ThreePointArc((1.796, 2.166), a19, (1.938, 2.225))
                    Line((1.938, 2.225), (2.085, 2.225))
                make_face()
            extrude(amount=0.2, mode=mode)

            # Profile 2
            with BuildSketch(sk_p):
                with BuildLine():
                    Line((0.84, 2.146), (1.05, 1.869))
                    ThreePointArc((1.05, 1.869), b2, (1.08, 1.779))
                    Line((1.08, 1.779), (1.08, 0.465))
                    Line((1.08, 0.465), (0.55, 0.465))
                    Line((0.55, 0.465), (0.55, 2.225))
                    Line((0.55, 2.225), (0.681, 2.225))
                    ThreePointArc((0.681, 2.225), b7, (0.84, 2.146))
                make_face()
            extrude(amount=0.2, mode=mode)

    # Side profile at X=6.355 with arcs, subtract+add, mirrored
    # Arc midpoints
    c7 = arc_mid_from_centre((0.925, 2.35), (0.85, 2.425), (0.85, 2.35), 0.075)
    c8 = (1.01, 2.265)   # semicircle bulge -Z
    c10 = (1.56, 2.265)  # semicircle bulge -Z
    c11 = arc_mid_from_centre((1.72, 2.425), (1.645, 2.35), (1.72, 2.35), 0.075)

    for x_orig, amt in [(6.355, -0.23), (-6.355, 0.23)]:
        sk_side = Plane(origin=(x_orig, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(sk_side):
                with BuildLine():
                    Line((2.21, 0.125), (0.15, 0.125))
                    Line((0.15, 0.125), (0.0, 0.275))
                    Line((0.0, 0.275), (0.0, 2.275))
                    Line((0.0, 2.275), (0.15, 2.425))
                    Line((0.15, 2.425), (0.85, 2.425))
                    ThreePointArc((0.85, 2.425), c7, (0.925, 2.35))
                    ThreePointArc((0.925, 2.35), c8, (1.095, 2.35))
                    Line((1.095, 2.35), (1.475, 2.35))
                    ThreePointArc((1.475, 2.35), c10, (1.645, 2.35))
                    ThreePointArc((1.645, 2.35), c11, (1.72, 2.425))
                    Line((1.72, 2.425), (2.21, 2.425))
                    Line((2.21, 2.425), (2.21, 0.125))
                make_face()
            extrude(amount=amt, mode=mode)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_SM08B-GHS-TB.stl")