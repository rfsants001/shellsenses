import re
import openai
import os
import json
import yaml
from dotenv import load_dotenv

from utils.file_manager import create_file_with_content

load_dotenv()
with open("config/config.yaml", "r") as file:
  config = yaml.safe_load(file)

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = config["openai"]["model"]


if "openai" in config and "model" in config["openai"]:
    model_name = config["openai"]["model"]
else:
    print("Erro: Configuração do modelo OpenAI não encontrada no config.yaml.")
    model_name = "gpt-4o-mini"  

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def interpret_shell_command(user_input):
  """Usa o modelo GPT-4o-mini da OpenAI para interpretar o comando em linguagem natural e criar comandos shell."""
  response = client.chat.completions.create(
      model=model_name,
       messages=[
        {"role": "system", "content": (
                        "Você é um assistente de terminal. Interprete comandos em linguagem natural e converta em comando shell sem formatação."
                    )},
        {"role": "user", "content": user_input}
      ],
      max_tokens=200,
      temperature=0.2
    )
  response_text = response.choices[0].message.content.strip()
  return response_text

def interpret_create_command(user_input):
  """
    Usa o modelo GPT-4o-mini da OpenAI para interpretar o comando em linguagem natural e criar arquivos e pastas de forma automatica.
  """
  try:
    response = client.chat.completions.create(
      model=model_name,
       messages=[
        {"role": "system", "content": (
                        "Você é um assistente de terminal e deve criar arquivos e pastas. Interprete comandos em linguagem natural. "
                        "Responda com uma estrutura JSON e no seguinte formato:\n"
                        "{'create_folder': true ou false, 'folder_path': 'caminho/da/pasta', 'create_file': true ou false, "
                        "'file_path': 'caminho/do/arquivo', 'content': 'conteúdo do arquivo, caso o comando não tenha instrussões de conteúdo, "
                        "crie um conteúdo basico com base no tipo de arquivo que foi pedido, em conotação para string adicione aspas simples no lugar de aspas normal', "
                        "'file_name': 'nome do arquivo com a extensão (.txt, .html, etc)'}"
                    )},
        {"role": "user", "content": user_input}
      ],
      max_tokens=1000,
      temperature=0.2
    )
    response_text = response.choices[0].message.content.strip()
    formatted_response = response_text.replace("'", '"')

    createdFolder = False
    try:
      response_data = json.loads(formatted_response)

      print(response_data)

      folder_path = response_data.get("folder_path") or os.getcwd()
      print(f"Folder path determinado: '{folder_path}'")

      if(response_data.get("create_folder")):
        if not os.path.exists(folder_path):
          os.makedirs(folder_path, exist_ok=True)
          print(f"Pasta criada com sucesso em {folder_path}")
          createdFolder = True
        else:
          print(f"Pasta já existe em {folder_path}")

      if(response_data.get("create_file")):
        file_name = response_data.get("file_name")
        if os.path.isabs(file_name):
            file_path = file_name
        else:
            file_path = os.path.join(folder_path, file_name) if not file_name.startswith(folder_path) else file_name

        print(f"File path completo: '{file_path}'")
        
        if not createdFolder:
          file_path = os.path.join(response_data["folder_path"], file_path)

        content = response_data.get("content", "")

        if file_path:  
          create_file_with_content(file_path, content)
          return "Arquivo '{file_path}' criado com o conteúdo fornecido."
          
        else:
          return "Erro: 'file_path' está vazio e não foi possível definir um caminho padrão para o arquivo."

    except json.JSONDecodeError as e:
      return f"Erro ao decodificar a resposta JSON: {e}"
  except Exception as e:
    print(f"Erro ao chamar a API da OpenAI: {e}")
    return None