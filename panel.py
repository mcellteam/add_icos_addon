import bpy
import random
import os


# register and unregister are required for Blender Addons
# We use per module class registration/unregistration

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


class MySceneSettings(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="Test Prop", default="Unknown")
    num_icos = bpy.props.IntProperty(name="Number of Icos", default=10)


class SceneAddIcos(bpy.types.Operator):
    """My Addon to Add Random Icospheres to Scene"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "scene.add_icos"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Random Icospheres"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        scene = context.scene
        # random.seed(a=1)

        for i in range(scene.my_settings.num_icos):
            x = 10*(random.random()-0.5)
            y = 10*(random.random()-0.5)
            z = 10*(random.random()-0.5)
            bpy.ops.mesh.primitive_ico_sphere_add(location=(x,y,z))


        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Tool Self"""
    bl_label = "Hello World Panel"
    bl_idname = "Scene_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Add Icos"
#    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        scene = context.scene

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.prop(scene.my_settings, "num_icos", text="number of icos")
        row = layout.row()
        row.operator("scene.add_icos")


