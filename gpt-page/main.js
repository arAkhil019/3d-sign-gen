import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Set up scene, camera, renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
const renderer = new THREE.WebGLRenderer();

renderer.setSize( window.innerWidth, window.innerHeight );
const controls = new OrbitControls( camera, renderer.domElement );
renderer.setClearColor(0xffffff);
document.body.appendChild( renderer.domElement );

// Create GLTFLoader instance
const loader = new GLTFLoader();

// Load GLB model
loader.load( 'scene.glb', function ( gltf ) { scene.add( gltf.scene ); },undefined, 
function ( error ) { console.error( error ); } );

// Position camera
// Position camera
camera.position.set(50, 50, 75);
// camera.lookAt(scene.position);

//texture render
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load('textures/HAND_C.jpg');

// loader.load('scene.glb', function (gltf) {
//     gltf.scene.traverse((node) => {
//         if (node.isMesh) {
//             node.material.map = texture; // Assign texture to the mesh's material
//             node.material.needsUpdate = true; // Ensure material updates
//         }
//     });
//     scene.add(gltf.scene);
// }, undefined, function (error) {
//     console.error(error);
// });
// Render loop
function animate() {
    requestAnimationFrame(animate);

    // const modelPos = scene.getObjectByName('Hand');
    // const distance = 75;

    // const camPos = modelPos.position.clone().add(new THREE.Vector3(0, 0, distance));
    // camera.lookAt(modelPos);
    // camera.position.lerp(camPos, 0.1);
    controls.update();
    renderer.render(scene, camera);
}

animate();