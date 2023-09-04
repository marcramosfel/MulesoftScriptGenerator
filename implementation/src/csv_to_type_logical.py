import csv
import codecs
import os
from termcolor import colored
import globals

dbtypes_list = globals.DBTYPES_LIST

def capitalize_first(s):
    """
    Retorna a string com a primeira letra em maiúscula.

    Parameters
    ----------
    s : str
        String de entrada.

    Returns
    -------
    str
        String com a primeira letra em maiúscula.
    """
    if not s:
        return s
    return s[0].upper() + s[1:]

def lowercase_first_letter(s):
    """
    Retorna a string com a primeira letra em minúscula.

    Parameters
    ----------
    s : str
        String de entrada.

    Returns
    -------
    str
        String com a primeira letra em minúscula.
    """
    return s[:1].lower() + s[1:]

def process_csv_file(csv_file_path, output_directory):
    """
    Processa o arquivo CSV fornecido e gera um arquivo DataWeave com base nos dados.

    Parameters
    ----------
    csv_file_path : str
        Caminho do arquivo CSV de entrada.
    output_directory : str
        Diretório onde o arquivo DataWeave será salvo.
    
    Raises
    ------
    FileNotFoundError
        Se o arquivo CSV não for encontrado.
    KeyError
        Se um tipo de dado não for encontrado na lista de dbtypes.
    """
    try:
        # Leitura do arquivo CSV
        with codecs.open(csv_file_path, 'r', 'utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            csv_rows = list(csv_reader)

        # Recupera o nome da tabela do arquivo CSV      
        table_name = next((row['Agregador'] for row in csv_rows if row['Agregador']), None)
        
        # Trata o nome da tabela para usos subsequentes
        if not table_name:
            raise ValueError(f"Nenhum nome de tabela encontrado em {csv_file_path}")
        
        # Trata o nome da tabela para usos subsequentes
        # (remove colchetes, substitui sublinhados, etc.)
        # ... (códigos para tratar o nome da tabela)
        table_name_without_brackets = table_name.replace("[]", "")
        table_name_withot_underscore = table_name.replace("_", "")
        table_name_withot_underscore_ID = table_name_withot_underscore.replace("[]", "") + "Id"
        capitalize_table_name = capitalize_first(table_name)

        output_file_path = os.path.join(output_directory, f"{table_name_without_brackets}.dwl")
        
        # ... (geração de código DataWeave)
        dw_code = f"""%dw 2.0 
output application/json      
---
{{
    dboName: "Tbl{capitalize_table_name}",
    dboType: "ies.{capitalize_table_name}Type",
    dboColumns: [
"""

        excluded_fields = [table_name_withot_underscore_ID]
        excluded_fields.extend(globals.EXCLUDED_FIELDS)

        for row in csv_rows:
            field_name = row['Campo']
            db_type = str(row['Tipo de dados'])
            db_type = db_type.replace("?", "") if db_type.endswith("?") else db_type
            #print(dbtypes_list.get(db_type))
            if field_name not in excluded_fields:
                dw_code += f'{{\n       dbName: "{field_name}",\n       dbType: {dbtypes_list.get(db_type, "Unknown")}\n   }},'

        dw_code = dw_code.rstrip(",\n")
        dw_code += f'''],
dataIn: vars.var{capitalize_table_name}.{capitalize_table_name} map (index, i) -> [
'''

        for row in csv_rows:
            field_name = row['Campo']
            if field_name not in excluded_fields:
                dw_code += f'        index.{field_name},\n'

        dw_code = dw_code.rstrip(",\n")
        dw_code += '''
    ]
}
'''
        
        # Escreve o código DataWeave no arquivo de saída
        with open(output_file_path, 'w') as output_file:
            output_file.write(dw_code)
        
        # Mensagem de sucesso
        print(colored(f"\nCódigo DataWeave salvo em {output_file_path}\n", 'green'))

    except FileNotFoundError:
        # Erro tratado: arquivo CSV não encontrado
        # ... (tratamento de outros erros específicos)
        print(colored(f"Erro: Arquivo {csv_file_path} não encontrado.", 'red'))
    except KeyError:
        print(colored(f"Erro: Tipo de dado não encontrado na lista dbtypes para {csv_file_path}.", 'red'))
    except Exception as e:
        print(colored(f"Erro ao processar {csv_file_path}: {e}", 'red'))

def process_csv_files(input_directory, output_directory):
    """
    Processa todos os arquivos CSV em um diretório fornecido.

    Parameters
    ----------
    input_directory : str
        Diretório contendo arquivos CSV.
    output_directory : str
        Diretório onde os arquivos DataWeave serão salvos.
    """
    
    # Itera sobre todos os arquivos no diretório de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(input_directory, filename)
            process_csv_file(csv_file_path, output_directory)

if __name__ == "__main__":
    input_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_TYPE_LOGICAL
    try:
        process_csv_files(input_directory, output_directory)
    except Exception as e:
        print(colored("Ocorreu um erro inesperado: ", 'red'), e)
