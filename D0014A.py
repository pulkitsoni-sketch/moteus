from build123d import *
import math

# Part: D0014A

offset_x = 0.11 * math.tan(math.radians(10))

with BuildPart() as part:
    # Rect 1 at Z=0.2 (3.726 x 8.475) with 0.2mm corner fillet
    with BuildSketch(Plane.XY.offset(0.2)):
        RectangleRounded(3.726, 8.475, 0.2)

    # Rect 2 at Z=0.88 (3.9 x 8.65) with 0.2mm corner fillet
    with BuildSketch(Plane.XY.offset(0.88)):
        RectangleRounded(3.9, 8.65, 0.2)

    loft()

    # Extrude top face at Z=0.88 up to Z=1.07
    top_face = part.faces().sort_by(Axis.Z)[-1]
    extrude(top_face, amount=0.19)

    # Tapered loft from Z=1.07 to Z=1.18 (X tapers inward)
    with BuildSketch(Plane.XY.offset(1.07)):
        RectangleRounded(3.9, 8.65, 0.2)

    with BuildSketch(Plane.XY.offset(1.18)):
        RectangleRounded(3.9 - 2 * offset_x, 8.65, 0.2)

    loft()

    # Loft from Z=1.18 to rect at Z=1.75
    # Top rect: X from -1.354 to 1.812 = width 3.166, centre X = 0.229
    # Y from -4.238 to 4.237 = height 8.475, centre Y ~ 0
    with BuildSketch(Plane.XY.offset(1.18)):
        RectangleRounded(3.9 - 2 * offset_x, 8.65, 0.2)

    with BuildSketch(Plane.XY.offset(1.75)):
        with Locations([(0.229, -0.0005)]):
            RectangleRounded(3.166, 8.475, 0.2)

    loft()

    # Fillet bottom face edges (Z=0.2) by 0.2mm
    bottom_face = part.faces().sort_by(Axis.Z)[0]
    fillet(bottom_face.edges(), radius=0.2)

    # Fillet top face edges (Z=1.75) by 0.2mm
    top_face_final = part.faces().sort_by(Axis.Z)[-1]
    fillet(top_face_final.edges(), radius=0.2)

    # Profile in XZ plane, 7 bodies at different Y positions, extruded -1.68
    import numpy as np

    def arc_mid_from_centre(p1, p2, centre, r):
        """Compute arc midpoint given endpoints and centre in 2D"""
        c = np.array(centre)
        a = np.array(p1)
        b = np.array(p2)
        va = a - c
        vb = b - c
        mid_dir = va / np.linalg.norm(va) + vb / np.linalg.norm(vb)
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
        mid = c + mid_dir * r
        return tuple(mid)

    # Arc midpoints (same for all bodies, profile shape is identical)
    m1 = arc_mid_from_centre((1.97, 0.88), (2.068, 0.797), (1.97, 0.78), 0.1)
    m2 = arc_mid_from_centre((2.152, 0.325), (2.472, 0.037), (2.496, 0.386), 0.35)
    m3 = arc_mid_from_centre((2.485, 0.226), (2.339, 0.358), (2.496, 0.386), 0.16)
    m4 = arc_mid_from_centre((2.256, 0.83), (1.97, 1.07), (1.97, 0.78), 0.29)

    y_positions = [-4.015, -2.745, -1.475, -0.205, 1.065, 2.335, 3.605]

    for y_pos in y_positions:
        sk_plane = Plane(origin=(0, y_pos, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_plane):
            with BuildLine():
                Line((1.95, 0.88), (1.97, 0.88))
                ThreePointArc((1.97, 0.88), m1, (2.068, 0.797))
                Line((2.068, 0.797), (2.152, 0.325))
                ThreePointArc((2.152, 0.325), m2, (2.472, 0.037))
                Line((2.472, 0.037), (3.0, 0.0))
                Line((3.0, 0.0), (3.013, 0.19))
                Line((3.013, 0.19), (2.485, 0.226))
                ThreePointArc((2.485, 0.226), m3, (2.339, 0.358))
                Line((2.339, 0.358), (2.256, 0.83))
                ThreePointArc((2.256, 0.83), m4, (1.97, 1.07))
                Line((1.97, 1.07), (1.95, 1.07))
                Line((1.95, 1.07), (1.95, 0.88))
            make_face()
        extrude(amount=-0.41)

    # Mirrored -X side: flip X coordinates
    m1n = arc_mid_from_centre((-1.97, 0.88), (-2.068, 0.797), (-1.97, 0.78), 0.1)
    m2n = arc_mid_from_centre((-2.152, 0.325), (-2.472, 0.037), (-2.496, 0.386), 0.35)
    m3n = arc_mid_from_centre((-2.485, 0.226), (-2.339, 0.358), (-2.496, 0.386), 0.16)
    m4n = arc_mid_from_centre((-2.256, 0.83), (-1.97, 1.07), (-1.97, 0.78), 0.29)

    for y_pos in y_positions:
        sk_plane = Plane(origin=(0, y_pos, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
        with BuildSketch(sk_plane):
            with BuildLine():
                Line((-1.95, 0.88), (-1.97, 0.88))
                ThreePointArc((-1.97, 0.88), m1n, (-2.068, 0.797))
                Line((-2.068, 0.797), (-2.152, 0.325))
                ThreePointArc((-2.152, 0.325), m2n, (-2.472, 0.037))
                Line((-2.472, 0.037), (-3.0, 0.0))
                Line((-3.0, 0.0), (-3.013, 0.19))
                Line((-3.013, 0.19), (-2.485, 0.226))
                ThreePointArc((-2.485, 0.226), m3n, (-2.339, 0.358))
                Line((-2.339, 0.358), (-2.256, 0.83))
                ThreePointArc((-2.256, 0.83), m4n, (-1.97, 1.07))
                Line((-1.97, 1.07), (-1.95, 1.07))
                Line((-1.95, 1.07), (-1.95, 0.88))
            make_face()
        extrude(amount=-0.41)

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_D0014A.stl")
