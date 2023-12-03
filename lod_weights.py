import bpy

class LOD_OT_Weights(bpy.types.Operator):
    bl_idname = "object.transfer_weights"
    bl_label = "Transfer Weights (Multiple Meshes)"

    def execute(self, context):

        source_mesh = bpy.context.active_object
        target_meshes = bpy.context.selected_objects[1:]

        for o in target_meshes:

            bpy.ops.object.select_all(action='DESELECT') #deselecting everything
            bpy.data.objects[o.name].select_set(True) #selecting target
            bpy.data.objects[source_mesh.name].select_set(True) #selecting source
            bpy.context.view_layer.objects.active = bpy.data.objects[o.name] #setting target as active

            bpy.ops.paint.weight_paint_toggle() #entering Weight Paint mode
            bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', layers_select_src='NAME', layers_select_dst='ALL') #transferring weights
            bpy.ops.paint.weight_paint_toggle() #exit Weight Paint Mode

        return {"FINISHED"}

# class LOD_MT_Menu(bpy.types.Menu):
#     bl_idname = 'object.mymenu'
#     bl_label = 'LOD Menu'

#     def draw(self, context):
#         layout = self.layout
#         layout.operator('object.generate', icon='OUTLINER_OB_MESH')