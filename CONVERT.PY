import aspose.threed as a3d
import os

# Lista com os caminhos dos arquivos FBX
fbx_files = [
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-99+(2) (1).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (1).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (3).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (4).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (5).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (6).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (7).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (8).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-65 (2) (9).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-77 3.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-79 (4).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-79 (8).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-79 (9).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-79 (10).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-93 (1) (1).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-93 (1) (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-93 (1) (3).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-93 (1) (4).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-93 (1) (5).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-94 (1) (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-94 (1) (4).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-94 (1).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-94+Divã (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 1.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 2.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 3.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 4.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 5.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 6.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 7.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 8.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 9.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-96 10.fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-97 (1) (1).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-97 (1) (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-97 (1) (3).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-97 (1) (5).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-99+(2) (1) (1.).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-99+(2) (1) (2).fbx",
    r"C:\Users\grazi\Downloads\S-90 (2) 16\S-99+(2) (1) (2.).fbx"
]

# Diretório de saída para os arquivos GLB
output_dir = r"C:\Users\grazi\Downloads\S-90 (2) 16\Converted"

# Criar o diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Loop para converter cada arquivo FBX para GLB
for fbx_file in fbx_files:
    # Nome do arquivo sem extensão
    file_name = os.path.splitext(os.path.basename(fbx_file))[0]
    
    # Caminho de saída para o arquivo GLB
    output_glb = os.path.join(output_dir, file_name + ".glb")
    
    # Carregar o arquivo FBX
    scene = a3d.Scene.from_file(fbx_file)
    
    # Criar instância das opções de salvamento para GLB
    save_options = a3d.GLTFSaveOptions()
    save_options.file_format = a3d.FileFormat.GLB
    
    # Converter e salvar como GLB
    scene.save(output_glb, save_options)
    
    print(f"Arquivo {output_glb} criado com sucesso!")

print("Conversão completa para todos os arquivos!")
16:47 16/08/2024