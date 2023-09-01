import csv
import codecs
import os
from termcolor import colored
import globals

def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

def lowercase_first_letter(s):
    return s[:1].lower() + s[1:]

def process_csv_file(csv_file_path, output_directory):
    try:
        with codecs.open(csv_file_path, 'r', 'utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            csv_rows = list(csv_reader)

        table_name = next((row['Agregador'] for row in csv_rows if row['Agregador']), None)

        if not table_name:
            raise ValueError(f"Nenhum nome de tabela encontrado em {csv_file_path}")

        table_name_without_brackets = table_name.replace("[]", "")
        table_name_withot_underscore = table_name.replace("_", "")
        table_name_withot_underscore_ID = table_name_withot_underscore.replace("[]", "") + "Id"
        output_file_path = f"{output_directory}/{table_name_without_brackets}.dwl"

        if table_name.endswith('[]'):
            table_name = table_name.replace('[]', '')

        capitalize_table_name = capitalize_first(table_name)
        lowercase_table_name = lowercase_first_letter(table_name)
        dw_code = f"""%dw 2.0
output application/java
---
{{
    "{capitalize_table_name}": payload.{lowercase_table_name} map (item, i) -> {{
"""

        excluded_fields = [table_name_withot_underscore_ID]
        print(excluded_fields)
        excluded_fields.extend(globals.EXCLUDED_FIELDS)
        print(excluded_fields)

        for row in csv_rows:
            field_name = row['Campo']
            #   print(field_name)
            if field_name == "q01_ANO" or field_name == "q03_NIF":
                dw_code += f'        "{field_name}": payload.rosto.{field_name},\n'
            elif field_name not in excluded_fields:
                #print(field_name)
                dw_code += f'        "{field_name}": item.{field_name},\n'

        dw_code = dw_code.rstrip(",\n")

        dw_code += """
    }
}"""

        with open(output_file_path, 'w') as output_file:
            output_file.write(dw_code)

        print(colored(f"\nCódigo DataWeave salvo em {output_file_path}\n", 'green'))

    except FileNotFoundError:
        print(colored(f"Erro: Arquivo {csv_file_path} não encontrado.", 'red'))
    except Exception as e:
        print(colored(f"Erro ao processar {csv_file_path}: {e}", 'red'))

def process_csv_files(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(input_directory, filename)
            process_csv_file(csv_file_path, output_directory)

if __name__ == "__main__":
    input_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_VARS
    try:
        process_csv_files(input_directory, output_directory)
    except Exception as e:
        print(colored("Ocorreu um erro inesperado: ", 'red'), e)
