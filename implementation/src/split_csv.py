import csv
import os
from termcolor import colored
import globals

def read_csv_data(input_csv_file):
    """
    Lê os dados de um arquivo CSV e agrupa as linhas pelo campo "Agregador".

    Parâmetros
    ----------
    input_csv_file : str
        Caminho para o arquivo CSV que deve ser lido.

    Retorna
    -------
    dict
        Um dicionário com a chave sendo o nome do agregador e os valores sendo 
        uma lista de linhas (dicionários) associadas a esse agregador.
        Retorna None em caso de erro na leitura.
    """
    
    data_by_aggregator = {}
    
    try:
        with open(input_csv_file, 'r') as csvfile:
            # Utilizando DictReader para ler o arquivo CSV como um dicionário
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            
            # Iterando sobre cada linha do CSV
            for row in csv_reader:
                aggregator = row["Agregador"]
                
                # Se o agregador não existir no dicionário, inicialize com uma lista vazia
                if aggregator not in data_by_aggregator:
                    data_by_aggregator[aggregator] = []
                
                # Adiciona a linha ao agregador correspondente
                data_by_aggregator[aggregator].append(row)
    
        return data_by_aggregator
    
    except FileNotFoundError:
        print(colored(f"Erro: Não foi possível encontrar o arquivo '{input_csv_file}'", 'red'))
        exit()
    except Exception as e:
        print(colored(f"Erro ao ler o arquivo CSV: {e}", 'red'))
        exit()

def create_output_csv(data_by_aggregator, output_directory):
    """
    Cria arquivos CSV separados para cada agregador.

    Parâmetros
    ----------
    data_by_aggregator : dict
        Dicionário contendo os dados agrupados por agregador.
    output_directory : str
        Diretório onde os arquivos CSV serão salvos.
    """

    try:
        # Criando o diretório de saída, se ele não existir
        os.makedirs(output_directory, exist_ok=True)
        
        # Iterando sobre cada agregador
        for aggregator, elements in data_by_aggregator.items():
            
            # Removendo "[]" se estiver no final do nome do agregador
            if aggregator.endswith("[]"):
                aggregator = aggregator.replace("[]", "")
            
            # Definindo o caminho do arquivo de saída
            output_csv_file = os.path.join(output_directory, f"{aggregator}.csv")

            with open(output_csv_file, 'w', newline='') as csvfile:
                # Escrevendo os dados no CSV de saída
                fieldnames = elements[0].keys()
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(elements)

            print(colored(f"\nElementos do Agregador '{aggregator}' salvos em '{output_csv_file}'\n", 'green'))

    except Exception as e:
        print(colored(f"Erro ao escrever o arquivo CSV: {e}", 'red'))

if __name__ == "__main__":
    print(globals.INPUT_CSV_FILE)
    input_csv_file =  globals.INPUT_CSV_FILE 
    output_directory = globals.OUTPUT_DIRECTORY_INPUT_CSV

    try:
        data_by_aggregator = read_csv_data(input_csv_file)
        if data_by_aggregator:
            create_output_csv(data_by_aggregator, output_directory)
    except Exception as e:
        print(colored("Erro inesperado:", 'red'), e)
