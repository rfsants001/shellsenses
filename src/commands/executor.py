import subprocess

def execute_command(command):
  """
    Executa um comando shell.
  """
  try:
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    print(result.stdout)
  except subprocess.CalledProcessError as e:
    print(f"Erro ao executar o comando: {e}")