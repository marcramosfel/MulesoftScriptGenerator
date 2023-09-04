import os
from termcolor import colored
import globals

def generate_yaml(files):
    """
    Gera uma estrutura YAML com base nos arquivos fornecidos.

    Parâmetros
    ----------
    files : lista
        Lista de nomes de arquivos para os quais a estrutura YAML precisa ser gerada.

    Retorna
    -------
    str
        Uma string formatada contendo a estrutura YAML gerada.
    """
    yaml = "#%RAML 1.0 DataType\n\n"
    yaml += "uses:\n  objectLibrary: libs/object.raml\n\nproperties:\n"

    for filename in files:
        name_without_extension = os.path.splitext(filename)[0]

        if name_without_extension.endswith("[]"):
            name_without_extension = name_without_extension.replace("[]", "")
        yaml += f"  {name_without_extension}:\n"
        yaml += f"    type: objectLibrary.{name_without_extension}Null\n"
        yaml += "    required: false\n"

    return yaml

if __name__ == "__main__":
    """
    Ponto principal de execução do script. Esta função irá:
    1. Ler todos os arquivos RAML do diretório de entrada especificado.
    2. Gerar uma estrutura YAML com base nos arquivos RAML.
    3. Escrever a estrutura YAML gerada no diretório de saída.
    """
    input_directory = globals.OUTPUT_DIRECTORY_OUTPUT_RAML
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_FINAL_DATATYPE 

    try:
        raml_files = [file for file in os.listdir(input_directory) if file.endswith(".raml")]

        if not raml_files:
            print(colored("Nenhum arquivo RAML encontrado no diretório.", "red"))
            exit()

        yaml_content = generate_yaml(raml_files)
        output_yaml = os.path.join(output_directory, 'output.yaml')

        with open(output_yaml, "w") as yaml_file:
            yaml_file.write(yaml_content)

        print(colored(f"\n\nEstrutura YAML gerada e salva como '{output_yaml}'\n", "green"))
    
    except FileNotFoundError:
        print(colored(f"Diretório '{input_directory}' não encontrado.", "red"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
