# README.md

---

## 🚀 MuleSoft Script Generator 🚀

### Descrição:

Este script é um utilitário que fornece um menu interativo para executar uma série de programas relacionados ao MuleSoft. Ele tem a capacidade de executar scripts individualmente ou em conjunto, de acordo com a escolha do usuário.

### Requisitos:

- Python 3.x
- Biblioteca `termcolor`

### Como usar:

1. Certifique-se de ter todos os programas listados na lista `programs_to_run` no local correto.
2. Execute o script principal:
```
python nome_do_script_principal.py
```
3. Um menu será exibido mostrando todos os programas disponíveis para execução. Escolha a opção desejada digitando o número correspondente.

### Funções:

- `run_program(filename)`: Executa um programa específico.
- `run_all()`: Executa todos os programas na ordem em que estão listados.
- `display_menu()`: Exibe o menu interativo e aguarda a escolha do usuário.

### Programas inclusos:

Aqui estão os programas que este utilitário pode executar:

- `remove_all_files.py`: Remove todos os arquivos de uma pasta especificada.
- `split_csv.py`: Divide um arquivo CSV em múltiplos arquivos baseados em um agrupador.
- `csv_to_variable.py`: Converte um CSV em uma variável (descrição específica não fornecida).
- `csv_to_type_logical.py`: Transforma dados CSV em um tipo lógico.
- `csv_to_raml.py`: Converte informações de um CSV para o formato RAML.
- `create_datatype.py`: Cria um novo tipo de dado (descrição específica não fornecida).
- `variable_to_transform_message.py`: Converte uma variável em uma mensagem transformadora.
- `type_logical_to_scatter_gather.py`: Converte um tipo lógico em um bloco scatter-gather.
- `output_scatter_gather.py`: Gera um código de saída para um bloco scatter-gather.
- `globals.py`: Define constantes e variáveis globais para o projeto.

### Contribuição:

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork, realizar suas alterações e criar um Pull Request.

---

Espero que isso ajude a esclarecer o propósito e o uso dos scripts contidos neste projeto. Por favor, lembre-se de sempre fazer backup de seus arquivos e testar os scripts em um ambiente seguro antes de usar em produção.