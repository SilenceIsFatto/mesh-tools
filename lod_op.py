import bpy

class LOD_OT_Generate(bpy.types.Operator):
    bl_idname = "object.generate"
    bl_label = "Generate LODs"

    name : bpy.props.StringProperty(name="Mesh Name", description="If left as is, current mesh name is used.", default="...")
    amount : bpy.props.IntProperty(name="Decimate Index", description="Decides how many LODs should be made.", default=4, min=1, max=100)
    ratio : bpy.props.FloatProperty(name="Decimate Ratio", description="Decides the ratio that the current LOD should be decimated by.", default=0.5, min=0.0, max=1.0)
    # folders : bpy.props.BoolProperty(name="Use Folders", description="Decides if each LOD is put into its own folder or not.", default=True)

    def invoke(self, context, event):

        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):

        object = bpy.context.active_object

        mesh_name = self.name
        mesh_amount = self.amount
        mesh_ratio = self.ratio
        # mesh_folders = self.folders

        if mesh_name == "...":
            mesh_name = object.name

        def copy(object, index, use_folders=False):
            
            active_obj = object.copy()
            active_obj.data = object.data.copy()

            new_name = mesh_name + "_" + str(index)
            active_obj.name = new_name

            # if (use_folders):
            new_collection = bpy.data.collections.new(new_name)
            bpy.context.scene.collection.children.link(new_collection)
            new_collection.objects.link(active_obj)
            
            if (index != 0):
            
                decimate(active_obj, ratio=mesh_ratio)

            bpy.context.view_layer.objects.active = active_obj

            return active_obj

        def decimate(object, ratio=0.5):

            mod = object.modifiers.new("Decimate", "DECIMATE")
            mod.ratio = mesh_ratio
            
            apply_modifiers(object)
            
        def apply_modifiers(o):
            #credit to https://blenderartists.org/t/how-to-copy-object-mesh-with-all-modifiers-applied/1390327/5
            c = bpy.context.copy()
            c["object"] = o
            for _, m in enumerate(o.modifiers):
                c["modifier"] = m
                bpy.ops.object.modifier_apply(c, modifier=m.name)

        for i in range(mesh_amount):
            
            active = bpy.context.active_object
            
            copy(active, i)

        return {"FINISHED"}