import * as THREE from 'https://unpkg.com/three@0.160.0/build/three.module.js';

export function initTour(containerId, scenes) {
  const container = document.getElementById(containerId);
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xe4e7e1);
  scene.fog = new THREE.Fog(0xe4e7e1, 72, 170);

  const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.shadowMap.enabled = true;
  container.appendChild(renderer.domElement);

  const target = new THREE.Vector3(0, 12, 12);
  const desiredCamera = new THREE.Vector3(40, 24, 72);
  const desiredTarget = new THREE.Vector3(0, 12, 18);

  const materials = {
    plot: new THREE.MeshStandardMaterial({ color: 0xf5f0e7, roughness: .82 }),
    road: new THREE.MeshStandardMaterial({ color: 0xb9b3aa, roughness: .9 }),
    wall: new THREE.MeshStandardMaterial({ color: 0xf7f2ea, roughness: .7 }),
    accent: new THREE.MeshStandardMaterial({ color: 0xb75f3b, roughness: .72 }),
    green: new THREE.MeshStandardMaterial({ color: 0x426b54, roughness: .75 }),
    blue: new THREE.MeshStandardMaterial({ color: 0x275f7b, roughness: .62 }),
    glass: new THREE.MeshStandardMaterial({ color: 0xcfe7ea, metalness: .05, roughness: .25, transparent: true, opacity: .68 }),
    parking: new THREE.MeshStandardMaterial({ color: 0x2f3d40, roughness: .55 }),
    service: new THREE.MeshStandardMaterial({ color: 0xb7872f, roughness: .7 }),
    terrace: new THREE.MeshStandardMaterial({ color: 0xe0d8ca, roughness: .88 }),
    unitA: new THREE.MeshStandardMaterial({ color: 0xfff7e8, roughness: .78 }),
    unitB: new THREE.MeshStandardMaterial({ color: 0xeef4ef, roughness: .78 }),
    unitC: new THREE.MeshStandardMaterial({ color: 0xe9f2f5, roughness: .78 })
  };

  const labelCanvas = document.createElement('canvas');
  const labelContext = labelCanvas.getContext('2d');

  function box(name, size, position, material, cast = true) {
    const mesh = new THREE.Mesh(new THREE.BoxGeometry(size[0], size[1], size[2]), material);
    mesh.name = name;
    mesh.position.set(position[0], position[1], position[2]);
    mesh.castShadow = cast;
    mesh.receiveShadow = true;
    scene.add(mesh);
    return mesh;
  }

  function label(text, position) {
    labelCanvas.width = 512;
    labelCanvas.height = 128;
    labelContext.clearRect(0, 0, 512, 128);
    labelContext.fillStyle = 'rgba(255,253,248,.92)';
    labelContext.fillRect(0, 0, 512, 128);
    labelContext.strokeStyle = '#d8d2c8';
    labelContext.strokeRect(2, 2, 508, 124);
    labelContext.fillStyle = '#222';
    labelContext.font = '700 34px Arial';
    labelContext.textAlign = 'center';
    labelContext.textBaseline = 'middle';
    labelContext.fillText(text, 256, 64);
    const texture = new THREE.CanvasTexture(labelCanvas);
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: texture, transparent: true }));
    sprite.scale.set(10, 2.5, 1);
    sprite.position.set(position[0], position[1], position[2]);
    scene.add(sprite);
    return sprite;
  }

  box('30 x 50 plot', [30, .35, 50], [0, -.2, 0], materials.plot, false);
  box('30 ft road', [42, .28, 16], [0, -.25, 35], materials.road, false);
  label('30 ft Road - East', [0, 1.5, 40]);

  box('ground floor mass', [30, 9, 50], [0, 4.5, 0], materials.wall);
  box('first floor mass', [30, 9, 50], [0, 13.8, 0], materials.unitB);
  box('second floor studio', [15, 8, 15], [-7.5, 23.5, -8], materials.unitC);
  box('stair mumty', [9, 11, 10], [10, 25, -18], materials.terrace);

  box('front facade frame', [31, 27, .8], [0, 13.5, 25.4], materials.wall);
  box('parking opening', [12, 5.6, 1.1], [-7, 3.2, 26.1], materials.parking);
  box('entry door', [4, 6, 1.2], [5, 3, 26.25], materials.green);
  box('meter wall', [3.5, 5, 1.3], [11.5, 3, 26.35], materials.service);
  box('balcony slab', [30, .8, 5], [0, 14.6, 29], materials.terrace);
  box('balcony rail', [30, 2.6, .45], [0, 16.4, 31.2], materials.glass);
  box('horizontal clay band', [29, 1.2, 1], [0, 18.8, 26.4], materials.accent);
  box('top blue canopy', [15, 1.1, 1.2], [-7, 27.6, 26.6], materials.blue);
  box('gold fin wall', [5, 25, 1.4], [11.5, 14, 26.8], materials.service);

  box('front window 1', [7, 3.5, 1.4], [-8, 22, 26.8], materials.glass);
  box('front window 2', [7, 3.5, 1.4], [2, 22, 26.8], materials.glass);
  box('front window 3', [6, 3.2, 1.4], [7, 12, 26.8], materials.glass);

  box('SUV bay', [11, .45, 17], [-7, .2, 16], materials.parking, false);
  box('bike parking', [7, .5, 4], [8, .25, 18], materials.service, false);
  box('UG sump', [4, .7, 4], [10, .35, 23], materials.blue, false);

  box('GF living', [10, 1.1, 18], [-5, 9.8, 4], materials.unitA, false);
  box('GF kitchen', [15, 1.1, 12], [-2.5, 9.9, -16], materials.accent, false);
  box('GF bedrooms', [15, 1.1, 24], [-7.5, 10, -3], materials.unitC, false);
  box('common stair', [8, 25, 12], [10, 12.5, -18], materials.green);
  box('wet shaft 1', [4, 18, 5], [-13, 9, 0], materials.blue);
  box('wet shaft 2', [5, 18, 5], [-4, 9, -22], materials.blue);

  box('1BHK zone', [18, 1.1, 24], [-6, 19, -4], materials.unitA, false);
  box('single room zone', [16, 1.1, 17], [6, 19.1, 5], materials.unitC, false);
  box('utility strip', [5, 1, 18], [12.5, 19.2, 8], materials.service, false);

  box('open terrace', [30, .55, 50], [0, 27.8, 0], materials.terrace, false);
  box('drying zone', [9, .7, 13], [-9, 28.5, 12], materials.green, false);
  box('overhead tank', [5, 5, 5], [8, 32, -20], materials.blue);
  label('OHT', [8, 36.5, -20]);

  const ambient = new THREE.HemisphereLight(0xffffff, 0xb7a991, 1.2);
  scene.add(ambient);
  const sun = new THREE.DirectionalLight(0xfff4df, 2.2);
  sun.position.set(35, 60, 45);
  sun.castShadow = true;
  sun.shadow.mapSize.width = 2048;
  sun.shadow.mapSize.height = 2048;
  scene.add(sun);

  const fill = new THREE.DirectionalLight(0xbfd8ff, .75);
  fill.position.set(-35, 28, -30);
  scene.add(fill);

  function resize() {
    const width = container.clientWidth || window.innerWidth;
    const height = container.clientHeight || window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }

  window.addEventListener('resize', resize);
  resize();

  function goToScene(id) {
    const selected = scenes.find((sceneData) => sceneData.id === id) || scenes[0];
    desiredCamera.fromArray(selected.cameraPosition);
    desiredTarget.fromArray(selected.target);
  }

  let angle = 0;
  let dragging = false;
  let lastX = 0;

  renderer.domElement.addEventListener('pointerdown', (event) => {
    dragging = true;
    lastX = event.clientX;
  });
  renderer.domElement.addEventListener('pointerup', () => { dragging = false; });
  renderer.domElement.addEventListener('pointerleave', () => { dragging = false; });
  renderer.domElement.addEventListener('pointermove', (event) => {
    if (!dragging) return;
    angle += (event.clientX - lastX) * 0.004;
    lastX = event.clientX;
  });

  function animate() {
    requestAnimationFrame(animate);
    camera.position.lerp(desiredCamera, .06);
    target.lerp(desiredTarget, .06);
    if (!dragging) angle += .0012;
    const radius = camera.position.distanceTo(target);
    const orbitOffset = new THREE.Vector3(Math.sin(angle) * .12 * radius, 0, Math.cos(angle) * .12 * radius);
    camera.lookAt(target.clone().add(orbitOffset.multiplyScalar(.08)));
    renderer.render(scene, camera);
  }

  animate();
  goToScene(scenes[0]?.id);

  return { camera, scene, renderer, goToScene };
}
