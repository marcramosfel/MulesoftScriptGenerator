import os
from termcolor import colored
import globals

def capitalize_first(s):
    """
    Capitaliza a primeira letra de uma string.

    Parâmetros
    ----------
    s : str
        String a ser capitalizada.

    Retorna
    -------
    str
        String com a primeira letra capitalizada.
    """
    if not s:
        return s
    return s[0].upper() + s[1:]

def generate_transform_block(file_content, filename):
    """
    Gera um bloco de transformação para o conteúdo do arquivo e nome do arquivo fornecidos.

    Parâmetros
    ----------
    file_content : str
        Conteúdo do arquivo.
    filename : str
        Nome do arquivo.

    Retorna
    -------
    str
        Bloco de transformação gerado.
    """
    capitalize_filename = capitalize_first(filename)
    block = f"""
<route >
    <ee:transform doc:name="{filename.split('.dwl')[0]}" doc:id="b5fde3b1-0049-4b00-acd6-253c4c587459" >
        <ee:message >
            <ee:set-payload ><![CDATA[{file_content}]]></ee:set-payload>
        </ee:message>
    </ee:transform>
    <flow-ref doc:name="z-common-db-sql-types\\typesLogical-dynamic" doc:id="e3c41792-7809-4dfa-a17c-e38b8b917339" name="z-common-db-sql-types\\typesLogical-dynamic" />
    <ee:transform doc:name="{filename.split('.dwl')[0]}_Obj @dboName" doc:id="a3eb8e9a-7f3c-42fd-9ab2-1716fd7a0c0d" >
        <ee:message >
            <ee:set-payload ><![CDATA[%dw 2.0
output application/java
---
{{
     tbl{capitalize_filename.split('.dwl')[0]}_Obj: vars.dboName
}}]]></ee:set-payload>
        </ee:message>
    </ee:transform>
</route>
"""
    return block

def generate_code_from_directory(directory_path):
    """
    Gera código a partir dos arquivos encontrados no diretório especificado.

    Parâmetros
    ----------
    directory_path : str
        Caminho do diretório contendo os arquivos.

    Retorna
    -------
    str
        Código gerado a partir dos arquivos no diretório.
    """
    all_code_blocks = []

    # Itera sobre todos os arquivos no diretório fornecido
    try:
        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                with open(os.path.join(directory_path, filename), 'r') as file:
                    file_content = file.read()
                    code_block = generate_transform_block(file_content, filename)
                    all_code_blocks.append(code_block)

        # Agrupa todos os blocos de código em <scatter-gather>
        return f"<scatter-gather doc:name=\"Scatter-Gather\" doc:id=\"AUTO_GENERATED_ID\" >\n{''.join(all_code_blocks)}\n</scatter-gather>"
    
    except Exception as e:
        print(colored(f"Ocorreu um erro ao gerar código a partir do diretório: {e}", "red"))
        exit()
def save_to_file(content, output_file_path):
    """
    Salva o conteúdo em um arquivo especificado.

    Parâmetros
    ----------
    content : str
        Conteúdo a ser salvo.
    output_file_path : str
        Caminho do arquivo de saída.

    """
    try:
        with open(output_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(colored(f"Ocorreu um erro ao salvar o arquivo: {e}", "red"))
        exit()
if __name__ == "__main__":
    directory_path = globals.OUTPUT_DIRECTORY_OUTPUT_TYPE_LOGICAL  # Substitua pelo caminho do seu diretório
    output_file_path = globals.OUTPUT_FILE_PATH_FINAL_SCATTER  # Substitua pelo caminho/nome de saída desejado

    # Tenta gerar o código e salvar o resultado
    try:
        result = generate_code_from_directory(directory_path)
        if result:
            save_to_file(result, output_file_path)
            print(colored(f"\n\nResultado salvo em {output_file_path}\n", "green"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
        exit()