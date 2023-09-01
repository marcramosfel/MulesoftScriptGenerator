import os
from termcolor import colored
import globals

def remove_files_in_directory(directory_path):
    """
    Remove todos os arquivos dentro do diretório especificado.
    """
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Certifica-se que é um arquivo e não um diretório ou subdiretório
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(colored(f"Arquivo {filename} removido com sucesso de {directory_path}!", "light_green"))
            elif os.path.isdir(file_path):
                # Se for um diretório, chama recursivamente para remover arquivos dentro de subdiretórios
                remove_files_in_directory(file_path)
    except Exception as e:
        print(colored(f"Erro ao tentar remover arquivos em {directory_path}: {e}", "red"))

def main():
    root_directory = globals.ROOT_DIRECTORY

    # Verifica se a pasta 'utils' existe
    if not os.path.exists(root_directory):
        print(colored(f"A pasta '{root_directory}' não existe!", "red"))
        return

    # Itera sobre todas as pastas dentro de 'utils'
    for dir_name in os.listdir(root_directory):
        dir_path = os.path.join(root_directory, dir_name)
        
        # Certifica-se de que é um diretório
        if os.path.isdir(dir_path):
            remove_files_in_directory(dir_path)

if __name__ == "__main__":
    main()
