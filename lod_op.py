import bpy

class LOD_OT_Generate(bpy.types.Operator):
    bl_idname = "object.generate"
    bl_label = "Generate LODs'"
            
    #bpy.context.active_object.name = "0"

    def execute(self, context):

        def copy(object, index):
            
            active_obj = object.copy()
            
            active_obj.data = object.data.copy()
            
            if (active_obj.name != "0"):
            
                decimate(active_obj)
            
            new_collection = bpy.data.collections.new(str(index))
            bpy.context.scene.collection.children.link(new_collection)
            
            new_collection.objects.link(active_obj)
            
            active_obj.name = str(index)
            
            bpy.context.view_layer.objects.active = active_obj

        def decimate(object):
            
            active = object

            mod = active.modifiers.new("Decimate", "DECIMATE")

            mod.ratio = 0.5

        #    bpy.ops.object.modifier_apply(modifier="Decimate")
            
            apply_modifiers(active)
            
        def apply_modifiers(o):
            #credit to https://blenderartists.org/t/how-to-copy-object-mesh-with-all-modifiers-applied/1390327/5
            c = bpy.context.copy()
            c["object"] = o
            for _, m in enumerate(o.modifiers):
                c["modifier"] = m
                bpy.ops.object.modifier_apply(c, modifier=m.name)

        for i in range(4):
        
            active = bpy.context.active_object
            
            copy(active, i)

        return {"FINISHED"}