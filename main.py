import os
from termcolor import *

class ProgramRunner:

    def __init__(self, programs):
        self.programs = programs

    def run_program(self, filename):
        try:
            os.system(f"python {filename}")
            print(colored(f"\n{filename} executado com sucesso!", "green"))
        except Exception as e:
            print(colored(f"Erro ao executar {filename}: {e}", "red"))

    def run_all(self):
        for program in self.programs:
            self.run_program(program)
            print("\n\n" + "+" * 120)

    def display_menu(self):
        print(colored("\nEscolha uma das seguintes opções:", 'yellow', 'on_black', ['bold', 'blink']))
        print(colored("\n0. Executar todos os programas\n", 'light_cyan'))
        for idx, program in enumerate(self.programs, 1):
            print(colored(f"{idx}. Executar {program}", "cyan"))

        choice = input(colored("\nInsira o número da sua escolha: ", 'yellow', 'on_black', ['bold', 'blink']))
        return choice

def main():
    programs_to_run = [
        "implementation\\codeV2\\0removeAllFiles.py",
        "implementation\\codeV2\\1splitCsv_V2.py",
        "implementation\\codeV2\\2csvToVariable_V2.py",
        "implementation\\codeV2\\3csvToTypeLogical_V2.py",
        "implementation\\codeV2\\4csvToRaml_V2.py",
        "implementation\\codeV2\\5createDataType_V2.py",
        "implementation\\codeV2\\6variableToTransformMessageV2.py",
        "implementation\\codeV2\\7typeLogicalToScatterV2.py",
        "implementation\\codeV2\\8outputScatterV2.py",
        "implementation\\codeV2\\globals.py"
    ]

    runner = ProgramRunner(programs_to_run)
    choice = runner.display_menu()

    if choice == "0":
        runner.run_all()
    elif choice.isdigit() and 0 < int(choice) <= len(programs_to_run):
        runner.run_program(programs_to_run[int(choice) - 1])
    else:
        print(colored("Opção inválida!", "red"))

if __name__ == "__main__":
    main()
