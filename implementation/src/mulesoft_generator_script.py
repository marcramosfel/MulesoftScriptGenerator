import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedTk

CONFIG_FILE = "implementation\\src\\config.txt"

class ProgramRunner:
    def __init__(self, root, programs):
        self.root = root
        self.programs = programs
        self.program_buttons = {}                

        self.setup_ui()

    def create_action_buttons(self):
        self.run_all_button = self.create_button(self.root, "Executar Todos os Scripts", self.run_all_programs, bg="#4CAF50")  # Cor verde
        self.run_all_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # Criar botões para cada programa
        for idx, (program_name, filepath) in enumerate(self.programs.items(), start=4):
            btn_color = "#4e89ae"
            if "Remover" in program_name:
                btn_color = "#FF0000"  # Cor vermelha
            btn = self.create_button(self.root, program_name, lambda fp=filepath: self.run_program(fp), bg=btn_color)
            btn.grid(row=idx, column=0, columnspan=2, pady=5, sticky="nsew")
            self.program_buttons[program_name] = btn

    def get_csv_from_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip()
        return None

    def run_programs(self, filepath):
        try:
            os.system(f"python {filepath}")
        except Exception as e:
            self.show_message("Erro", f"Erro ao executar {filepath}: {str(e)}")
        self.update_ui_state()

    def run_program(self, filepath):
        try:
            os.system(f"python {filepath}")
            self.show_message("Sucesso", f"{filepath} foi executado com sucesso!")
        except Exception as e:
            self.show_message("Erro", f"Erro ao executar {filepath}: {str(e)}")
        self.update_ui_state()

    def setup_ui(self):
        self.root.title("MuleSoft Script Generator")
        self.root.configure(bg="#f0f4f7")
        self.create_header()
        self.create_csv_display_area()
        self.create_control_buttons()
        self.create_action_buttons()

        # Configurar pesos para linhas e colunas
        self.root.grid_rowconfigure(0, weight=1)  # Linha principal
        self.root.grid_columnconfigure(0, weight=1)  # Coluna principal

    def create_header(self):
        tk.Label(self.root, text="🚀 MuleSoft Script Generator 🚀", font=("Arial", 40), bg="#f0f4f7").grid(row=0, column=0, columnspan=2, pady=10)  # Fonte maior e padding menor


    def create_csv_display_area(self):
        self.csv_text = self.create_text_widget(self.root, height=2, width=40)
        self.csv_text.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    def create_control_buttons(self):
        self.upload_button = self.create_button(self.root, "Carregar CSV", self.upload_csv)
        
        # Estique o botão para preencher todo o espaço horizontal na célula da grade
        self.upload_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.remove_csv_button = self.create_button(self.root, "Remover CSV", self.remove_csv)
        self.remove_csv_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Ajustar a coluna para que ela use todo o espaço disponível
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
    def create_button(self, parent, text, command, bg="#4e89ae"):
        return tk.Button(parent, text=text, command=command, bg=bg, fg="white", font=("Arial", 22))

    def create_text_widget(self, parent, **kwargs):
        text_widget = tk.Text(parent, **kwargs, bg="#e0e7ee")
        text_widget.config(state=tk.DISABLED)
        return text_widget

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def upload_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        if filepath:
            with open(CONFIG_FILE, 'w') as f:
                f.write(filepath)
            self.update_ui_state()
            #messagebox.showinfo("Sucesso", f"Arquivo CSV carregado de: {filepath}")

    def remove_csv(self):
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
            self.update_ui_state()
            #messagebox.showinfo("Sucesso", "Caminho do CSV removido com sucesso!")

    def update_ui_state(self):
        csv_path = self.get_csv_from_config()
        self.csv_text.config(state=tk.NORMAL, bg="#e0e7ee")
        self.csv_text.delete(1.0, tk.END)

        if csv_path:
            self.csv_text.insert(tk.END, csv_path)
            self.csv_text.config(bg='#FFD700')

            self.run_all_button.grid(row=3, column=0, columnspan=2, pady=10)
            for idx, btn in enumerate(self.program_buttons.values(), start=4):
                btn.grid(row=idx, column=0, columnspan=2, pady=5)
        else:
            self.run_all_button.grid_remove()
            for btn in self.program_buttons.values():
                btn.grid_remove()

        self.csv_text.config(state=tk.DISABLED)
   
    def run_all_programs(self):
        for program_name, filepath in self.programs.items():
            self.run_programs(filepath)
        self.show_message(f"Sucesso", "Todos os programas foram executado com sucesso!")


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

    root = ThemedTk(theme="arc")
    runner = ProgramRunner(root, programs_to_run)
    root.mainloop()

if __name__ == "__main__":
    main()
