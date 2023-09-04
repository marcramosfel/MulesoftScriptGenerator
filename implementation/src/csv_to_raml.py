import csv
import codecs
import os
from termcolor import colored
import globals

# Criando um dicionário para mapear os tipos de dados SQL para seus respectivos tipos em Raml
data_type_mapping = globals.DATA_TYPE_MAP_SQL_TYPES_TO_RAML

# Criando um dicionário para mapear os tipos de dados SQL para seus respectivos exemplos em RAML
example_mapping = globals.DATA_TYPE_MAP_SQL_TYPES_TO_EXAMPLES

# Criando uma lista para não mapear os campos, dessa forma excluindo-os do output final
excluded_fields = globals.EXCLUDED_FIELDS


def lowercase_first_letter(s):
    """
    Converte a primeira letra de uma string para minúsculas.

    Parâmetros
    ----------
    s : str
        String original.

    Retorna
    -------
    str
        String com a primeira letra convertida para minúscula.
    """
    return s[:1].lower() + s[1:]

def process_raml_file(csv_file_path, output_directory):
    """
    Processa o arquivo CSV fornecido e gera um arquivo RAML correspondente.

    Parâmetros
    ----------
    csv_file_path : str
        Caminho para o arquivo CSV a ser processado.
    output_directory : str
        Diretório onde o arquivo RAML gerado será salvo.
    """
    try:
        with codecs.open(csv_file_path, 'r', 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Ignora a linha do cabeçalho
            rows = [row for row in csv_reader]

        file_name = os.path.basename(csv_file_path).split('.')[0]
        output_raml = os.path.join(output_directory, f"{file_name}.raml")

        raml_data = generate_raml_datatype(rows)

        with open(output_raml, 'w') as ramlfile:
            ramlfile.write(raml_data)

        print(colored(f"\nRAML data type gerado e salvo como '{output_raml}'\n", 'green'))

    except Exception as e:
        print(colored(f"Erro ao processar arquivo '{csv_file_path}': {e}", 'red'))

def generate_raml_datatype(rows):
    """
    Gera um tipo de dado RAML a partir das linhas fornecidas.

    Parâmetros
    ----------
    rows : list
        Lista de linhas do arquivo CSV contendo informações sobre os campos.

    Retorna
    -------
    str
        String formatada contendo o tipo de dado RAML gerado.
    """
    output = "#%RAML 1.0 DataType\n\n"
    output = "#%RAML 1.0 DataType\n\n"
    output += "type: array\nitems:\n  type: object\n  properties:\n"

    for row in rows:
        field = lowercase_first_letter(row[1])
        data_type = row[2]
        
        if data_type.endswith('?'):
            data_type = data_type.replace('?', "")
            raml_data_type = data_type_mapping.get(data_type, "string") # Default para "string" se não encontrado
            required = 'false'
        else:
            raml_data_type = data_type_mapping.get(data_type, "string") # Default para "string" se não encontrado
            required = 'true'
        if field not in excluded_fields:
            output += "    {}:\n".format(field)
            output += "      type: {}\n".format(raml_data_type)
            example = example_mapping.get(raml_data_type, '"string"')  # Default para "string" se não encontrado
            output += "      example: {}\n".format(example)
            output += "      required: {}\n".format(required)


    return output

def process_raml_files(input_directory, output_directory):
    """
    Processa todos os arquivos CSV no diretório fornecido e gera arquivos RAML correspondentes.

    Parâmetros
    ----------
    input_directory : str
        Diretório contendo os arquivos CSV a serem processados.
    output_directory : str
        Diretório onde os arquivos RAML gerados serão salvos.
    """
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(input_directory, filename)
            process_raml_file(csv_file_path, output_directory)

if __name__ == "__main__":
    """
    Ponto principal de execução do script. Esta função irá:
    1. Ler todos os arquivos CSV do diretório de entrada especificado.
    2. Gerar arquivos RAML correspondentes para cada arquivo CSV.
    3. Salvar os arquivos RAML gerados no diretório de saída.
    """
    input_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_RAML

    try:
        process_raml_files(input_directory, output_directory)
    except Exception as e:
        print(colored(f"Ocorreu um erro geral: {e}", 'red'))
