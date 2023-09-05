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

Claro! Integrando o exemplo de CSV ao trecho de documentação anterior:

---

### **Documentação para Importação de Tabelas**

---

#### **1. Introdução**

Esta documentação fornece um guia detalhado sobre como importar tabelas usando nosso sistema. A importação é feita através de arquivos CSV que devem seguir um padrão específico para garantir que a leitura seja realizada com sucesso.

---

#### **2. Formato do CSV**

O arquivo CSV usado para a importação deve seguir o formato especificado abaixo:

```
Tabela,Campo,Tipo de dados,Agregador
```

---

#### **3. Exemplo de CSV**

Aqui está um exemplo de como o CSV de input deve ser formatado:

```csv
Tabela,Campo,Tipo de dados,Agregador
tabela_A,campoA_id,bigint,tabela_A
tabela_A,campo_nome,varchar,tabela_A
tabela_A,campo_coluna,nchar,tabela_A
tabela_A,campo_data1,date,tabela_A
tabela_A,campo_data2,real,tabela_A
tabela_A,campo_data3,timestamp,tabela_A
tabela_A,campo_data4_SOMA,sqlxml,tabela_A
tabela_A,campo_data5,boolean,tabela_A
tabela_A,campo_data6,clob,tabela_A
tabela_A,campo_data7_SOMA,blob,tabela_A
tabela_A,campo_data8,numeric,tabela_A
tabela_A,campo_data9,datetime2,tabela_A
tabela_A,campo_data10,float,tabela_A
tabela_A,campo_data11,int,tabela_A
tabela_A,campo_data12,tinyint,tabela_A
tabela_A,campo_data13,time_with_timezone,tabela_A
tabela_A,campo_data14,decimal,tabela_A
tabela_A,campo_data15,datalink,tabela_A
tabela_A,campo_data16_SOMA,varbinary,tabela_A
tabela_A,campo_data17,java_object,tabela_A
tabela_A,campo_data18,time,tabela_A
tabela_A,campo_data19,timestamp_with_timezone,tabela_A
tabela_A,campo_data20,ref_cursor,tabela_A
tabela_A,campo_data21,struct,tabela_A
tabela_A,campo_data22_SOMA,longvarbinary,tabela_A
tabela_A,campo_data23_SOMA,other,tabela_A
tabela_A,campo_data24,smallint,tabela_A
tabela_A,campo_data25,ref,tabela_A
tabela_A,campo_data26,double,tabela_A
tabela_A,campo_data27,bit,tabela_A
tabela_A,data_criacao,nvarchar,tabela_A
tabela_A,id_criador,binary,tabela_A

```

---

#### **4. Instruções de Importação**

1. **Preparação do CSV**: Antes de iniciar a importação, certifique-se de que o arquivo CSV esteja formatado corretamente conforme o exemplo acima.
2. **Acess

## Funções

- `run_program(filename)`: Executa um programa específico.
- `run_all()`: Executa todos na sequência.
- `display_menu()`: Mostra o menu.

## Programas Inclusos

- `remove_all_files.py`: Limpa arquivos de uma pasta.
- `split_csv.py`: Divide um CSV.
- ... (e outros conforme listados anteriormente)
