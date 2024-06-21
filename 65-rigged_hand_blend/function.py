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

def poseHand(hand,angles):
    order = [1,2,3,5,6,7,9,10,11,13,14,15,17,18,19,'x','y','z','rx','ry','rz','x0','y0']
    if hand == 'R':
        arm = "Armature.001"
    else:
        arm = "Armature"
    j=0
    for i in range(1,15,3):
        set_bone_angle(arm, f"Bone0{i}.R", f"Bone{i}.R", angles[j])
        set_bone_angle(arm, f"Bone{i}.R", f"Bone{i+1}.R", angles[j+1])
        set_bone_angle(arm, f"Bone{i+1}.R", f"Bone{i+2}.R", angles[j+2])
        j+=3
    armature_obj = bpy.data.objects.get(arm)
    set_bone_at(armature_obj, 'Bone', tuple(angles[15:18]))
    set_bone_at(armature_obj, 'BoneR.R', tuple(angles[18:21]))
    move_bone = armature_obj.pose.bones["Bone07.R"]
    move_bone.location = tuple(angles[21:23]+[0])

input = [10, 2, 11, 76, 95, 17, 86, 81, 18, 61, 98, 17, 8, 17, 7, 79, 1, 1, -3, -77, -77, 67, 72, 26, 31, 34, 23, 147, 3, 21, 156, 15, 19, 164, 23, 17, 169, 15, 104, 1, 1, 38, -83, -83, 20, 65]

poseHand('L',input[:23])
poseHand('R',input[23:])