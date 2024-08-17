import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { STLLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/STLLoader.js";

// Inicialização do cenário Three.js
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true; // Habilitar sombras no renderer
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // Tipo de sombra
document.getElementById("COPO").appendChild(renderer.domElement);

let controls = new OrbitControls(camera, renderer.domElement);

function criarLuzDirecional(posicao) {
    const luz = new THREE.DirectionalLight(0x383838, 1);
    luz.position.copy(posicao);
    luz.castShadow = true; // Permitir que a luz gere sombras

    // Configurar as propriedades da sombra
    luz.shadow.mapSize.width = 1024;
    luz.shadow.mapSize.height = 1024;
    luz.shadow.camera.near = 0.5;
    luz.shadow.camera.far = 500;

    scene.add(luz);
}

// Adicionar luzes direcionais
const direcoesLuzes = [
    new THREE.Vector3(2, 2, 2),
    new THREE.Vector3(2, 2, -2),
    new THREE.Vector3(-2, 2, 2),
    new THREE.Vector3(-2, 2, -2),
    new THREE.Vector3(2, 0, 2),
    new THREE.Vector3(2, 0, -2),
    new THREE.Vector3(-2, 0, 2),
    new THREE.Vector3(-2, 0, -2),
    new THREE.Vector3(2, -2, 2),
    new THREE.Vector3(2, -2, -2),
    new THREE.Vector3(-2, -2, 2),
    new THREE.Vector3(-2, -2, -2)
];

direcoesLuzes.forEach(posicao => criarLuzDirecional(posicao));

const loader = new STLLoader();
let object;

loader.load(
    'models/CUP3D/scene.stl',
    function (geometry) {
        
        const material = new THREE.MeshStandardMaterial({ color: 0xffffff }); // Cor branca
        object = new THREE.Mesh(geometry, material);

        // Ajustar a escala do objeto para que ele fique maior
        object.scale.set(0.00315, 0.00315, 0.00315);

        // Ajustar a posição do objeto para ficar no topo da página
        object.position.set(10, 10, 60);

        // Permitir que o objeto projete e receba sombras
        object.castShadow = true;
        object.receiveShadow = true;

        // Adicionar o modelo à cena
        scene.add(object);

        // Ajustar a posição da câmera
        const caixaLimitadora = new THREE.Box3().setFromObject(object);
        const centro = new THREE.Vector3();
        caixaLimitadora.getCenter(centro);
        controls.target.copy(centro);
        camera.position.set(centro.x + 10, centro.y + 10, centro.z + 10);
    },
    function (xhr) {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    },
    function (error) {
        console.error('Erro ao carregar o modelo STL:', error);
    }
);

// Criar um plano para receber as sombras
const planeGeometry = new THREE.PlaneGeometry(200, 200);
const planeMaterial = new THREE.ShadowMaterial({ opacity: 0.4 });
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -Math.PI / 2;
plane.position.y = 0; // Ajuste conforme necessário
plane.receiveShadow = true;
scene.add(plane);

// Função de animação
function animate() {
    requestAnimationFrame(animate);

    if (object) {
        object.rotation.y += 0.01; // Rotação automática do objeto
    }

    controls.update();
    renderer.render(scene, camera);
}

// Configurar controles de zoom
controls.enableZoom = true;
controls.zoomSpeed = 1.2;

window.addEventListener("resize", function () {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

animate();
