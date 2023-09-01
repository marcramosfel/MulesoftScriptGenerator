import os
from termcolor import colored
import globals

def generate_yaml(files):
    yaml = "#%RAML 1.0 DataType\n\n"
    yaml += "uses:\n  objectLibrary: libs/object.raml\n\nproperties:\n"

    for filename in files:
        name_without_extension = os.path.splitext(filename)[0]

        if name_without_extension.endswith("[]"):
            name_without_extension = name_without_extension.replace("[]", "")
        yaml += f"  {name_without_extension}:\n"
        yaml += f"    type: objectLibrary.{name_without_extension}Null\n"
        yaml += "    required: false\n"

    return yaml

if __name__ == "__main__":
    input_directory = globals.OUTPUT_DIRECTORY_OUTPUT_RAML
    output_directory = globals.OUTPUT_DIRECTORY_OUTPUT_FINAL_DATATYPE 

    try:
        raml_files = [file for file in os.listdir(input_directory) if file.endswith(".raml")]

        if not raml_files:
            print(colored("No RAML files found in the directory.", "red"))
            exit()

        yaml_content = generate_yaml(raml_files)
        output_yaml = os.path.join(output_directory, 'output.yaml')

        with open(output_yaml, "w") as yaml_file:
            yaml_file.write(yaml_content)

        print(colored(f"\n\nYAML structure generated and saved as '{output_yaml}'\n", "green"))
    
    except FileNotFoundError:
        print(colored(f"Directory '{input_directory}' not found.", "red"))
    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}", "red"))
