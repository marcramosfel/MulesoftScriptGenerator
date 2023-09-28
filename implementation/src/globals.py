ROOT_DIRECTORY = "implementation\\utils"  # Diretório raiz
"""
str: Caminho para o diretório raiz onde estão localizados os utilitários.
"""

# Defina o caminho do arquivo
file_path = "implementation\\src\\config.txt"

# Leia o conteúdo do arquivo
with open(file_path, 'r') as file:
    INPUT_CSV_FILE = file.read()

#INPUT_CSV_FILE = "implementation\\utils\\inputCsv"
"""
str: Caminho para o arquivo CSV de entrada que contém referências.
"""

OUTPUT_DIRECTORY_INPUT_CSV = "implementation\\utils\\inputCsv"
"""
str: Diretório de saída onde os arquivos CSV de entrada são salvos.
"""

OUTPUT_DIRECTORY_OUTPUT_VARS = "implementation\\utils\\outputVars"
"""
str: Diretório de saída onde as variáveis são salvas.
"""

OUTPUT_DIRECTORY_OUTPUT_TYPE_LOGICAL = "implementation\\utils\\outputTypeLogical"
"""
str: Diretório de saída para os tipos lógicos.
"""

OUTPUT_DIRECTORY_OUTPUT_RAML = "implementation\\utils\\outputRaml"
"""
str: Diretório de saída para o arquivo RAML.
"""

OUTPUT_DIRECTORY_OUTPUT_FINAL_DATATYPE = "implementation\\utils\\outputFinalDataType"  
"""
str: Diretório de saída para o tipo de dado final.
"""

OUTPUT_FILE_PATH_FINAL_TRANSFORM_MESSAGE = "implementation\\utils\\outputFinalTransformMessage\\finalTransformMessage.xml"  
"""
str: Caminho do arquivo de saída para a mensagem de transformação final.
"""

OUTPUT_FILE_PATH_FINAL_SCATTER = "implementation\\utils\\outputFinalTransformMessage\\finalScatter.xml"
"""
str: Caminho do arquivo de saída para a operação de dispersão.
"""

OUTPUT_FILE_PATH_FINAL_OUTPUT_SCATTER = "implementation\\utils\\outputFinalTransformMessage\\finalOutputScatter.xml"
"""
str: Caminho do arquivo de saída para a saída da operação de dispersão.
"""

EXCLUDED_FIELDS =  ["q01_ANO", 
                    "q03_NIF",
                    "DesignacaoColunaIes",
                    "DesignacaoQuadroIes",
                    "DesignacaoCampoIes",
                    "CriacaoData",
                    "CriacaoUtilizadoId",
                    "AlteracaoData",
                    "AlteracaoUtilizadorId",
                    "ConsolidadoPedidoPagamentoDespesaId",
                    "CriacaoExternoPedidoPagamentoDespesaId",
                    "ConsolidadoPedidoPagamentoId",
                    "CriacaoExternoPedidoPagamentoId"
                    "ConsolidadoCriacaoSistemaId",
                    "ConsolidadoAlteracaoData",
                    "ConsolidadoAlteracaoSistemaId",
                    "ExternoAlteracaoUtilizadorId",
                    "ExternoAlteracaoData",
                    "ConsolidadoCriacaoData",
                    "ConsolidadoCriacaoSistemaId"]
"""
list of str: Lista de campos que devem ser excluídos do processamento.
"""

DBTYPES_LIST = {
    "datetime2": 2013,
    "array": 2003,
    "bigint": -5,
    "binary": -2,
    "bit": -7,
    "blob": 2004,
    "boolean": 16,
    "char": 1,
    "clob": 2005,
    "datalink": 70,
    "date": 91,
    "decimal": 3,
    "distinct": 2001,
    "double": 8,
    "float": 6,
    "integer": 4,
    "int": 4,
    "java_object": 2000,
    "longnvarchar": -16,
    "longvarbinary": -4,
    "longvarchar": -1,
    "nchar": -15,
    "nclob": 2011,
    "null": 0,
    "numeric": 2,
    "nvarchar": -9,
    "other": 1111,
    "real": 7,
    "ref": 2006,
    "ref_cursor": 2012,
    "rowid": -8,
    "smallint": 5,
    "sqlxml": 2009,
    "struct": 2002,
    "string": 12,
    "time": 92,
    "time_with_timezone": 2013,
    "timestamp": 93,
    "timestamp_with_timezone": 2014,
    "tinyint": -6,
    "varbinary": -3,
    "varchar": 12,
    '"': "wrong",
    '': "wrong"
}
"""
dict: Mapeia os nomes dos tipos de dados do banco de dados para os seus respectivos códigos numéricos.
"""

DATA_TYPE_MAP_SQL_TYPES_TO_RAML = {
    '': "",
    '"': "",
    'array': 'array',
    'binary': 'string',
    'bigint': 'integer',
    'bit': 'boolean',
    'blob': 'string',
    'boolean': 'boolean',
    'char': 'string',
    'clob': 'string',
    'date': 'date',
    'datetime2': 'datetime',
    'decimal': 'number',
    'double': 'number',
    'float': 'number',
    'int': 'integer',
    'integer': 'integer',
    'longnvarchar': 'string',
    'longvarbinary': 'string',
    'longvarchar': 'string',
    'nchar': 'string',
    'nclob': 'string',
    'null': 'nil',
    'numeric': 'number',
    'nvarchar': 'string',
    'real': 'number',
    'smallint': 'integer',
    'string': 'string | nil',
    'time': 'time',
    'time_with_timezone': 'time',
    'timestamp': 'datetime',
    'timestamp_with_timezone': 'datetime',
    'tinyint': 'integer',
    'varbinary': 'string',
    'varchar': 'string'
}
"""
dict: Mapeia os tipos de dados SQL para os seus respectivos tipos em RAML.
"""

DATA_TYPE_MAP_SQL_TYPES_TO_EXAMPLES = {
    '': '""',
    '"': '"quote"',
    'array': '"[1,2,3]"',
    'binary': 'b"1010"',
    'bigint': '1234567890',
    'bit': '1',
    'blob': '"blobdata"',
    'boolean': 'true',
    'char': '"c"',
    'clob': '"clobdata"',
    'datalink': '"http://example.com"',
    'date': '"2020-01-01"',
    'datetime': '"2020-01-01T00:00:00Z"',
    'datetime2': '"2020-01-01T00:00:00Z"',
    'decimal': '1.22',
    'distinct': '"distinctValue"',
    'double': '1.22',
    'float': '1.22',
    'int': '1',
    'integer': '1',
    'java_object': '"javaObj"',
    'longnvarchar': '"longNVarCharData"',
    'longvarbinary': 'b"longBinaryData"',
    'longvarchar': '"longVarCharData"',
    'nchar': '"nc"',
    'nclob': '"nclobdata"',
    'null': 'null',
    'numeric': '1.22',
    'nvarchar': '"nVarCharData"',
    'other': '"otherData"',
    'real': '1.22',
    'ref': '"refData"',
    'ref_cursor': '"refCursorData"',
    'rowid': '123',
    'smallint': '1',
    'sqlxml': '"<xml></xml>"',
    'struct': '"structData"',
    'time': '"00:00:00"',
    'time_with_timezone': '"00:00:00+01:00"',
    'timestamp': '"2020-01-01T00:00:00Z"',
    'timestamp_with_timezone': '"2020-01-01 00:00:00+01:00Z"',
    'tinyint': '1',
    'varbinary': 'b"1010"',
    'varchar': '"varCharData"'
}
"""
dict: Mapeia os tipos de dados SQL para exemplos representativos dos tipos.
"""
