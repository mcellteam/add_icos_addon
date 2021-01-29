bl_info = {
    "name": "Add Random Icos",
    "blender": (2, 79, 0),
    "category": "Scene",
}


import bpy
import random
import os

if "panel" not in locals():
    print("Importing Add Icos Addon")
    from . import panel
else:
    print("Reloading Add Icos Addon")
    import imp
    imp.reload(panel)

'''
if "bpy" in locals():
    print("Reloading Add Icos Addon")
    import imp
    imp.reload(panel)
else:
    print("Importing Add Icos Addon")
    from . import \
        panel
'''


def register():
    # register all of the components of the Addon
    bpy.utils.register_module(__name__)
    bpy.types.Scene.my_settings = bpy.props.PointerProperty(type=panel.MySceneSettings)
    bpy.types.Object.my_obj_props = bpy.props.PointerProperty(type=panel.MyObjectProperties)
    print("Add Icos Addon registered")


def unregister():
    # register all of the components of the Addon
    bpy.utils.unregister_module(__name__)
    print("Add Icos Addon unregistered")


if __name__ == "__main__":
    bin_dir = os.path.join(os.path.dirname(__file__), 'bin')  # joins strings with path sep, "/" or "\"   
    recon2obj_bin = os.path.join(bin_dir,'recon2obj')
    print(bin_dir)
    print(recon2obj_bin)

    register()
