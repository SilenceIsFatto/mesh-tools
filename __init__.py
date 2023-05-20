bl_info = {
    "name" : "lodgenerator",
    "author" : "Silence",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

from . lod_op import LOD_OT_Generate
import bpy

def menu_item_draw_func(self, context):
    self.layout.separator()
    self.layout.operator('object.generate', icon='OUTLINER_OB_MESH')

def register():
    bpy.utils.register_class(LOD_OT_Generate)

    bpy.types.VIEW3D_MT_object_context_menu.append(menu_item_draw_func)

def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_item_draw_func)
    bpy.utils.unregister_class(LOD_OT_Generate)