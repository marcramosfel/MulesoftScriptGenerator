# 🚀 MuleSoft Script Generator 🚀

## Índice

- [Descrição](#descrição)
- [Guia de Configuração e Execução](#guia-de-configuração-e-execução)
- [Início Rápido](#início-rápido)
- [Documentação Detalhada](#documentação-do-mulesoft-script-generator)
- [Requisitos](#requisitos)
- [Como Usar](#como-usar)
- [Funções](#funções)
- [Programas Inclusos](#programas-inclusos)
- [Contribuições](#contribuições)
- [Suporte](#suporte)
- [Licença](#licença)
- [Agradecimentos](#agradecimentos)

## Descrição

Este script é um utilitário que fornece um menu interativo para executar uma série de programas relacionados ao MuleSoft. Ele tem a capacidade de executar scripts individualmente ou em conjunto, facilitando a escrita de código Mulesoft dwl.

## Guia de Configuração e Execução

1. **Executar CMD com Permissões de Administrador**:
   - Pressione `Win` + `S` para abrir a busca.
   - Digite "cmd" ou "Prompt de Comando".
   - Clique com o botão direito e selecione "Executar como administrador".

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
   ```bash
   pip install -r requirements.txt
   ```

5. 🚀 **Executar o Script**:
   ```bash
   python implementation\src\mulesoft_generator_script.py
   ```

## Início Rápido

- Navegue até a pasta `implementation\src`.
- Execute `mulesoft_generator_script.py` para iniciar o programa.
- Siga as instruções na tela.

## Documentação do Mulesoft Script Generator

1. 📂 **Encontrando a Documentação**:
   - Vá até `docs\build\html` na pasta principal.
   
2. 🌍 **Iniciar a Jornada**:
   - Abra `index.html` em seu navegador. Esta é a porta de entrada para nossa documentação!

3. 🧐 **Explore**:
   - Navegue e aprenda mais sobre o Mulesoft Script Generator.

## Requisitos

- Python 3.x
- `termcolor`, `codecs`, `os`, `csv`

## Como Usar

1. Assegure-se de que todos os programas em `programs_to_run` estejam no local correto.
2. Execute o script principal:
   ```bash
   python mulesoft_generator_script.py
   ```

3. Um menu será exibido. Escolha a opção desejada.

## Funções

- `run_program(filename)`: Executa um programa específico.
- `run_all()`: Executa todos na sequência.
- `display_menu()`: Mostra o menu.

## Programas Inclusos

- `remove_all_files.py`: Limpa arquivos de uma pasta.
- `split_csv.py`: Divide um CSV.
- ... (e outros conforme listados anteriormente)
