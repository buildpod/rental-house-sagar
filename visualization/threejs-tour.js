import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

export function initTour(containerId) {
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f2f5);
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / 600, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(window.innerWidth, 600);
    document.getElementById(containerId).appendChild(renderer.domElement);
    
    const controls = new OrbitControls(camera, renderer.domElement);
    camera.position.set(40, 30, 40);
    
    scene.add(new THREE.AmbientLight(0xffffff, 0.6));
    const dir = new THREE.DirectionalLight(0xffffff, 0.8);
    dir.position.set(10,20,10); scene.add(dir);
    
    // Simple Massing
    const gf = new THREE.Mesh(new THREE.BoxGeometry(30, 10, 50), new THREE.MeshStandardMaterial({color: 0x90caf9}));
    gf.position.y = 5; scene.add(gf);
    const ff = new THREE.Mesh(new THREE.BoxGeometry(30, 10, 50), new THREE.MeshStandardMaterial({color: 0xa5d6a7}));
    ff.position.y = 15; scene.add(ff);
    const sf = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 15), new THREE.MeshStandardMaterial({color: 0xffe082}));
    sf.position.set(-7.5, 25, 17.5); scene.add(sf); // Studio
    
    // Balcony
    const balc = new THREE.Mesh(new THREE.BoxGeometry(30, 1, 5), new THREE.MeshStandardMaterial({color: 0xeeeeee}));
    balc.position.set(0, 10, 27.5); scene.add(balc);
    
    function animate() { requestAnimationFrame(animate); controls.update(); renderer.render(scene, camera); }
    animate();
    return { camera, controls };
}
