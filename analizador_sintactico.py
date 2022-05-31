# Importes
# Modelos de Datos (Tokens)
# from src.models.tokens import tokens
from analizador_lexico import tokens
from src.functions.leerFichero import datosFichero

# Paquetes
from ply.yacc import yacc

# Definiciones
# precedencia = (
#     ('right', 'ID', 'IF', 'WHILE'),
# 	('right', 'VAR'),
#     ('right', 'OPERADOR_ASIGNACION'),
#     ('left', 'SIMBOLO_OPERACION_LOGICA_NO_IGUAL'),
#     ('left', 'SIMBOLO_OPERACION_LOGICA_MENOR', 'SIMBOLO_OPERACION_LOGICA_MAYOR',
#      'SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL', 'SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL'),
#     ('left', 'SIMBOLO_OPERACION_ARITMETICA_MAS',
#      'SIMBOLO_OPERACION_ARITMETICA_MENOS'),
#     ('left', 'SIMBOLO_OPERACION_ARITMETICA_POR',
#      'SIMBOLO_OPERACION_ARITMETICA_DIVISION'),
#     ('left', 'SIMBOLO_DELIMITADOR_APERTURA', 'SIMBOLO_DELIMITADOR_CIERRE')
# )


# Tipos de datos

def p_tipo_dato_ent(p):
    'tipo_dato : TIPO_DATO_ENT ID_VARIABLE'
    p[0] = p[1] + p[2]
    print("TIPO_DATO_ENT")

def p_tipo_dato_dec(p):
    'tipo_dato : TIPO_DATO_DEC ID_VARIABLE'
    p[0] = p[1] + p[2]
    print("TIPO_DATO_DEC")

def p_tipo_dato_txt(p):
    'tipo_dato : TIPO_DATO_TXT ID_VARIABLE'
    p[0] = p[1] + p[2]
    print("TIPO_DATO_TXT")

def p_tipo_dato_bin(p):
    'tipo_dato : TIPO_DATO_BIN ID_VARIABLE'
    p[0] = p[1] + p[2]
    print("TIPO_DATO_BIN")

# Asignación de datos
def p_asignacion_datos(p):
    'asignacion : ID_VARIABLE OPERADOR_ASIGNACION NUMERO'
    p[0] = p[1] + p[3]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    if p.value[0] == r'\r':
        print(dir(p))

# Definiendo el analizador sintáctico
#yacc()

# for clas in dir(parser):
#     print(clas)

# Bucle para analizar y validar

analizador = yacc().parse(datosFichero())
# while True:
#     try:
#         s = input('analizador sintactico > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = yacc().parse(s, debug=0)
#     print(result)