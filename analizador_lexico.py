# Importes
# Modelos de Datos (Tokens)
from src.models.tokens import tokens, reservadas
from src.functions.leerFichero import datosFichero
# Paquetes
from ply import lex

###########################################
#              Tokens                     #
###########################################

reservadas = {
    'ent': 'TIPO_DATO_ENT',
    'dec': 'TIPO_DATO_DEC',
    'txt': 'TIPO_DATO_TXT',
    'bin': 'TIPO_DATO_BIN',
    'si': 'SENTENCIA_LOGICA_SI',
    'sino': 'SENTENCIA_LOGICA_SINO',
    'ciclo': 'SENTENCIA_LOGICA_CICLO',
    'mientras': 'SENTENCIA_LOGICA_MIENTRAS',
    'caso': 'SENTENCIA_LOGICA_OPCIONES',
    'romper': 'SENTENCIA_SALIDA_CICLOS',
    'devolver': 'SENTENCIA_RETORNO'
    
}


# Tokens para identificacion
tokens = [
    # Operaciones Aritmeticas
    'SIMBOLO_OPERACION_ARITMETICA_MAS',
    'SIMBOLO_OPERACION_ARITMETICA_MENOS',
    'SIMBOLO_OPERACION_ARITMETICA_POR',
    'SIMBOLO_OPERACION_ARITMETICA_DIVISION',
    'SIMBOLO_OPERACION_ARITMETICA_MOD',


    # Operaciones Logicas
    'SIMBOLO_OPERACION_LOGICA_MAYOR',
    'SIMBOLO_OPERACION_LOGICA_MENOR',
    'SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL',
    'SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL',
    'SIMBOLO_OPERACION_LOGICA_NO_IGUAL',
    'SIMBOLO_OPERACION_LOGICA_IGUAL',


    # Simbolos
    # Simbolos unicos
    'OPERADOR_ASIGNACION',
    'SIMBOLO_FIN_LINEA',
    'SIMBOLO_CADENA_TEXTO',
    'SIMBOLO_OPCIONES',

    # Simbolos Delimitadores
    'SIMBOLO_DELIMITADOR_APERTURA',
    'SIMBOLO_DELIMITADOR_CIERRE',
    'SIMBOLO_APERTURA_BLOQUE',
    'SIMBOLO_CIERRE_BLOQUE',
    'SIMBOLO_APERTURA_ARREGLO',
    'SIMBOLO_CIERRE_ARREGLO',

    
    # Tipos de Datos
    # 'TIPO_DATO_ENT',
    # 'TIPO_DATO_DEC',
    # 'TIPO_DATO_TXT',
    # 'TIPO_DATO_BIN',

    # Sentencias Logicas
    # Sentencias If
    # 'SENTENCIA_LOGICA_SI',
    # 'SENTENCIA_LOGICA_SINO',

    # Sentencias de Ciclos 
    # 'SENTENCIA_LOGICA_CICLO',
    # 'SENTENCIA_LOGICA_MIENTRAS',
    # 'SENTENCIA_LOGICA_OPCIONES',
    # 'SENTENCIA_LOGICA_CASO',
    # 'SENTENCIA_SALIDA_CICLOS',

    # Sentencias Especiales
    # 'SENTENCIA_RETORNO',
    'ID_VARIABLE',
    'NUMERO',
    'COMENTARIOS_UNA_LINEA',
    'COMENTARIOS_VARIAS_LINEAS',
    'TEXTO'
] + list(reservadas.values())


###########################################


# Carácteres ignorados, como espacios y tabulaciones
t_ignore = ' \t'

# Simbolos de Aritmetica
t_SIMBOLO_OPERACION_ARITMETICA_MAS = r'\+'
t_SIMBOLO_OPERACION_ARITMETICA_MENOS = r'\-'
t_SIMBOLO_OPERACION_ARITMETICA_POR = r'\*'
t_SIMBOLO_OPERACION_ARITMETICA_DIVISION = r'\/'
t_SIMBOLO_OPERACION_ARITMETICA_MOD = r'\%'

# Simbolos usados en Operaciones Lógicas
t_SIMBOLO_OPERACION_LOGICA_MAYOR = r'\>'
t_SIMBOLO_OPERACION_LOGICA_MENOR = r'\<'
t_SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL = r'\>='
t_SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL = r'\<='
t_SIMBOLO_OPERACION_LOGICA_NO_IGUAL = r'\!='
t_SIMBOLO_OPERACION_LOGICA_IGUAL = r'\=='

# Simbolos Únicos
t_OPERADOR_ASIGNACION = r'\='
t_SIMBOLO_FIN_LINEA = r'\;'
t_SIMBOLO_CADENA_TEXTO = r'\"'
t_SIMBOLO_OPCIONES = r'\:'

# Simbolos de Apertura y Cierre
t_SIMBOLO_DELIMITADOR_APERTURA = r'\('
t_SIMBOLO_DELIMITADOR_CIERRE = r'\)'
t_SIMBOLO_APERTURA_BLOQUE = r'\{'
t_SIMBOLO_CIERRE_BLOQUE = r'\}'
t_SIMBOLO_APERTURA_ARREGLO = r'\['
t_SIMBOLO_CIERRE_ARREGLO = r'\]'


# Definicion de Funciones Retornadoras de Información

# Retornará ID_VARIABLE, o Tipo de datos, o sentencias lógicas

def t_ID_TEXTO(t):
     r'".*"'
     t.type = reservadas.get(t.value,'TEXTO')    # Check for reserved words
     return t

def t_ID_VARIABLE(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID_VARIABLE')    # Check for reserved words
     return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Manejo de errores y carácteres ilegales.
def t_error(t):
    # almacenar = t.value[0].replace("\r", "SALTOLINEA")
    # print(t.value[0].replace("\r", ""), em)
    # if t.value[0] != r' \n':
    if t.value[0] != '\r':
        print(f'Carácter Ilegal: {(t.value[0])}')
        t.lexer.skip(1)
    else:
        t.lexer.skip(1)

# Definiendo el Analizador Léxico
analizador = lex.lex()

analizador.input(datosFichero())

# Tokenizando
while True:
    tok = analizador.token()
    if not tok: 
        break
    print(tok)