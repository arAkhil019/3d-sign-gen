import bpy
import math
import sys

# Select the armature
print(bpy.data)
armature = bpy.data.objects['Armature']  # Name of the armature

# Ensure the armature is in pose mode
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Access a specific bone in pose mode
pose_bone = armature.pose.bones # Name of the bone

b1 = "Bone"
b2 = "Bone001"
b3 = "Bone002"
a = 60
desired_angle = math.radians(60)
parent_bone = armature.pose.bones.get('Bone')  # Name of the parent bone
child_bone1 = armature.pose.bones.get('Bone001')  # Name of the first child bone
child_bone2 = armature.pose.bones.get('Bone002')  # Name of the second child bone

print(parent_bone,child_bone1,child_bone2)
initial_angle1 = parent_bone.matrix.to_3x3().inverted().normalized().to_euler()[0] - child_bone1.matrix.to_3x3().inverted().normalized().to_euler()[0]
initial_angle2 = parent_bone.matrix.to_3x3().inverted().normalized().to_euler()[0] - child_bone2.matrix.to_3x3().inverted().normalized().to_euler()[0]
    
angle_diff1 = initial_angle1 - desired_angle
angle_diff2 = initial_angle2 - desired_angle
    
child_bone1.rotation_euler[0] -= angle_diff1
child_bone2.rotation_euler[0] -= angle_diff2
bpy.context.view_layer.update()
    
angles = {2: 10.35, 3: 3.69, 6: 0.83, 7: 1.14, 10: 2.57, 11: 1.6, 14: 27.56, 15: 5.32, 18: 51.26, 19: 4.93}


# Calculate the initial angles between the parent and child bones

# Calculate the difference in angles


# Apply the difference to rotate the child bones


#assign_marks = {'001':lm[1],'004':lm[5],'007':lm[9],'010':lm[13],'013':lm[17]}
#for bone_num in assign_marks.keys():
#    bone_name = "Bone"+str(bone_num)
#    pose_bone = armature.pose.bones[bone_name]
#    lms = assign_marks[bone_num]
#    pose_bone.location = (lms[0],lms[1],lms[2])
 # Example coordinates

# Update the scene to apply the changes

