import bpy

class LOD_OT_Normals(bpy.types.Operator):
    bl_idname = "object.clear_normals"
    bl_label = "Clear Mesh Normal Data"

    def execute(self, context):

        object = bpy.context.selected_objects

        for o in object:
            bpy.context.view_layer.objects.active = o
            bpy.ops.mesh.customdata_custom_splitnormals_clear()

        return {"FINISHED"}

# class LOD_MT_Menu(bpy.types.Menu):
#     bl_idname = 'object.mymenu'
#     bl_label = 'LOD Menu'

#     def draw(self, context):
#         layout = self.layout
#         layout.operator('object.generate', icon='OUTLINER_OB_MESH')