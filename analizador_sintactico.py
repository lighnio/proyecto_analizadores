# Importes
# Modelos de Datos (Tokens)
# from src.models.tokens import tokens
from analizador_lexico import tokens

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

def p_expression_mas(p):
    'expression : ID_VARIABLE SIMBOLO_OPERACION_ARITMETICA_MAS ID_VARIABLE'
    p[0] = p[1] + p[3]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Definiendo el analizador sintáctico
yacc()

# for clas in dir(parser):
#     print(clas)

# Bucle para analizar y validar
while True:
    try:
        s = input('analizador sintactico > ')
    except EOFError:
        break
    if not s: continue
    result = yacc().parse(s, debug=1)
    print(result)