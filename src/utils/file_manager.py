import os

def create_file_with_content(file_path, content): 
  """
    Cria um arquivo no caminho especificado e escreve o conteúdo fornecido.
    Se o arquivo já existir, ele será sobrescrito.
  """
  try:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
      file.write(content)
    print(f"Arquivo criado com sucesso em {file_path}")
  except Exception as e:
    print(f"Erro ao criar o arquivo: {e}")