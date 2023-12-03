bl_info = {
    "name" : "Mesh Utilities",
    "author" : "Silence",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

from . lod_op import LOD_OT_Generate
from . lod_normals import LOD_OT_Normals
from . lod_weights import LOD_OT_Weights
import bpy

class LOD_MT_Menu(bpy.types.Menu):
    bl_idname = 'object.mymenu'
    bl_label = 'Mesh Utilities'

    def draw(self, context):
        layout = self.layout
        layout.operator('object.generate', icon='OUTLINER_OB_MESH')
        layout.operator('object.clear_normals', icon='OUTLINER_OB_MESH')
        layout.operator('object.transfer_weights', icon='OUTLINER_OB_MESH')

def menu_item_draw_func(self, context):
    self.layout.separator()
    # self.layout.operator('object.generate', icon='OUTLINER_OB_MESH')
    self.layout.menu(LOD_MT_Menu.bl_idname, icon='OUTLINER_OB_MESH')

def register():
    bpy.utils.register_class(LOD_OT_Generate)
    bpy.utils.register_class(LOD_OT_Normals)
    bpy.utils.register_class(LOD_OT_Weights)
    bpy.utils.register_class(LOD_MT_Menu)

    bpy.types.VIEW3D_MT_object_context_menu.append(menu_item_draw_func)

def unregister():
    bpy.utils.unregister_class(LOD_OT_Generate)
    bpy.utils.unregister_class(LOD_OT_Normals)
    bpy.utils.unregister_class(LOD_OT_Weights)
    bpy.utils.unregister_class(LOD_MT_Menu)

    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_item_draw_func)