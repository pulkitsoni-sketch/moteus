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

from ocp_vscode import show
show(part)

# Export STL
export_stl(part.part, "output_D0014A.stl")