import bpy
import mathutils
import math
import random

def update_camera(camera, x, y, z, focus_point=mathutils.Vector((0.0, 0.0, 0.0)), distance=10.0):
    """
    Focus the camera to a focus point and place the camera at a specific distance from that
    focus point. The camera stays in a direct line with the focus point.

    :param camera: the camera object
    :type camera: bpy.types.object
    :param focus_point: the point to focus on (default=``mathutils.Vector((0.0, 0.0, 0.0))``)
    :type focus_point: mathutils.Vector
    :param distance: the distance to keep to the focus point (default=``10.0``)
    :type distance: float
    """
    camera.location[0] = x
    camera.location[1] = y
    camera.location[2] = z
    looking_direction = camera.location - focus_point
    rot_quat = looking_direction.to_track_quat('Z', 'Y')

    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat * mathutils.Vector((0.0, 0.0, distance))


def calcPosition(center, distance, parts, step):
    radians = math.radians(360/parts * step)
    x = distance * math.cos(radians) + center[0]
    y = distance * math.sin(radians) + center[1]
    z = random.random() * distance - distance/2
    return (x,y,z)

cam = bpy.data.objects['Camera']

step_count = 4

for step in range(0, step_count):
    print(round((step+1)/step_count*100,2), '%')
    positions = calcPosition((0,0), 10, step_count, step)
    update_camera(bpy.data.objects['Camera'], positions[0], positions[1], positions[2])
    
    bpy.context.scene.render.image_settings.file_format='JPEG'
    bpy.context.scene.render.filepath = "/home/jaroslaw/Downloads/Pictures/elf_warrior_%d.jpg"%step

    bpy.ops.render.render( write_still=True )
