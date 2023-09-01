import csv
import os
from termcolor import colored
import globals

def read_csv_data(input_csv_file):
    data_by_aggregator = {}
    
    try:
        with open(input_csv_file, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            for row in csv_reader:
                aggregator = row["Agregador"]
                if aggregator not in data_by_aggregator:
                    data_by_aggregator[aggregator] = []
                data_by_aggregator[aggregator].append(row)
    
        return data_by_aggregator
    except FileNotFoundError:
        print(colored(f"Erro: Não foi possível encontrar o arquivo '{input_csv_file}'", 'red'))
        return None
    except Exception as e:
        print(colored(f"Erro ao ler o arquivo CSV: {e}", 'red'))
        return None

def create_output_csv(data_by_aggregator, output_directory):
    try:
        os.makedirs(output_directory, exist_ok=True)
        for aggregator, elements in data_by_aggregator.items():
            if aggregator.endswith("[]"):
                aggregator = aggregator.replace("[]", "")
            output_csv_file = os.path.join(output_directory, f"{aggregator}.csv")

            with open(output_csv_file, 'w', newline='') as csvfile:
                fieldnames = elements[0].keys()
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                csv_writer.writeheader()
                csv_writer.writerows(elements)

            print(colored(f"\nElementos do Agregador '{aggregator}' salvos em '{output_csv_file}'\n", 'green'))

    except Exception as e:
        print(colored(f"Erro ao escrever o arquivo CSV: {e}", 'red'))

if __name__ == "__main__":
    input_csv_file =  globals.INPUT_CSV_FILE # Substitua pelo caminho do seu arquivo CSV
    output_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV

    try:
        data_by_aggregator = read_csv_data(input_csv_file)
        if data_by_aggregator:  # Se não houve erro na leitura do arquivo CSV
            create_output_csv(data_by_aggregator, output_directory)
    except Exception as e:
        print(colored("Erro inesperado:", 'red'), e)
