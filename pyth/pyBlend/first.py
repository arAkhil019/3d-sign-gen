import bpy

# Specify the path to your Blender file using raw string literal
blend_file_path = r'D:\code here♥d-sign-gen5-rigged_hand_blend\Rigged Hand 2.blend'

def load_blend_file(blend_path):
    try:
        with bpy.data.libraries.load(blend_path) as (data_from, data_to):
            data_to.objects = data_from.objects
            
        # Link objects to current scene
        for obj in data_to.objects:
            bpy.context.collection.objects.link(obj)  # or bpy.context.scene.collection.objects.link(obj)
            
        # Set the first object as the active object (change this based on your loaded objects)
        if data_to.objects:
            bpy.context.view_layer.objects.active = data_to.objects[0]

    except OSError as e:
        print(f"OSError: load: {blend_path} failed to open blend file")
        print(f"Error details: {e}")

def apply_pose():
    # Your pose scripting logic here
    pass  # Placeholder for actual pose scripting code

if __name__ == "__main__":
    load_blend_file(blend_file_path)
    apply_pose()

    # Optional: Manually interact with the viewport to refresh display
    # Example: Rotate the view by 90 degrees
    bpy.ops.view3d.view_axis(type='TOP', align_active=True)

    # Optional: Render the scene or perform other operations
    bpy.ops.render.render(write_still=True)
