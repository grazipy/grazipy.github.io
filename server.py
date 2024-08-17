from flask import Flask, request, jsonify
import os
import zipfile
import subprocess

app = Flask(__name__)

def convert_fbx_to_glb(input_fbx_path, output_glb_path):
    try:
        subprocess.run([
            "assimp", "export", input_fbx_path, output_glb_path, "-f", "glb"
        ], check=True)
        return f"Conversão concluída: {input_fbx_path} -> {output_glb_path}"
    except subprocess.CalledProcessError as e:
        return f"Erro ao converter FBX para GLB: {e}"

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return f"Arquivo ZIP extraído: {zip_path} -> {extract_to}"
    except Exception as e:
        return f"Erro ao extrair ZIP: {e}"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    output_dir = os.path.join('outputs', os.path.splitext(file.filename)[0])
    os.makedirs(output_dir, exist_ok=True)

    result = ""
    if file.filename.lower().endswith('.fbx'):
        output_glb_path = os.path.join(output_dir, os.path.splitext(file.filename)[0] + ".glb")
        result = convert_fbx_to_glb(file_path, output_glb_path)
    elif file.filename.lower().endswith('.zip'):
        result = extract_zip(file_path, output_dir)
        for root, _, files in os.walk(output_dir):
            for file in files:
                if file.lower().endswith('.fbx'):
                    input_fbx_path = os.path.join(root, file)
                    output_glb_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".glb")
                    result = convert_fbx_to_glb(input_fbx_path, output_glb_path)

    return jsonify({'message': result}), 200

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    app.run(debug=True)
