import bpy

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Define vertices of the box
vertices = [
    (0, 0, 0),
    (100, 0, 0),
    (100, 100, 0),
    (0, 100, 0),
    (0, 0, 100),
    (100, 0, 100),
    (100, 100, 100),
    (0, 100, 100)
]

# Define edges (pairs of vertices)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges connecting bottom to top
]

# Create new mesh and object
mesh = bpy.data.meshes.new("BoxMesh")
obj = bpy.data.objects.new("BoxObject", mesh)

# Set mesh location and scene context
obj.location = bpy.context.scene.cursor.location
bpy.context.scene.collection.objects.link(obj)

# Create vertices
mesh.from_pydata(vertices, [], [])

# Update mesh geometry
mesh.update()

# Create edges
for v1, v2 in edges:
    mesh.edges.add(1)
    mesh.edges[-1].vertices[0] = v1
    mesh.edges[-1].vertices[1] = v2

# Set object to be selected and active
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
