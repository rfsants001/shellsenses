import sys
import os

# Adiciona o diretório principal ao caminho de importação
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.commands.command_parser import interpret_shell_command, interpret_create_command
from src.commands.executor import execute_command

def main():
  print("Welcome to the command line interface ShellSenses! \nPara comandos shell, use 'run:'. Para criar arquivos/pastas, use 'create:' \nType 'exit' to quit.")
  while True:
    user_input = input("ShellSenses -> ").strip()
    if user_input == "exit":
      print("Exiting ShellSenses...")
      break;

    if user_input.startswith("run:"):
      shell_command = interpret_shell_command(user_input[len("run:"):].strip())
      if shell_command:
        print("Executing command: " + shell_command)
        confirm = input("Do you want to execute this command? (y/n) ").lower()
        if confirm == "y":
          execute_command(shell_command)
        else:
          print("Command execution cancelled.")
    
    if user_input.startswith("create:"):
      create_command = interpret_create_command(user_input[len("create:"):].strip())
      interpret_create_command(create_command)

    else:
      print("Comando não reconhecido. Tente novamente.")

if __name__ == "__main__":
  main()