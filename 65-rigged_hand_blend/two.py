import bpy
import bmesh

# Coordinates of the points
points = [
    (0.49660858511924744, 0.7461532354354858, 1.0917805184362805e-06),
    (0.42561307549476624, 0.6507793664932251, -0.023379279300570488),
    (0.35283204913139343, 0.5186304450035095, -0.06645891815423965),
    (0.29742521047592163, 0.4151679575443268, -0.10738563537597656),
    (0.23635946214199066, 0.353977769613266, -0.14200858771800995),
    (0.31368568539619446, 0.5305399298667908, -0.11221174150705338),
    (0.33975890278816223, 0.3401527404785156, -0.18388301134109497),
    (0.3569319248199463, 0.344044953584671, -0.22193937003612518),
    (0.35196512937545776, 0.38002756237983704, -0.23872022330760956),
    (0.3545425832271576, 0.5670217871665955, -0.12790557742118835),
    (0.3966732621192932, 0.30257028341293335, -0.19975249469280243),
    (0.4286328852176666, 0.15802344679832458, -0.22774337232112885),
    (0.4534105062484741, 0.05275419354438782, -0.24376936256885529),
    (0.4180983304977417, 0.5942768454551697, -0.139839306473732),
    (0.46997755765914917, 0.34552106261253357, -0.18719042837619781),
    (0.4804006814956665, 0.40303564071655273, -0.1563834846019745),
    (0.4707072973251343, 0.4874613285064697, -0.12786097824573517),
    (0.4846096634864807, 0.6044600009918213, -0.1544772982597351),
    (0.5227261781692505, 0.4148874878883362, -0.17477673292160034),
    (0.526402473449707, 0.46142762899398804, -0.14254483580589294),
    (0.511804461479187, 0.531866192817688, -0.11469347029924393)
]

## Clear existing objects (optional)
#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(type='MESH')
#bpy.ops.object.delete()

# Create spheres (points) at each coordinate with reduced radius
point_objects = []
for point in points:
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, location=point)
    point_object = bpy.context.object
    point_objects.append(point_object)

# Create a new mesh to hold the lines (edges)
mesh = bpy.data.meshes.new(name="LinesMesh")
obj = bpy.data.objects.new(name="LinesObject", object_data=mesh)
bpy.context.collection.objects.link(obj)

# Create a BMesh to add edges
bm = bmesh.new()

# Create vertices in BMesh
bm_verts = [bm.verts.new(point) for point in points]

# Create edges in BMesh
for i in range(len(points) - 1):
    bm.edges.new([bm_verts[i], bm_verts[i + 1]])

# Convert BMesh to mesh
bm.to_mesh(mesh)
bm.free()

# Optionally, set the viewport shading to Material Preview or Rendered for better visualization
#bpy.context.space_data.shading.type = 'MATERIAL'
