from build123d import *

# Part: SM06B-GHS-TB

with BuildPart() as part:
    # Rect at Z=2.048 (10.75 x 4.07), extrude down to Z=-2.002
    with BuildSketch(Plane.XY.offset(2.048)):
        with BuildLine():
            Line((-5.375, 4.25), (5.375, 4.25))
            Line((5.375, 4.25), (5.375, 0.18))
            Line((5.375, 0.18), (-5.375, 0.18))
            Line((-5.375, 0.18), (-5.375, 4.25))
        make_face()
    extrude(amount=-4.05)

    # Rect in YZ plane at X=5.375 (Y: 2.4→3.4, Z: 0.088→2.048), extrude to X=5.265
    sk1 = Plane(origin=(5.375, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk1):
        with BuildLine():
            Line((3.4, 2.048), (3.4, 0.088))
            Line((3.4, 0.088), (2.4, 0.088))
            Line((2.4, 0.088), (2.4, 2.048))
            Line((2.4, 2.048), (3.4, 2.048))
        make_face()
    extrude(amount=-0.11, mode=Mode.SUBTRACT)

    # Mirror: -X side at X=-5.375, extrude to X=-5.265
    sk2 = Plane(origin=(-5.375, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk2):
        with BuildLine():
            Line((3.4, 2.048), (3.4, 0.088))
            Line((3.4, 0.088), (2.4, 0.088))
            Line((2.4, 0.088), (2.4, 2.048))
            Line((2.4, 2.048), (3.4, 2.048))
        make_face()
    extrude(amount=0.11, mode=Mode.SUBTRACT)

    # 5-point profile in XZ plane at Y=3.325, extrude to Y=3.965 (subtract)
    sk3 = Plane(origin=(0, 3.325, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk3):
        with BuildLine():
            Line((3.85, 0.088), (4.425, 0.088))
            Line((4.425, 0.088), (5.0, 0.663))
            Line((5.0, 0.663), (5.0, 2.048))
            Line((5.0, 2.048), (3.85, 2.048))
            Line((3.85, 2.048), (3.85, 0.088))
        make_face()
    extrude(amount=-0.64, mode=Mode.SUBTRACT)

    # Mirror: -X side
    with BuildSketch(sk3):
        with BuildLine():
            Line((-3.85, 0.088), (-4.425, 0.088))
            Line((-4.425, 0.088), (-5.0, 0.663))
            Line((-5.0, 0.663), (-5.0, 2.048))
            Line((-5.0, 2.048), (-3.85, 2.048))
            Line((-3.85, 2.048), (-3.85, 0.088))
        make_face()
    extrude(amount=-0.64, mode=Mode.SUBTRACT)

    # Triangle profile in XZ plane at Y=4.25, extrude to Y=4.19
    sk4 = Plane(origin=(0, 4.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    with BuildSketch(sk4):
        with BuildLine():
            Line((-5.075, 2.048), (-4.688, 1.378))
            Line((-4.688, 1.378), (-4.301, 2.048))
            Line((-4.301, 2.048), (-5.075, 2.048))
        make_face()
    extrude(amount=0.06, mode=Mode.SUBTRACT)

    # 6-point profile in YZ plane at X=4.515, extrude to X=5.375 (subtract)
    sk5 = Plane(origin=(4.515, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5):
        with BuildLine():
            Line((4.25, 0.118), (4.12, 0.118))
            Line((4.12, 0.118), (4.12, -1.702))
            Line((4.12, -1.702), (1.903, -1.702))
            Line((1.903, -1.702), (1.903, -2.002))
            Line((1.903, -2.002), (4.25, -2.002))
            Line((4.25, -2.002), (4.25, 0.118))
        make_face()
    extrude(amount=0.86, mode=Mode.SUBTRACT)

    # 8-point profile in YZ plane at X=4.875, extrude to X=5.375 (subtract)
    sk6 = Plane(origin=(4.875, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6):
        with BuildLine():
            Line((4.12, 0.118), (3.965, 0.118))
            Line((3.965, 0.118), (3.965, 0.088))
            Line((3.965, 0.088), (3.5, 0.088))
            Line((3.5, 0.088), (3.5, -1.312))
            Line((3.5, -1.312), (1.903, -1.312))
            Line((1.903, -1.312), (1.903, -1.702))
            Line((1.903, -1.702), (4.12, -1.702))
            Line((4.12, -1.702), (4.12, 0.118))
        make_face()
    extrude(amount=0.5, mode=Mode.SUBTRACT)

    # Small rect in YZ plane at X=5.0, extrude to X=5.375 (subtract)
    sk7 = Plane(origin=(5.0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk7):
        with BuildLine():
            Line((3.965, 0.118), (3.965, 0.088))
            Line((3.965, 0.088), (3.5, 0.088))
            Line((3.5, 0.088), (3.5, 0.118))
            Line((3.5, 0.118), (3.965, 0.118))
        make_face()
    extrude(amount=0.375, mode=Mode.SUBTRACT)

    # Mirror: 6-point profile at X=-4.515, extrude to X=-5.375
    sk5m = Plane(origin=(-4.515, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk5m):
        with BuildLine():
            Line((4.25, 0.118), (4.12, 0.118))
            Line((4.12, 0.118), (4.12, -1.702))
            Line((4.12, -1.702), (1.903, -1.702))
            Line((1.903, -1.702), (1.903, -2.002))
            Line((1.903, -2.002), (4.25, -2.002))
            Line((4.25, -2.002), (4.25, 0.118))
        make_face()
    extrude(amount=-0.86, mode=Mode.SUBTRACT)

    # Mirror: 8-point profile at X=-4.875, extrude to X=-5.375
    sk6m = Plane(origin=(-4.875, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk6m):
        with BuildLine():
            Line((4.12, 0.118), (3.965, 0.118))
            Line((3.965, 0.118), (3.965, 0.088))
            Line((3.965, 0.088), (3.5, 0.088))
            Line((3.5, 0.088), (3.5, -1.312))
            Line((3.5, -1.312), (1.903, -1.312))
            Line((1.903, -1.312), (1.903, -1.702))
            Line((1.903, -1.702), (4.12, -1.702))
            Line((4.12, -1.702), (4.12, 0.118))
        make_face()
    extrude(amount=-0.5, mode=Mode.SUBTRACT)

    # Mirror: Small rect at X=-5.0, extrude to X=-5.375
    sk7m = Plane(origin=(-5.0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk7m):
        with BuildLine():
            Line((3.965, 0.118), (3.965, 0.088))
            Line((3.965, 0.088), (3.5, 0.088))
            Line((3.5, 0.088), (3.5, 0.118))
            Line((3.5, 0.118), (3.965, 0.118))
        make_face()
    extrude(amount=-0.375, mode=Mode.SUBTRACT)

    # Rect at Z=-2.002 (6.6 x 1.33), extrude up to Z=-1.202 (subtract)
    with BuildSketch(Plane.XY.offset(-2.002)):
        with BuildLine():
            Line((3.3, 3.82), (-3.3, 3.82))
            Line((-3.3, 3.82), (-3.3, 2.49))
            Line((-3.3, 2.49), (3.3, 2.49))
            Line((3.3, 2.49), (3.3, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # Rect at Z=-2.002 (-X side), extrude up to Z=-1.202 (subtract)
    with BuildSketch(Plane.XY.offset(-2.002)):
        with BuildLine():
            Line((-3.94, 3.82), (-4.3, 3.82))
            Line((-4.3, 3.82), (-4.3, 3.24))
            Line((-4.3, 3.24), (-3.94, 3.24))
            Line((-3.94, 3.24), (-3.94, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # Mirror: +X side
    with BuildSketch(Plane.XY.offset(-2.002)):
        with BuildLine():
            Line((3.94, 3.82), (4.3, 3.82))
            Line((4.3, 3.82), (4.3, 3.24))
            Line((4.3, 3.24), (3.94, 3.24))
            Line((3.94, 3.24), (3.94, 3.82))
        make_face()
    extrude(amount=0.8, mode=Mode.SUBTRACT)

    # Rect in YZ plane at X=5.375 (Y: 0.34→1.03, Z: -2.002→-1.442), extrude to X=-5.375
    sk8 = Plane(origin=(5.375, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk8):
        with BuildLine():
            Line((1.03, -2.002), (1.03, -1.442))
            Line((1.03, -1.442), (0.34, -1.442))
            Line((0.34, -1.442), (0.34, -2.002))
            Line((0.34, -2.002), (1.03, -2.002))
        make_face()
    extrude(amount=-10.75, mode=Mode.SUBTRACT)

    # Rect in YZ plane at X=5.375 (Y: 0.18→0.34, Z: -2.002→-1.292), extrude to X=-5.375
    with BuildSketch(sk8):
        with BuildLine():
            Line((0.34, -2.002), (0.34, -1.292))
            Line((0.34, -1.292), (0.18, -1.292))
            Line((0.18, -1.292), (0.18, -2.002))
            Line((0.18, -2.002), (0.34, -2.002))
        make_face()
    extrude(amount=-10.75, mode=Mode.SUBTRACT)

    # 11-point profile at Z=-0.252, extrude to Z=2.048 (subtract)
    with BuildSketch(Plane.XY.offset(-0.252)):
        with BuildLine():
            Line((-5.105, 2.21), (-4.875, 2.21))
            Line((-4.875, 2.21), (-4.875, 0.48))
            Line((-4.875, 0.48), (-4.775, 0.48))
            Line((-4.775, 0.48), (-4.475, 0.18))
            Line((-4.475, 0.18), (-5.375, 0.18))
            Line((-5.375, 0.18), (-5.375, 0.78))
            Line((-5.375, 0.78), (-5.225, 0.78))
            Line((-5.225, 0.78), (-5.225, 0.48))
            Line((-5.225, 0.48), (-5.105, 0.48))
            Line((-5.105, 0.48), (-5.105, 0.78))
            Line((-5.105, 0.78), (-5.105, 2.21))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Rect at Z=-0.302, extrude to Z=2.048
    with BuildSketch(Plane.XY.offset(-0.302)):
        with BuildLine():
            Line((-5.225, 0.78), (-5.105, 0.78))
            Line((-5.105, 0.78), (-5.105, 0.53))
            Line((-5.105, 0.53), (-5.225, 0.53))
            Line((-5.225, 0.53), (-5.225, 0.78))
        make_face()
    extrude(amount=2.35, mode=Mode.SUBTRACT)

    # Rect at Z=-0.252, extrude to Z=2.048
    with BuildSketch(Plane.XY.offset(-0.252)):
        with BuildLine():
            Line((-5.225, 0.53), (-5.105, 0.53))
            Line((-5.105, 0.53), (-5.105, 0.48))
            Line((-5.105, 0.48), (-5.225, 0.48))
            Line((-5.225, 0.48), (-5.225, 0.53))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Triangle in YZ plane at X=-5.105, extrude to X=-5.225
    sk9 = Plane(origin=(-5.105, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk9):
        with BuildLine():
            Line((0.53, -0.302), (0.53, -0.252))
            Line((0.53, -0.252), (0.48, -0.252))
            Line((0.48, -0.252), (0.53, -0.302))
        make_face()
    extrude(amount=-0.12, mode=Mode.SUBTRACT)

    # 4-point profile in YZ plane at X=-5.225, extrude to X=-5.105
    sk10 = Plane(origin=(-5.225, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk10):
        with BuildLine():
            Line((2.21, 1.348), (2.21, 1.298))
            Line((2.21, 1.298), (1.76, 1.298))
            Line((1.76, 1.298), (1.71, 1.348))
            Line((1.71, 1.348), (2.21, 1.348))
        make_face()
    extrude(amount=0.12, mode=Mode.SUBTRACT)

    # Rect at Z=1.348 (X: -5.375→-5.105, Y: 0.78→2.21), extrude to Z=2.048 (subtract)
    with BuildSketch(Plane.XY.offset(1.348)):
        with BuildLine():
            Line((-5.375, 2.21), (-5.105, 2.21))
            Line((-5.105, 2.21), (-5.105, 0.78))
            Line((-5.105, 0.78), (-5.375, 0.78))
            Line((-5.375, 0.78), (-5.375, 2.21))
        make_face()
    extrude(amount=0.7, mode=Mode.SUBTRACT)

    # Loft between two rects in subtract mode
    # Rect 1 at Z=2.048 (X: -5.375→-4.825, Y: 0.48→2.26)
    with BuildSketch(Plane.XY.offset(2.048)):
        with BuildLine():
            Line((-5.375, 2.26), (-4.825, 2.26))
            Line((-4.825, 2.26), (-4.825, 0.48))
            Line((-4.825, 0.48), (-5.375, 0.48))
            Line((-5.375, 0.48), (-5.375, 2.26))
        make_face()

    # Rect 2 at Z=1.998 (X: -5.375→-4.875, Y: 0.48→2.21)
    with BuildSketch(Plane.XY.offset(1.998)):
        with BuildLine():
            Line((-5.375, 2.21), (-4.875, 2.21))
            Line((-4.875, 2.21), (-4.875, 0.48))
            Line((-4.875, 0.48), (-5.375, 0.48))
            Line((-5.375, 0.48), (-5.375, 2.21))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # === Mirror of features after line 178 about X=0, YZ plane ===

    # Mirror: 11-point profile at Z=-0.252 (+X side)
    with BuildSketch(Plane.XY.offset(-0.252)):
        with BuildLine():
            Line((5.105, 2.21), (4.875, 2.21))
            Line((4.875, 2.21), (4.875, 0.48))
            Line((4.875, 0.48), (4.775, 0.48))
            Line((4.775, 0.48), (4.475, 0.18))
            Line((4.475, 0.18), (5.375, 0.18))
            Line((5.375, 0.18), (5.375, 0.78))
            Line((5.375, 0.78), (5.225, 0.78))
            Line((5.225, 0.78), (5.225, 0.48))
            Line((5.225, 0.48), (5.105, 0.48))
            Line((5.105, 0.48), (5.105, 0.78))
            Line((5.105, 0.78), (5.105, 2.21))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Mirror: Rect at Z=-0.302
    with BuildSketch(Plane.XY.offset(-0.302)):
        with BuildLine():
            Line((5.225, 0.78), (5.105, 0.78))
            Line((5.105, 0.78), (5.105, 0.53))
            Line((5.105, 0.53), (5.225, 0.53))
            Line((5.225, 0.53), (5.225, 0.78))
        make_face()
    extrude(amount=2.35, mode=Mode.SUBTRACT)

    # Mirror: Rect at Z=-0.252
    with BuildSketch(Plane.XY.offset(-0.252)):
        with BuildLine():
            Line((5.225, 0.53), (5.105, 0.53))
            Line((5.105, 0.53), (5.105, 0.48))
            Line((5.105, 0.48), (5.225, 0.48))
            Line((5.225, 0.48), (5.225, 0.53))
        make_face()
    extrude(amount=2.3, mode=Mode.SUBTRACT)

    # Mirror: Triangle in YZ plane at X=5.105, extrude to X=5.225
    sk9m = Plane(origin=(5.105, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk9m):
        with BuildLine():
            Line((0.53, -0.302), (0.53, -0.252))
            Line((0.53, -0.252), (0.48, -0.252))
            Line((0.48, -0.252), (0.53, -0.302))
        make_face()
    extrude(amount=0.12, mode=Mode.SUBTRACT)

    # Mirror: 4-point profile in YZ plane at X=5.225, extrude to X=5.105
    sk10m = Plane(origin=(5.225, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk10m):
        with BuildLine():
            Line((2.21, 1.348), (2.21, 1.298))
            Line((2.21, 1.298), (1.76, 1.298))
            Line((1.76, 1.298), (1.71, 1.348))
            Line((1.71, 1.348), (2.21, 1.348))
        make_face()
    extrude(amount=-0.12, mode=Mode.SUBTRACT)

    # Mirror: Rect at Z=1.348 (+X side)
    with BuildSketch(Plane.XY.offset(1.348)):
        with BuildLine():
            Line((5.375, 2.21), (5.105, 2.21))
            Line((5.105, 2.21), (5.105, 0.78))
            Line((5.105, 0.78), (5.375, 0.78))
            Line((5.375, 0.78), (5.375, 2.21))
        make_face()
    extrude(amount=0.7, mode=Mode.SUBTRACT)

    # Mirror: Loft between two rects (+X side)
    with BuildSketch(Plane.XY.offset(2.048)):
        with BuildLine():
            Line((5.375, 2.26), (4.825, 2.26))
            Line((4.825, 2.26), (4.825, 0.48))
            Line((4.825, 0.48), (5.375, 0.48))
            Line((5.375, 0.48), (5.375, 2.26))
        make_face()

    with BuildSketch(Plane.XY.offset(1.998)):
        with BuildLine():
            Line((5.375, 2.21), (4.875, 2.21))
            Line((4.875, 2.21), (4.875, 0.48))
            Line((4.875, 0.48), (5.375, 0.48))
            Line((5.375, 0.48), (5.375, 2.21))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # 32-point comb profile at Z=1.848, extrude to Z=0.088 (subtract)
    with BuildSketch(Plane.XY.offset(1.848)):
        with BuildLine():
            Line((-4.29, 2.76), (-3.864, 2.76))
            Line((-3.864, 2.76), (-3.864, 2.255))
            Line((-3.864, 2.255), (-3.438, 2.255))
            Line((-3.438, 2.255), (-3.438, 1.855))
            Line((-3.438, 1.855), (-2.812, 1.855))
            Line((-2.812, 1.855), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.188, 2.255))
            Line((-2.188, 2.255), (-2.188, 1.855))
            Line((-2.188, 1.855), (-1.562, 1.855))
            Line((-1.562, 1.855), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.938, 2.255))
            Line((-0.938, 2.255), (-0.938, 1.855))
            Line((-0.938, 1.855), (-0.312, 1.855))
            Line((-0.312, 1.855), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 1.855))
            Line((0.313, 1.855), (0.938, 1.855))
            Line((0.938, 1.855), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 1.855))
            Line((1.562, 1.855), (2.188, 1.855))
            Line((2.188, 1.855), (2.188, 2.255))
            Line((2.188, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 1.855))
            Line((2.812, 1.855), (3.438, 1.855))
            Line((3.438, 1.855), (3.438, 2.255))
            Line((3.438, 2.255), (3.864, 2.255))
            Line((3.864, 2.255), (3.864, 2.76))
            Line((3.864, 2.76), (4.29, 2.76))
            Line((4.29, 2.76), (4.29, 0.78))
            Line((4.29, 0.78), (-4.29, 0.78))
            Line((-4.29, 0.78), (-4.29, 2.76))
        make_face()
    extrude(amount=-1.76, mode=Mode.SUBTRACT)

    # Loft between outer profile at Z=2.048 and inner profile at Z=1.848 (subtract)
    # Outer profile at Z=2.048
    with BuildSketch(Plane.XY.offset(2.048)):
        with BuildLine():
            Line((-4.49, 2.96), (-3.664, 2.96))
            Line((-3.664, 2.96), (-3.664, 2.255))
            Line((-3.664, 2.255), (-3.438, 2.255))
            Line((-3.438, 2.255), (-3.438, 2.055))
            Line((-3.438, 2.055), (-2.812, 2.055))
            Line((-2.812, 2.055), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.188, 2.255))
            Line((-2.188, 2.255), (-2.188, 2.055))
            Line((-2.188, 2.055), (-1.562, 2.055))
            Line((-1.562, 2.055), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.938, 2.255))
            Line((-0.938, 2.255), (-0.938, 2.055))
            Line((-0.938, 2.055), (-0.312, 2.055))
            Line((-0.312, 2.055), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 2.055))
            Line((0.313, 2.055), (0.938, 2.055))
            Line((0.938, 2.055), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 2.055))
            Line((1.562, 2.055), (2.188, 2.055))
            Line((2.188, 2.055), (2.188, 2.255))
            Line((2.188, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 2.055))
            Line((2.812, 2.055), (3.438, 2.055))
            Line((3.438, 2.055), (3.438, 2.255))
            Line((3.438, 2.255), (3.664, 2.255))
            Line((3.664, 2.255), (3.664, 2.96))
            Line((3.664, 2.96), (4.49, 2.96))
            Line((4.49, 2.96), (4.49, 0.58))
            Line((4.49, 0.58), (-4.49, 0.58))
            Line((-4.49, 0.58), (-4.49, 2.96))
        make_face()

    # Inner profile at Z=1.848
    with BuildSketch(Plane.XY.offset(1.848)):
        with BuildLine():
            Line((-4.29, 2.76), (-3.864, 2.76))
            Line((-3.864, 2.76), (-3.864, 2.255))
            Line((-3.864, 2.255), (-3.438, 2.255))
            Line((-3.438, 2.255), (-3.438, 1.855))
            Line((-3.438, 1.855), (-2.812, 1.855))
            Line((-2.812, 1.855), (-2.812, 2.255))
            Line((-2.812, 2.255), (-2.188, 2.255))
            Line((-2.188, 2.255), (-2.188, 1.855))
            Line((-2.188, 1.855), (-1.562, 1.855))
            Line((-1.562, 1.855), (-1.562, 2.255))
            Line((-1.562, 2.255), (-0.938, 2.255))
            Line((-0.938, 2.255), (-0.938, 1.855))
            Line((-0.938, 1.855), (-0.312, 1.855))
            Line((-0.312, 1.855), (-0.312, 2.255))
            Line((-0.312, 2.255), (0.313, 2.255))
            Line((0.313, 2.255), (0.313, 1.855))
            Line((0.313, 1.855), (0.938, 1.855))
            Line((0.938, 1.855), (0.938, 2.255))
            Line((0.938, 2.255), (1.562, 2.255))
            Line((1.562, 2.255), (1.562, 1.855))
            Line((1.562, 1.855), (2.188, 1.855))
            Line((2.188, 1.855), (2.188, 2.255))
            Line((2.188, 2.255), (2.812, 2.255))
            Line((2.812, 2.255), (2.812, 1.855))
            Line((2.812, 1.855), (3.438, 1.855))
            Line((3.438, 1.855), (3.438, 2.255))
            Line((3.438, 2.255), (3.864, 2.255))
            Line((3.864, 2.255), (3.864, 2.76))
            Line((3.864, 2.76), (4.29, 2.76))
            Line((4.29, 2.76), (4.29, 0.78))
            Line((4.29, 0.78), (-4.29, 0.78))
            Line((-4.29, 0.78), (-4.29, 2.76))
        make_face()

    loft(mode=Mode.SUBTRACT)

    # 12 slot extrusions in subtract mode
    # Top side (Y=2.085): profile goes downward
    top_x = [-3.225, -1.975, -0.725, 0.525, 1.775, 3.025]
    for lx in top_x:
        sk_slot = Plane(origin=(lx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_slot):
            with BuildLine():
                Line((2.085, 0.088), (1.855, 0.088))
                Line((1.855, 0.088), (1.855, 1.848))
                Line((1.855, 1.848), (2.055, 2.048))
                Line((2.055, 2.048), (2.085, 2.048))
                Line((2.085, 2.048), (2.085, 0.088))
            make_face()
        extrude(amount=0.2, mode=Mode.SUBTRACT)

    # Bottom side (Y=0.55): profile goes upward (mirrored in Y)
    bot_x = [3.225, 1.975, 0.725, -0.525, -1.775, -3.025]
    for lx in bot_x:
        sk_slot = Plane(origin=(lx, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
        with BuildSketch(sk_slot):
            with BuildLine():
                Line((0.55, 0.088), (0.78, 0.088))
                Line((0.78, 0.088), (0.78, 1.848))
                Line((0.78, 1.848), (0.58, 2.048))
                Line((0.58, 2.048), (0.55, 2.048))
                Line((0.55, 2.048), (0.55, 0.088))
            make_face()
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

    # 12-point profile in YZ plane at X=-5.105 with arcs, subtract+add+mirror
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

    # Arc midpoints in sketch coords (sketch X=world Y, sketch Y=world Z)
    # P3→P4: centre (1.72, 1.973), R=0.075
    am_a = arc_mid_from_centre((1.72, 2.048), (1.645, 1.973), (1.72, 1.973), 0.075)
    # P4→P5: semicircle, centre (1.56, 1.973), R=0.085, bulge -Z
    am_b = (1.56, 1.888)
    # P6→P7: semicircle, centre (1.01, 1.973), R=0.085, bulge -Z
    am_c = (1.01, 1.888)
    # P7→P8: centre (0.85, 1.973), R=0.075
    am_d = arc_mid_from_centre((0.925, 1.973), (0.85, 2.048), (0.85, 1.973), 0.075)

    # -X side and +X side
    configs = [
        (-5.105, 0.23),   # -X side, extrude +X
        (5.105, -0.23),   # +X side (mirror), extrude -X
    ]

    for x_orig, amt in configs:
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            sk_pin = Plane(origin=(x_orig, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
            with BuildSketch(sk_pin):
                with BuildLine():
                    Line((2.21, -0.252), (2.21, 2.048))
                    Line((2.21, 2.048), (1.72, 2.048))
                    ThreePointArc((1.72, 2.048), am_a, (1.645, 1.973))
                    ThreePointArc((1.645, 1.973), am_b, (1.475, 1.973))
                    Line((1.475, 1.973), (1.095, 1.973))
                    ThreePointArc((1.095, 1.973), am_c, (0.925, 1.973))
                    ThreePointArc((0.925, 1.973), am_d, (0.85, 2.048))
                    Line((0.85, 2.048), (0.15, 2.048))
                    Line((0.15, 2.048), (0.0, 1.898))
                    Line((0.0, 1.898), (0.0, -0.102))
                    Line((0.0, -0.102), (0.15, -0.252))
                    Line((0.15, -0.252), (2.21, -0.252))
                make_face()
            extrude(amount=amt, mode=mode)

    # Complex profile in YZ plane at X=-3.025, extrude to X=-3.225
    # Arc midpoints
    am_e3 = arc_mid_from_centre((0.6, -2.002), (0.3, -2.302), (0.6, -2.302), 0.3)
    am_e12 = arc_mid_from_centre((1.586, 1.043), (1.63, 0.937), (1.48, 0.937), 0.15)
    am_e14 = arc_mid_from_centre((1.455, 1.236), (1.499, 1.13), (1.605, 1.236), 0.15)
    am_e16 = arc_mid_from_centre((1.499, 1.492), (1.455, 1.386), (1.605, 1.386), 0.15)
    am_e18 = arc_mid_from_centre((1.938, 1.848), (1.796, 1.789), (1.938, 1.648), 0.2)

    sk_complex = Plane(origin=(-3.025, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    with BuildSketch(sk_complex):
        with BuildLine():
            Line((2.085, 1.848), (2.085, -2.002))            # Edge 1: P1→P2 (start)
            Line((2.085, -2.002), (0.6, -2.002))             # Edge 2: P2→P3
            ThreePointArc((0.6, -2.002), am_e3, (0.3, -2.302))  # Edge 3: arc
            Line((0.3, -2.302), (0.3, -2.802))               # Edge 4
            Line((0.3, -2.802), (0.0, -2.802))               # Edge 5
            Line((0.0, -2.802), (0.0, -1.787))               # Edge 6
            Line((0.0, -1.787), (0.225, -1.562))             # Edge 7
            Line((0.225, -1.562), (0.505, -1.562))           # Edge 8
            Line((0.505, -1.562), (0.625, -1.442))           # Edge 9
            Line((0.625, -1.442), (1.63, -1.442))            # Edge 10
            Line((1.63, -1.442), (1.63, 0.937))              # Edge 11
            ThreePointArc((1.63, 0.937), am_e12, (1.586, 1.043))  # Edge 12: arc
            Line((1.586, 1.043), (1.499, 1.13))              # Edge 13
            ThreePointArc((1.499, 1.13), am_e14, (1.455, 1.236))  # Edge 14: arc
            Line((1.455, 1.236), (1.455, 1.386))             # Edge 15
            ThreePointArc((1.455, 1.386), am_e16, (1.499, 1.492))  # Edge 16: arc
            Line((1.499, 1.492), (1.796, 1.789))             # Edge 17
            ThreePointArc((1.796, 1.789), am_e18, (1.938, 1.848))  # Edge 18: arc
            Line((1.938, 1.848), (2.085, 1.848))             # Edge 19: close
        make_face()
    extrude(amount=-0.2)
# 7-point profile in YZ plane at X=-3.025
    # Edge 1: Arc center (0.93, 1.401), R=0.15
    am_new1 = arc_mid_from_centre((1.05, 1.492), (1.08, 1.401), (0.93, 1.401), 0.15)
    
    # Edge 6: Arc center (0.681, 1.648), R=0.2
    am_new6 = arc_mid_from_centre((0.681, 1.848), (0.84, 1.769), (0.681, 1.648), 0.2)

    sk_new = Plane(origin=(-3.025, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))

    # The user requested both add and subtract modes
    for mode in [Mode.SUBTRACT, Mode.ADD]:
        with BuildSketch(sk_new):
            with BuildLine():
                # Edge 1 (Arc)
                ThreePointArc((1.05, 1.492),(1.072, 1.449), (1.08, 1.401))
                # Edge 2 (Line)
                Line((1.08, 1.401), (1.08, 0.088))
                # Edge 3 (Line)
                Line((1.08, 0.088), (0.55, 0.088))
                # Edge 4 (Line - reversed to maintain loop)
                Line((0.55, 0.088), (0.55, 1.848))
                # Edge 5 (Line - reversed to maintain loop)
                Line((0.55, 1.848), (0.681, 1.848))
                # Edge 6 (Arc - reversed to maintain loop)
                ThreePointArc((0.681, 1.848), (0.77, 1.827), (0.84, 1.769))
                # Edge 7 (Line)
                Line((0.84, 1.769), (1.05, 1.492))
            make_face()
        
        # Extrude to X=-3.225 (Relative amount is -0.2 since Plane is at X=-3.025)
        extrude(amount=-0.2, mode=mode)
# Target left X-coordinates for the 6 patterned bodies
    left_x_coords = [-3.225, -1.975, -0.725, 0.525, 1.775, 3.025]

    # --- Arc midpoints for the 19-point profile ---
    am_e3 = arc_mid_from_centre((0.6, -2.002), (0.3, -2.302), (0.6, -2.302), 0.3)
    am_e12 = arc_mid_from_centre((1.586, 1.043), (1.63, 0.937), (1.48, 0.937), 0.15)
    am_e14 = arc_mid_from_centre((1.455, 1.236), (1.499, 1.13), (1.605, 1.236), 0.15)
    am_e16 = arc_mid_from_centre((1.499, 1.492), (1.455, 1.386), (1.605, 1.386), 0.15)
    am_e18 = arc_mid_from_centre((1.938, 1.848), (1.796, 1.789), (1.938, 1.648), 0.2)

    # --- Pattern Loop ---
    for lx in left_x_coords:
        # Calculate the right-side plane origin (Left Corner + 0.2)
        plane_x = lx + 0.2
        sk_plane = Plane(origin=(plane_x, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))

        # 1. Extrude the 19-point Complex Profile
        with BuildSketch(sk_plane):
            with BuildLine():
                Line((2.085, 1.848), (2.085, -2.002))            # Edge 1
                Line((2.085, -2.002), (0.6, -2.002))             # Edge 2
                ThreePointArc((0.6, -2.002), am_e3, (0.3, -2.302))  # Edge 3
                Line((0.3, -2.302), (0.3, -2.802))               # Edge 4
                Line((0.3, -2.802), (0.0, -2.802))               # Edge 5
                Line((0.0, -2.802), (0.0, -1.787))               # Edge 6
                Line((0.0, -1.787), (0.225, -1.562))             # Edge 7
                Line((0.225, -1.562), (0.505, -1.562))           # Edge 8
                Line((0.505, -1.562), (0.625, -1.442))           # Edge 9
                Line((0.625, -1.442), (1.63, -1.442))            # Edge 10
                Line((1.63, -1.442), (1.63, 0.937))              # Edge 11
                ThreePointArc((1.63, 0.937), am_e12, (1.586, 1.043))  # Edge 12
                Line((1.586, 1.043), (1.499, 1.13))              # Edge 13
                ThreePointArc((1.499, 1.13), am_e14, (1.455, 1.236))  # Edge 14
                Line((1.455, 1.236), (1.455, 1.386))             # Edge 15
                ThreePointArc((1.455, 1.386), am_e16, (1.499, 1.492))  # Edge 16
                Line((1.499, 1.492), (1.796, 1.789))             # Edge 17
                ThreePointArc((1.796, 1.789), am_e18, (1.938, 1.848))  # Edge 18
                Line((1.938, 1.848), (2.085, 1.848))             # Edge 19
            make_face()
        
        # Kept original behavior (defaults to Mode.ADD). 
        # If this is supposed to carve out a hole, add `mode=Mode.SUBTRACT`.
        extrude(amount=-0.2)

        # 2. Extrude the 7-point Pin Profile (Subtract, then Add)
        for mode in [Mode.SUBTRACT, Mode.ADD]:
            with BuildSketch(sk_plane):
                with BuildLine():
                    ThreePointArc((1.05, 1.492), (1.072, 1.449), (1.08, 1.401))
                    Line((1.08, 1.401), (1.08, 0.088))
                    Line((1.08, 0.088), (0.55, 0.088))
                    Line((0.55, 0.088), (0.55, 1.848))
                    Line((0.55, 1.848), (0.681, 1.848))
                    ThreePointArc((0.681, 1.848), (0.77, 1.827), (0.84, 1.769))
                    Line((0.84, 1.769), (1.05, 1.492))
                make_face()
            extrude(amount=-0.2, mode=mode)
from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_SM06B-GHS-TB.stl")