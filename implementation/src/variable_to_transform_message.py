import os
from termcolor import colored
import globals

def insert_into_set_variable(file_content, variable_name):
    template = f"""
<ee:set-variable variableName="{variable_name}"><![CDATA[
{file_content}
]]></ee:set-variable>
"""
    return template

def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

def generate_code_from_directory(directory_path):
    all_code_blocks = []

    try:
        # Iterar sobre cada arquivo no diretório
        for filename in os.listdir(directory_path):
            # Certifique-se de que é um arquivo e não um diretório ou outra coisa
            if os.path.isfile(os.path.join(directory_path, filename)):
                with open(os.path.join(directory_path, filename), 'r') as file:
                    file_content = file.read()
                    variable_name = capitalize_first(filename)
                    # Usando o nome do arquivo como nome da variável para simplificar

                    variable_name1 = "var" + variable_name.replace(".dwl", "")
                    code_block = insert_into_set_variable(file_content, variable_name1)
                    all_code_blocks.append(code_block)
        return "\n".join(all_code_blocks)
    
    except Exception as e:
        print(colored(f"Ocorreu um erro ao gerar código a partir do diretório: {e}", "red"))
        return None

def save_to_file(content, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(colored(f"Ocorreu um erro ao salvar o arquivo: {e}", "red"))

if __name__ == "__main__":
    directory_path = globals.OUTPUT_DIRECTORY_OUTPUT_VARS  # substitua pelo caminho do seu diretório
    output_file_path = globals.OUTPUT_FILE_PATH_FINAL_TRANSFORM_MESSAGE  # substitua pelo caminho/nome do arquivo de saída desejado
    
    try:
        result = generate_code_from_directory(directory_path)
        if result:
            save_to_file(result, output_file_path)
            print(colored(f"\n\nResultado salvo em {output_file_path}\n", "green"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
