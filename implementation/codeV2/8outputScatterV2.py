import os
from termcolor import colored
import globals

def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

def generate_script(directory_path):
    try:
        # Get all files in the given directory
        filenames = os.listdir(directory_path)
        
        # Filter out non-desired files or directories
        filenames = [f for f in filenames if os.path.isfile(os.path.join(directory_path, f))]

        # Initialize the script with the header
        script = """%%dw 2.0
output application/java
---
{"""

        # For each filename, generate the corresponding line in the script
        for filename in filenames:
            name_without_extension = capitalize_first(os.path.splitext(filename)[0])
            line = f"\n\tTbl{name_without_extension}: payload..tbl{name_without_extension}_Obj[0],"
            script += line

        # Close the script's curly brace
        script += "\n}\n"

        return script
    except Exception as e:
        print(colored(f"Ocorreu um erro ao gerar o script: {e}", "red"))
        return None

def save_to_file(content, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(colored(f"Ocorreu um erro ao salvar o arquivo: {e}", "red"))

if __name__ == "__main__":
    directory_path = globals.OUTPUT_DIRECTORY_OUTPUT_RAML  # Replace with your directory path
    output_file_path = globals.OUTPUT_FILE_PATH_FINAL_OUTPUT_SCATTER  # Replace with desired output path/name
    
    try:
        result = generate_script(directory_path)
        if result:
            save_to_file(result, output_file_path)
            print(colored(f"Resultado salvo em {output_file_path}", "green"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
