import bpy
import math

def set_bone_angle(armature_name, bone1_name, bone2_name, angle_degrees):
    # Select the armature object
    armature = bpy.data.objects[armature_name]
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Get the bones
    bone1 = armature.pose.bones[bone1_name]
    bone2 = armature.pose.bones[bone2_name]
    
    # Convert the angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Ensure bone2 is a child of bone1
    if bone2.parent != bone1:
        raise ValueError(f"{bone2_name} is not a child of {bone1_name}")

    # Get the current rotation mode to revert back after setting rotation
    current_rotation_mode_bone2 = bone2.rotation_mode
    
    # Set the rotation mode to 'XYZ' to manipulate the rotation in Euler angles
    bone2.rotation_mode = 'XYZ'
    
    # Rotate bone2 around its parent bone (bone1)
    bone2.rotation_euler.z += angle_radians
    
    # Restore the original rotation mode
    bone2.rotation_mode = current_rotation_mode_bone2
    
    # Update the pose
    bpy.context.view_layer.update()
    
    print(f"Bent {bone2_name} by {angle_degrees} degrees relative to {bone1_name}")

def set_bone_at(armature_obj, bone_name, angles):
    # Validate input parameters
    if not armature_obj or armature_obj.type != 'ARMATURE':
        print("Error: Invalid armature object.")
        return False
    
    # Switch to Pose Mode
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='POSE')
    
    # Get the pose bone
    pose_bone = armature_obj.pose.bones.get(bone_name)
    if not pose_bone:
        print(f"Error: Bone '{bone_name}' not found in armature '{armature_obj.name}'.")
        return False
    
    # Convert angles from degrees to radians
    angles_radians = [math.radians(angle) for angle in angles]
    
    # Apply rotations
    pose_bone.rotation_mode = 'XYZ'  # Adjust as necessary based on bone's rotation mode
    pose_bone.rotation_euler = angles_radians
    
    # Update the scene
    bpy.context.view_layer.update()
    
    return True
    
    
angles = {1: 46, 2: 21, 3: 8, 5: 10, 6: 2, 7: 2, 9: 8, 10: 6, 11: 3, 13: 17, 14: 138, 15: 13, 17: 29, 18: 130, 19: 10, 'xyz': (103, -1, -1), 'r': (4, -88, -88)}


j=1
for i in range(1,15,3):
    set_bone_angle("Armature.001", f"Bone0{i}.R", f"Bone{i}.R", angles[j])
    set_bone_angle("Armature.001", f"Bone{i}.R", f"Bone{i+1}.R", angles[j+1])
    set_bone_angle("Armature.001", f"Bone{i+1}.R", f"Bone{i+2}.R", angles[j+2])
    j+=4

armature_obj = bpy.data.objects.get('Armature.001')
set_bone_at(armature_obj, 'Bone', angles['xyz'])
set_bone_at(armature_obj, 'BoneR.R', angles['r'])