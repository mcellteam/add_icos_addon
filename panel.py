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
    active_index = bpy.props.IntProperty(name="Active Index", default=0)

class MyObjectProperties(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="Test Obj Prop", default="Unknown")
    value1 = bpy.props.FloatProperty(name="Value 1", default=0)
    value2 = bpy.props.FloatProperty(name="Value 2", default=0)

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
            obj = context.active_object
            obj.my_obj_props.value1 = random.random()
            obj.my_obj_props.value2 = random.random()

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


class MY_UL_obj_draw_item(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):
        scn = bpy.context.scene
        layout.label(item.name)

        '''
        filt = scn.test_tool.spine_namestruct_name.replace('#','[0-9]')
        self.filter_name = filt
        self.use_filter_sort_alpha = True
        if item.processor.newton == True:
            layout.label(item.name, icon='FILE_TICK')
        elif item.processor.smoothed == True:
            layout.label(item.name, icon='MOD_SMOOTH')
        else:
            layout.label(item.name)
        '''


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

        if obj != None:
          row = layout.row()
          row.label(text=obj.name, icon='WORLD_DATA')
          row = layout.row()
          row.prop(obj.my_obj_props, "value1", text="Value 1")

        '''
         row.template_list("MY_UL_obj_draw_item","objects_in_scene",
                          bpy.context.scene, "objects",
                          self, "active_index",
                          rows=2)
        '''



