import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Set up scene, camera, renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
const renderer = new THREE.WebGLRenderer({alpha: true});

renderer.setSize( window.innerWidth, window.innerHeight );
const controls = new OrbitControls( camera, renderer.domElement );
renderer.setClearColor(0xCEEFF3);
document.getElementById('container3d').appendChild( renderer.domElement );

// Create GLTFLoader instance
const loader = new GLTFLoader();

// Load GLTF model
loader.load( 'scene.gltf', function ( gltf ) { scene.add( gltf.scene ); }, undefined, 
function ( error ) { console.error( error ); } );

// Load GLB model
// loader.load( 'scene.glb', function ( gltf ) { scene.add( gltf.scene ); },undefined, 
// function ( error ) { console.error( error ); } );

// Position camera
// Position camera
camera.position.set(50, 50, 100);
scene.add(camera);
// camera.lookAt(scene.position);


// Add light
const topLight = new THREE.DirectionalLight(0xffffff, 5); // (color, intensity)
topLight.position.set(500, 500, 500) //top-left-ish
topLight.castShadow = true;
scene.add(topLight);

//texture render
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load('textures/HAND_C.jpg');


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