from build123d import *

# Part: DRL0008A

with BuildPart() as part:
    # Rect 1 at Z=0.6 (1.108 x 2.008) with 0.05mm corner fillet
    with BuildSketch(Plane.XY.offset(0.6)):
        RectangleRounded(1.108, 2.008, 0.05)

    # Rect 2 at Z=0.025 (1.2 x 2.1) with 0.05mm corner fillet
    with BuildSketch(Plane.XY.offset(0.025)):
        RectangleRounded(1.2, 2.1, 0.05)

    loft()

    # Fillet top face edges (Z=0.6) by 0.05mm
    top_face = part.faces().sort_by(Axis.Z)[-1]
    long_edges = [e for e in top_face.edges() if e.length > 0.2]
    if long_edges:
        max_r = part.part.max_fillet(long_edges)
        print(f"Max fillet radius for top face edges: {max_r}")
        if max_r >= 0.05:
            fillet(long_edges, radius=0.05)
        elif max_r > 0:
            print(f"Using max radius: {max_r}")
            fillet(long_edges, radius=max_r * 0.9)

    # 8 rect bodies at Z=0.0, subtract then add, extrude up 0.13
    y_corners = [0.85, 0.35, -0.15, -0.65]

    # +X side
    for yc in y_corners:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((0.8, yc), (0.5, yc))
                Line((0.5, yc), (0.5, yc - 0.2))
                Line((0.5, yc - 0.2), (0.8, yc - 0.2))
                Line((0.8, yc - 0.2), (0.8, yc))
            make_face()
        extrude(amount=0.13, mode=Mode.SUBTRACT)

        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((0.8, yc), (0.5, yc))
                Line((0.5, yc), (0.5, yc - 0.2))
                Line((0.5, yc - 0.2), (0.8, yc - 0.2))
                Line((0.8, yc - 0.2), (0.8, yc))
            make_face()
        extrude(amount=0.13)

    # -X side (mirrored)
    for yc in y_corners:
        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((-0.5, yc), (-0.8, yc))
                Line((-0.8, yc), (-0.8, yc - 0.2))
                Line((-0.8, yc - 0.2), (-0.5, yc - 0.2))
                Line((-0.5, yc - 0.2), (-0.5, yc))
            make_face()
        extrude(amount=0.13, mode=Mode.SUBTRACT)

        with BuildSketch(Plane.XY.offset(0.0)):
            with BuildLine():
                Line((-0.5, yc), (-0.8, yc))
                Line((-0.8, yc), (-0.8, yc - 0.2))
                Line((-0.8, yc - 0.2), (-0.5, yc - 0.2))
                Line((-0.5, yc - 0.2), (-0.5, yc))
            make_face()
        extrude(amount=0.13)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_DRL0008A.stl")