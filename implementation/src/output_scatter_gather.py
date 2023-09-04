import os
from termcolor import colored
import globals

def capitalize_first(s):
    """
    Capitaliza a primeira letra da string fornecida.

    Parâmetros
    ----------
    s : str
        A string a ser capitalizada.

    Retorna
    -------
    str
        String com a primeira letra capitalizada.
    """
    if not s:
        return s
    return s[0].upper() + s[1:]

def generate_script(directory_path):
    """
    Gera um script com base nos nomes dos arquivos no diretório fornecido.

    Parâmetros
    ----------
    directory_path : str
        O caminho do diretório contendo os arquivos.

    Retorna
    -------
    str
        Script gerado com base nos nomes dos arquivos.
    """
    try:
        # Obtém todos os arquivos no diretório fornecido
        filenames = os.listdir(directory_path)
        
        # Filtra arquivos indesejados ou diretórios
        filenames = [f for f in filenames if os.path.isfile(os.path.join(directory_path, f))]

        # Inicializa o script com o cabeçalho
        script = """%%dw 2.0
output application/java
---
{"""

        # Para cada nome de arquivo, gera a linha correspondente no script
        for filename in filenames:
            name_without_extension = capitalize_first(os.path.splitext(filename)[0])
            line = f"\n\tTbl{name_without_extension}: payload..tbl{name_without_extension}_Obj[0],"
            script += line

        # Fecha a chave do script
        script += "\n}\n"

        return script
    except Exception as e:
        print(colored(f"Ocorreu um erro ao gerar o script: {e}", "red"))
        exit()
def save_to_file(content, output_file_path):
    """
    Salva o conteúdo em um arquivo especificado.

    Parâmetros
    ----------
    content : str
        Conteúdo a ser salvo.
    output_file_path : str
        Caminho para o arquivo de saída.

    Retorna
    -------
    None
    """
    try:
        with open(output_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(colored(f"Ocorreu um erro ao salvar o arquivo: {e}", "red"))
        exit()

if __name__ == "__main__":
    directory_path = globals.OUTPUT_DIRECTORY_OUTPUT_RAML  # Substitua pelo caminho do seu diretório
    output_file_path = globals.OUTPUT_FILE_PATH_FINAL_OUTPUT_SCATTER  # Substitua pelo caminho/nome de saída desejado
    
    try:
        result = generate_script(directory_path)
        if result:
            save_to_file(result, output_file_path)
            print(colored(f"Resultado salvo em {output_file_path}", "green"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
        exit()
