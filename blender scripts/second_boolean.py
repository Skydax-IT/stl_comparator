#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bpy
import sys

# Blender scripts that imports two .stl files into a blender scene
# Performs a boolean difference between the first and the second stl
# Exports the result

path1 = sys.argv[6]
path2 = sys.argv[7]
stl1 = sys.argv[8]
stl2 = sys.argv[9]
output_path = sys.argv[10]

def clean_scene():
    for mesh in bpy.data.meshes:
        print("Removing mesh", mesh.name)
        bpy.data.meshes.remove(mesh)

    for camera in bpy.data.cameras:
        print("Removing camera", camera.name)
        bpy.data.cameras.remove(camera)
    
    for light in bpy.data.lights:
        print("Removing light", light.name)
        bpy.data.lights.remove(light)

clean_scene()

bpy.ops.import_mesh.stl(filepath=path2)
bpy.ops.import_mesh.stl(filepath=path1)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[stl2]
bpy.ops.object.modifier_apply(modifier="Boolean")

bpy.ops.export_mesh.stl(filepath=f'{output_path}/bool_result_2.stl' ,check_existing=True, filter_glob=stl1, use_selection=True, global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True, batch_mode="OFF", axis_forward="Y", axis_up="Z")

# print(path1)
# print(path2)
# print(stl1)
# print(stl2)
# print("success")
