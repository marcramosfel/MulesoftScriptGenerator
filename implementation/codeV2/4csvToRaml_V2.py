import csv
import codecs
import os
from termcolor import colored
import globals

# Create a dictionary to map SQL data types to their respective types in Raml
data_type_mapping = globals.DATA_TYPE_MAP_SQL_TYPES_TO_RAML

# Create a dictionary to map SQL data types to their respective examples in RAML
example_mapping = globals.DATA_TYPE_MAP_SQL_TYPES_TO_EXAMPLES

excluded_fields = globals.EXCLUDED_FIELDS

def lowercase_first_letter(s):
    return s[:1].lower() + s[1:]

def process_raml_file(csv_file_path, output_directory):
    try:
        with codecs.open(csv_file_path, 'r', 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
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
    output = "#%RAML 1.0 DataType\n\n"
    output += "type: array\nitems:\n  type: object\n  properties:\n"

    for row in rows:
        field = lowercase_first_letter(row[1])
        data_type = row[2]
        
        if data_type.endswith('?'):
            data_type = data_type.replace('?', "")
            raml_data_type = data_type_mapping.get(data_type, "string") # Default to "string" if not found
            required = 'false'
        else:
            raml_data_type = data_type_mapping.get(data_type, "string") # Default to "string" if not found
            required = 'true'
        if field not in excluded_fields:
            output += "    {}:\n".format(field)
            output += "      type: {}\n".format(raml_data_type)
            example = example_mapping.get(raml_data_type, '"string"')  # Default to "string" if not found
            output += "      example: {}\n".format(example)
            output += "      required: {}\n".format(required)


    return output

def process_raml_files(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(input_directory, filename)
            process_raml_file(csv_file_path, output_directory)

if __name__ == "__main__":
    input_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_RAML

    try:
        process_raml_files(input_directory, output_directory)
    except Exception as e:
        print(colored(f"Ocorreu um erro geral: {e}", 'red'))
