from build123d import *

# Part: XT60PW-M

with BuildPart() as part:
    # ---------------------------------------------------------
    # 1. Main Profile (XZ Plane, Y: 0.3 up to 8.4)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-0.3)):
        with BuildLine():
            profile_points = [
                (-7.75, 3.7), (-7.75, 0.5), (-7.0, 0.5), (-7.0, 0.75),
                (-6.5, 0.75), (-6.5, -0.75), (-7.0, -0.75), (-7.0, -0.5),
                (-7.75, -0.5), (-7.75, -10.35), (7.75, -10.35), (7.75, -0.5),
                (7.0, -0.5), (7.0, -0.75), (6.5, -0.75), (6.5, 0.75),
                (7.0, 0.75), (7.0, 0.5), (7.75, 0.5), (7.75, 3.7),
                (7.75, 4.35), (-7.75, 4.35)
            ]
            Polyline(profile_points, close=True)
        make_face()
    extrude(amount=-8.1)

    # ---------------------------------------------------------
    # 2. Corner Subtractions (XY Plane, Z: -10.35 to 4.35)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-10.35)):
        with BuildLine():
            Line((7.75, 7.4), (7.75, 8.4)) 
            Line((7.75, 8.4), (6.75, 8.4)) 
            CenterArc(center=(6.75, 7.4), radius=1.0, start_angle=90, arc_size=-90)
            Line((-7.75, 7.4), (-7.75, 8.4)) 
            Line((-7.75, 8.4), (-6.75, 8.4)) 
            CenterArc(center=(-6.75, 7.4), radius=1.0, start_angle=90, arc_size=90)
        make_face()
    extrude(amount=14.7, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 3. Hollow Subtractive Profile (XY Plane, Z: 3.7 to 3.75)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(3.7)):
        with BuildLine():
            Line((-7.75, 0.3), (-7.75, 7.4))
            CenterArc(center=(-6.75, 7.4), radius=1.0, start_angle=180, arc_size=-90)
            Line((-6.75, 8.4), (6.75, 8.4))
            CenterArc(center=(6.75, 7.4), radius=1.0, start_angle=90, arc_size=-90)
            Line((7.75, 7.4), (7.75, 0.3))
            Line((7.75, 0.3), (-7.75, 0.3))
        with BuildLine():
            Line((-7.65, 0.4), (-7.65, 7.4))
            CenterArc(center=(-6.75, 7.4), radius=0.9, start_angle=180, arc_size=-90)
            Line((-6.75, 8.3), (6.75, 8.3))
            CenterArc(center=(6.75, 7.4), radius=0.9, start_angle=90, arc_size=-90)
            Line((7.65, 7.4), (7.65, 0.4))
            Line((7.65, 0.4), (-7.65, 0.4))
        make_face()
    extrude(amount=0.05, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 4. Top Shell Additive Profile (XZ Plane, Y: 0.3 to 8.2)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-0.3)):
        with BuildLine():
            p1_4, p2_4, p3_4, p4_4, p5_4, p6_4 = (7.55, 4.35), (5.919, 7.45), (4.95, 7.85), (-4.95, 7.85), (-5.919, 7.45), (-7.55, 4.35)
            RadiusArc(p1_4, p2_4, -6.183)
            RadiusArc(p2_4, p3_4, -1.526)
            Line(p3_4, p4_4)
            RadiusArc(p4_4, p5_4, -1.526)
            RadiusArc(p5_4, p6_4, -6.183)
            Line(p6_4, p1_4)
        make_face()
    extrude(amount=-7.9)

    # ---------------------------------------------------------
    # 5. Small Additive Profile (XZ Plane, Y: 0.3 to 0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-0.3)):
        with BuildLine():
            p1_5, p2_5, p3_5, p4_5 = (5.919, 7.45), (4.95, 7.85), (-4.95, 7.85), (-5.919, 7.45)
            RadiusArc(p1_5, p2_5, -1.526) 
            Line(p2_5, p3_5)             
            RadiusArc(p3_5, p4_5, -1.526) 
            Line(p4_5, p1_5)             
        make_face()
    extrude(amount=0.3)

    # ---------------------------------------------------------
    # 6. Cutting Sweep (Manual Mode to avoid ValueError)
    # ---------------------------------------------------------
    # Path: Outer perimeter at Y=8.2
    shell_top_face = part.faces().filter_by(Axis.Y, 8.2).last
    path = shell_top_face.outer_wire()

    with BuildSketch(Plane.XY.offset(4.35)) as sweep_sketch:
        with BuildLine():
            p1_s, p2_s, p3_s = (7.55, 7.2), (7.55, 8.2), (6.539, 8.2)
            Line(p1_s, p2_s)
            Line(p2_s, p3_s)
            # Center (6.539, 7.189), connects p3 to p1
            CenterArc(center=(6.539, 7.189), radius=1.011, start_angle=90, arc_size=-90)
        make_face()
    
    # Use Mode.PRIVATE to stop the automatic (and failing) addition to BuildPart
    # Note: Transition must be ROUNDED (not ROUND)
    cutter = sweep(sweep_sketch.face(), path=path, transition=Transition.ROUND, mode=Mode.PRIVATE)
    
    # Convert Shell to Solid so it can be subtracted
    if isinstance(cutter, Shell):
        cutter = Solid.make_solid(cutter)
    
    # Manually subtract the solid
    add(cutter, mode=Mode.SUBTRACT)

if __name__ == "__main__":
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        part.part.export_step("XT60PW-M.step")