import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import shutil

# Caminho para o arquivo de configuração que armazenará o caminho do CSV
CONFIG_FILE = "implementation\\src\\config.txt"

class ProgramRunner:
    def __init__(self, root, programs):
        """Inicializa a interface gráfica e as configurações do programa."""
        self.root = root
        self.programs = programs
        self.setup_ui()

    def get_csv_from_config(self):
        """Retorna o caminho do CSV a partir do arquivo de configuração."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip()
        return None

    def run_program(self, filepath):
        """Executa um programa específico com base no caminho do arquivo fornecido."""
        try:
            os.system(f"python {filepath}")
            messagebox.showinfo("Sucesso", f"{filepath} foi executado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar {filepath}: {str(e)}")
        self.update_ui_state()

    def run_all_programs(self):
        """Executa todos os programas listados."""
        for program in self.programs.values():
            self.run_program(program)
        self.update_ui_state()

    def setup_ui(self):
        

        """Configura a interface gráfica do programa."""
        self.root.title("MuleSoft Script Generator")
        self.root.configure(bg="#f0f4f7")

        # Cabeçalho
        tk.Label(self.root, text="🚀 MuleSoft Script Generator 🚀", font=("Arial", 16), bg="#f0f4f7").grid(row=0, column=0, columnspan=2, pady=20)

        # Área de exibição do CSV
        self.csv_text = tk.Text(self.root, height=2, width=40, bg="#e0e7ee")
        self.csv_text.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        self.csv_text.config(state=tk.DISABLED)

        # Botões de controle
        self.upload_button = tk.Button(self.root, text="Carregar CSV", command=self.upload_csv, bg="#4e89ae", fg="white", font=("Arial", 12))
        self.upload_button.grid(row=2, column=0, padx=20, pady=10)

        self.remove_csv_button = tk.Button(self.root, text="Remover CSV", command=self.remove_csv, bg="#4e89ae", fg="white", font=("Arial", 12))
        self.remove_csv_button.grid(row=2, column=1, padx=20, pady=10)

        # Botões de ação
        self.run_all_button = tk.Button(self.root, text="Executar Todos os Scripts", command=self.run_all_programs, bg="#4e89ae", fg="white", font=("Arial", 12))

        '''# Adicionar botão para gerar ZIP
        self.zip_button = tk.Button(self.root, text="Gerar ZIP de uma Pasta", command=self.zip_directory, bg="#4e89ae", fg="white", font=("Arial", 12))
        self.zip_button.grid(row=100, column=0, columnspan=2, pady=20)  # O número da linha foi ajustado para garantir que este botão fique na parte inferior.'''

        self.program_buttons = {}
        for idx, (name, path) in enumerate(self.programs.items(), start=4):
            btn = tk.Button(self.root, text=name, command=lambda p=path: self.run_program(p), bg="#4e89ae", fg="white", font=("Arial", 12))
            self.program_buttons[name] = btn

        self.update_ui_state()

    '''def zip_directory(self):
        """Compacta a pasta selecionada em um arquivo .zip."""
        dirpath = filedialog.askdirectory(title="Selecionar pasta para compactar")
        
        if dirpath:
            # Nome do arquivo zip baseado no nome da pasta
            zippath = os.path.join(os.path.dirname(dirpath), os.path.basename(dirpath) + ".zip")
            
            try:
                shutil.make_archive(zippath[:-4], 'zip', dirpath)
                messagebox.showinfo("Sucesso", f"Pasta compactada com sucesso em: {zippath}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao compactar pasta: {str(e)}")'''

    def upload_csv(self):
        """Carrega o arquivo CSV e atualiza a interface."""
        filepath = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        if filepath:
            with open(CONFIG_FILE, 'w') as f:
                f.write(filepath)
            self.update_ui_state()
            messagebox.showinfo("Sucesso", f"Arquivo CSV carregado de: {filepath}")

    def remove_csv(self):
        """Remove o caminho do CSV do arquivo de configuração e atualiza a interface."""
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
            self.update_ui_state()
            messagebox.showinfo("Sucesso", "Caminho do CSV removido com sucesso!")

    def update_ui_state(self):
        """Atualiza o estado da interface com base na presença ou ausência do arquivo CSV."""
        csv_path = self.get_csv_from_config()
        self.csv_text.config(state=tk.NORMAL, bg="#e0e7ee")
        self.csv_text.delete(1.0, tk.END)

        if csv_path:
            self.csv_text.insert(tk.END, csv_path)
            self.csv_text.config(bg='#FFD700')  # Cor de destaque

            # Exibe os botões
            self.run_all_button.grid(row=3, column=0, columnspan=2, pady=10)
            for idx, btn in enumerate(self.program_buttons.values(), start=4):
                btn.grid(row=idx, column=0, columnspan=2, pady=5)
        else:
            # Oculta os botões
            self.run_all_button.grid_remove()
            for btn in self.program_buttons.values():
                btn.grid_remove()

        self.csv_text.config(state=tk.DISABLED)

def main():
    """Função principal para iniciar o aplicativo."""
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


    root = tk.Tk()
    runner = ProgramRunner(root, programs_to_run)
    root.mainloop()

if __name__ == "__main__":
    main()

