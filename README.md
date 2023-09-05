# README.md

---

## 🚀 MuleSoft Script Generator 🚀

### Descrição:

Este script é um utilitário que fornece um menu interativo para executar uma série de programas relacionados ao MuleSoft. Ele tem a capacidade de executar scripts individualmente ou em conjunto, de acordo com a escolha do usuário que facilitaram a escrita de código Mulesoft dwl.


🚀 **Guia de Configuração e Execução do Mulesoft Script Generator** 🚀

Siga estes passos simples para configurar e executar o programa no seu sistema:

1. **Executar CMD com Permissões de Administrador**:
    - Pressione `Win` + `S` para abrir a busca.
    - Digite "cmd" ou "Prompt de Comando".
    - Clique com o botão direito no "Prompt de Comando" e selecione "Executar como administrador".

2. 🐍 **Instalar Python com PIP**:
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```

3. 📂 **Navegar até a Pasta do Projeto**:
    ```bash
    cd caminho\para\a\pasta\mulesoft_script_generator
    ```

4. 📦 **Instalar Dependências**:
    - Dentro da pasta `mulesoft_script_generator`, instale as dependências necessárias usando o arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5. 🚀 **Executar o Script**:
    ```bash
    python implementation\src\mulesoft_generator_script.py
    ```

Pronto! Agora você deve estar com o Mulesoft Script Generator rodando em sua máquina! 🎉🎈

---
### Início Rápido

Navegue até a pasta `implementation\src`.
Execute o arquivo `mulesoft_generator_script.py` para iniciar o programa.
Siga as instruções na interface do programa para completar as ações desejadas.

Claro! Aqui está um guia passo a passo para o `README`:

---

---

📚 **Documentação do Mulesoft Script Generator** 📚

Quer mergulhar profundamente nos segredos do Mulesoft Script Generator? Nós preparamos uma documentação detalhada para guiar sua jornada! 🚀

1. 📂 **Encontrando a Documentação**:
   - Navegue até `docs\build\html` na pasta principal do projeto.

2. 🌍 **Abra a Porta para o Conhecimento**:
   - Dê um duplo clique no arquivo `index.html` para abri-lo em seu navegador padrão. Este é o seu ponto de partida para o maravilhoso mundo da nossa documentação! 🚪🔍

3. 🧐 **Explore**:
   - Agora, você está livre para explorar! A documentação oferece uma visão detalhada de cada aspecto do Mulesoft Script Generator. Desejamos a você uma leitura frutífera e esclarecedora! 📖💡

Dica: Sempre comece pelo `index.html` para obter a visão completa e a melhor experiência de navegação.

Boa leitura e exploração! 🎉🎓

---

### Requisitos:

- Python 3.x
- Biblioteca `termcolor`
<<<<<<< Updated upstream
=======
- Biblioteca `codecs`
- Biblioteca `os`
- Biblioteca `csv`
- Biblioteca `tkinter`


>>>>>>> Stashed changes

### Como usar:

1. Certifique-se de ter todos os programas listados na lista `programs_to_run` no local correto.
2. Execute o script principal:
```
<<<<<<< Updated upstream
python nome_do_script_principal.py
=======
python mulesoft_generator_script.py
>>>>>>> Stashed changes
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