import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Define o nome do arquivo que irá guardar o caminho do CSV
CONFIG_FILE = "implementation\\src\\config.txt"  

class ProgramRunner:
    def __init__(self, programs):
        self.programs = programs

    def get_csv_from_config(self):
        """Retorna o caminho do CSV do arquivo de configuração ou None se não estiver disponível."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip()
        return None

    def run_program(self, filepath):
        """Executa um programa individual."""
        try:
            os.system(f"python {filepath}")
            messagebox.showinfo("Sucesso", f"{filepath} executado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar {filepath}: {e}")
        self.check_csv_and_update_buttons()

    def run_all_programs(self):
        """Executa todos os programas disponíveis, exceto o 'Remover todos os arquivos' primeiro."""
        remove_all_program_path = self.programs.get("Remover todos os arquivos", None)
        
        for program in self.programs.values():
            # Garante que não estamos executando o programa 'remove_all_files.py' primeiro
            if program == remove_all_program_path:
                continue
            self.run_program(program)
            self.check_csv_and_update_buttons()

    def display_menu(self, root):
        """Mostra o menu interativo."""

        # Cabeçalho
        tk.Label(root, text="🚀 MuleSoft Script Generator 🚀", font=("Arial", 16)).pack(pady=10)

        # Botão para carregar um CSV
        self.upload_button = tk.Button(root, text="Carregar CSV", command=self.upload_csv)
        self.upload_button.pack(pady=10)

        # Botão para rodar todos os programas de uma vez
        self.run_all_button = tk.Button(root, text="Rodar Todos", command=self.run_all_programs)
        self.run_all_button.pack(pady=10)

        # Botões para cada programa individual
        self.program_buttons = []
        for program_name, program_path in self.programs.items():
            btn = tk.Button(root, text=program_name, command=lambda p=program_path: self.run_program(p))
            btn.pack(pady=5)
            self.program_buttons.append(btn)

        self.check_csv_and_update_buttons()

    def upload_csv(self):
        """Permite ao usuário fazer o upload de um arquivo CSV e salva o caminho no arquivo de configuração."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        file_path = file_path.replace("/", "\\\\")
        if file_path:
            with open(CONFIG_FILE, 'w') as f:
                f.write(file_path)
            messagebox.showinfo("Sucesso", f"Arquivo CSV carregado: {file_path}")
        self.check_csv_and_update_buttons()

    def check_csv_and_update_buttons(self):
        """Verifica se um CSV está disponível e atualiza a habilitação dos botões conforme necessário."""
        has_csv = bool(self.get_csv_from_config())
        
        # Atualiza o estado dos botões com base na presença do CSV
        for btn in self.program_buttons:
            btn['state'] = tk.NORMAL if has_csv else tk.DISABLED
        
        # Atualiza o botão 'Rodar Todos'
        self.run_all_button['state'] = tk.NORMAL if has_csv else tk.DISABLED

def main():
    programs_to_run = {
        "Remover todos os arquivos": "implementation\\src\\remove_all_files.py",
        "Dividir CSV": "implementation\\src\\split_csv.py",
        "CSV para Variável": "implementation\\src\\csv_to_variable.py",
        "CSV para Tipo Lógico": "implementation\\src\\csv_to_type_logical.py",
        "CSV para RAML": "implementation\\src\\csv_to_raml.py",
        "Criar Data Type": "implementation\\src\\create_datatype.py",
        "Variável para Transform Message": "implementation\\src\\variable_to_transform_message.py",
        "Tipo Lógico para Scatter-Gather": "implementation\\src\\type_logical_to_scatter_gather.py",
        "Saída Scatter-Gather": "implementation\\src\\output_scatter_gather.py"
    }


    runner = ProgramRunner(programs_to_run)
    
    root = tk.Tk()
    root.title("Menu Interativo")
    runner.display_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
