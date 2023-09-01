import os
from termcolor import colored
import globals

def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

def generate_transform_block(file_content, filename):
    capitalize_filename = capitalize_first(filename)
    block = f"""
<route >
    <ee:transform doc:name="{filename.split('.dwl')[0]}" doc:id="b5fde3b1-0049-4b00-acd6-253c4c587459" >
        <ee:message >
            <ee:set-payload ><![CDATA[{file_content}]]></ee:set-payload>
        </ee:message>
    </ee:transform>
    <flow-ref doc:name="z-common-db-sql-types\\typesLogical-dynamic" doc:id="e3c41792-7809-4dfa-a17c-e38b8b917339" name="z-common-db-sql-types\\typesLogical-dynamic" />
    <ee:transform doc:name="{filename.split('.dwl')[0]}_Obj @dboName" doc:id="a3eb8e9a-7f3c-42fd-9ab2-1716fd7a0c0d" >
        <ee:message >
            <ee:set-payload ><![CDATA[%dw 2.0
output application/java
---
{{
     tbl{capitalize_filename.split('.dwl')[0]}_Obj: vars.dboName
}}]]></ee:set-payload>
        </ee:message>
    </ee:transform>
</route>
"""
    return block

def generate_code_from_directory(directory_path):
    all_code_blocks = []
    
    try:
        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                with open(os.path.join(directory_path, filename), 'r') as file:
                    file_content = file.read()
                    code_block = generate_transform_block(file_content, filename)
                    all_code_blocks.append(code_block)

        # Wrap all the blocks in <scatter-gather>
        return f"<scatter-gather doc:name=\"Scatter-Gather\" doc:id=\"AUTO_GENERATED_ID\" >\n{''.join(all_code_blocks)}\n</scatter-gather>"
    
    except Exception as e:
        print(colored(f"Ocorreu um erro ao gerar código a partir do diretório: {e}", "red"))
        return None

def save_to_file(content, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(colored(f"Ocorreu um erro ao salvar o arquivo: {e}", "red"))

if __name__ == "__main__":
    directory_path = globals.OUTPUT_DIRECTORY_OUTPUT_TYPE_LOGICAL  # Replace with your directory path
    output_file_path = globals.OUTPUT_FILE_PATH_FINAL_SCATTER  # Replace with desired output path/name
    
    try:
        result = generate_code_from_directory(directory_path)
        if result:
            save_to_file(result, output_file_path)
            print(colored(f"\n\nResultado salvo em {output_file_path}\n", "green"))
    except Exception as e:
        print(colored(f"Ocorreu um erro inesperado: {e}", "red"))
