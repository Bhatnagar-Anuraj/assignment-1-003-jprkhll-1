"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds
import random   #for random building heights

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=2,
    subdivisionsY=2,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
# building 1 -- simple massing for a surrounding building
building_width = 4
building_height = 10
building_depth = 4
building_x = -15
building_z = 2

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height/2, building_z, building)

# ---------------------------------------------------------------------------
# DONE: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
# building 2 -- a condo building angled 45 degrees
building2_width = 8
building2_height = 12
building2_depth = 5
building2_x = -17
building2_z = -5

building2 = cmds.polyCube(
    name="penthouse",
    width=building2_width,
    height=building2_height,
    depth=building2_depth,
)[0]

cmds.move(building2_x, building2_height/2.0, building2_z, building2)
cmds.rotate(0, 45, 0, building2)
# ---------------------------------------------------------------------------
# DONE: Add Object 3
# ---------------------------------------------------------------------------
# Sun object -- sphere representing light source (done)
sun_x = 10
sun_y = 20
sun_z = 15

sun = cmds.polySphere(
    name="sun",
    radius=1,
    subdivisionsX=20,
    subdivisionsY=20,
)[0]

cmds.move(sun_x, sun_y, sun_z, sun)

# ---------------------------------------------------------------------------
# DONE: Add Object 4
# ---------------------------------------------------------------------------
# Rittenhouse Square

park_width=20
park_height=0.3
park_depth=20
park_x=0
park_z=0

park = cmds.polyCube(
    name="sidewalk",
    width=park_width,
    depth=park_depth,
    height=park_height,
)[0]
#bevel for rounded sidewalk edges

cmds.move(park_x, park_height/2.0, park_z, park)
# ---------------------------------------------------------------------------
# DONE: Add Object 5
# ---------------------------------------------------------------------------
# Cylindrical guard tower at the center of park

tower_width = 1
tower_height = 1.5
tower_depth = 1
tower_x = 0
tower_z = 0

tower = cmds.polyCylinder(
    name="guard_tower",
    radius=0.5,
    height=tower_height,
    subdivisionsX=15,
    subdivisionsY=15,
    subdivisionsZ=15,
)[0]
cmds.move(tower_x, tower_height/2.0, tower_z, tower)
# ---------------------------------------------------------------------------
# DONE (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------
# Additional building masses with random heights to generate different skyline visability, although currently matching value heights for simplicity
massingheight=random.randint(6,12)
massingheightb=random.randint(3,9)

building3 = cmds.polyCube(
    name="building_03",
    width=2,
    height=massingheight,
    depth=5,
)[0]

building4 = cmds.polyCube(
    name="building_04",
    width=2,
    height=massingheight,
    depth=5,
)[0]
building5 = cmds.polyCube(
    name="building_05",
    width=2,
    height=massingheight,
    depth=5,
)[0]
building6 = cmds.polyCube(
    name="building_06",
    width=5,
    height=massingheight,
    depth=2,
)[0]
building7 = cmds.polyCube(
    name="building_07",
    width=5,
    height=massingheight,
    depth=2,
)[0]
building8 = cmds.polyCube(
    name="building_08",
    width=2,
    height=massingheight,
    depth=5,
)[0]
building9 = cmds.polyCube(
    name="building_09",
    width=2,
    height=massingheight,
    depth=5,
)[0]
building10 = cmds.polyCube(
    name="building_10",
    width=2,
    height=massingheight,
    depth=5,
)[0]
building11 = cmds.polyCube(
    name="building_11",
    width=5,
    height=massingheightb,
    depth=2,
)[0]
building12 = cmds.polyCube(
    name="building_12",
    width=5,
    height=massingheight,
    depth=2,
)[0]
building13 = cmds.polyCube(
    name="building_13",
    width=5,
    height=massingheight,
    depth=2,
)[0]
building14 = cmds.polyCube(
    name="building_14",
    width=4,
    height=massingheightb,
    depth=2,
)[0]

cmds.move(-10, massingheight/2.0, 15, building3)
cmds.move(-6, massingheight/2.0, 15, building4)
cmds.move(-2, massingheight/2.0, 15, building5)
cmds.move(1, massingheight/2.0, 15, building6)
cmds.move(7.5, massingheight/2.0, 15, building7)
cmds.move(13, massingheight/2.0, 7.5, building8)
cmds.move(13, massingheight/2.0, 0, building9)
cmds.move(13, massingheight/2.0, -7.5, building10)
cmds.move(7.5, massingheightb/2.0, -13, building11)
cmds.move(0, massingheight/2.0, -13, building12)
cmds.move(-7.5, massingheight/2.0, -13, building13)
cmds.move(-15, massingheightb/2.0, 8, building14)
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
