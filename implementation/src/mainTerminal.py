import os
from termcolor import colored

class ProgramRunner:
    """
    Classe para executar uma lista de programas.

    Parameters
    ----------
    programs : list
        Lista contendo os nomes dos arquivos de programa a serem executados.

    Attributes
    ----------
    programs : list
        Armazena os nomes dos arquivos de programa.
    """

    def __init__(self, programs):
        self.programs = programs

    def run_program(self, filename):
        """Executa um programa."""
        try:
            os.system(f"python {filename}")
            #print(colored(f"\n{filename} executado com sucesso!", "green"))
        except Exception as e:
            print(colored(f"Erro ao executar {filename}: {e}", "red"))
            exit()

    def run_all(self):
        """Executa todos os programas."""
        for program in self.programs:
            self.run_program(program)
            print("\n\n" + "+" * 120)

    def display_menu(self):
        """Exibe o menu interativo e retorna a escolha do usuário."""
        os.system("clear" if os.name == "posix" else "cls")  # limpa o terminal
        
        # Cabeçalho
        print(colored("+" * 82, 'yellow'))
        print(colored("🚀 MuleSoft Script Generator 🚀".center(80), 'black', 'on_yellow', ['bold']))
        print(colored("+" * 82, 'yellow'))

        # Lista de programas
        print(colored("\nEscolha uma das seguintes opções:", 'yellow', 'on_black', ['bold', 'blink']))
        print(colored("\n0️⃣. Executar todos os programas\n", 'light_cyan'))
        for idx, program in enumerate(self.programs, 1):
            print(colored(f"{idx}️⃣. Executar {program}", "cyan"))

        choice = input(colored("\nInsira o número da sua escolha: ", 'yellow', 'on_black', ['bold', 'blink']))
        return choice

def main():
    """
    Função principal. Inicia o menu interativo e processa a escolha do usuário.

    """
    programs_to_run = [
        "implementation\\src\\remove_all_files.py",
        "implementation\\src\\split_csv.py",
        "implementation\\src\\csv_to_variable.py",
        "implementation\\src\\csv_to_type_logical.py",
        "implementation\\src\\csv_to_raml.py",
        "implementation\\src\\create_datatype.py",
        "implementation\\src\\variable_to_transform_message.py",
        "implementation\\src\\type_logical_to_scatter_gather.py",
        "implementation\\src\\output_scatter_gather.py"
    ]

    runner = ProgramRunner(programs_to_run)
    choice = runner.display_menu()
    try:
        if choice == "0":
            runner.run_all()
        elif choice.isdigit() and 0 < int(choice) <= len(programs_to_run):
            runner.run_program(programs_to_run[int(choice) - 1])
        else:
            print(colored("Opção inválida!", "red"))
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
