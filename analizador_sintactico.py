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

def p_program(p):
    '''program : bloque'''
    p[0] = p[1]
    print("program")


def p_bloque(p):
    '''bloque : sentencia enunciado'''
    p[0] = p[1]
    print("bloque")  

#enunciados
def p_enunciado_sentencia(p):
    '''enunciado : sentencia'''
    p[0] = p[1]
    print("sentencia")

def p_enunciado_expresion(p):
    '''enunciado : expresion'''
    p[0] = p[1]
    print("sentencia")

def p_enunciado_multi(p):
    '''enunciado : enunciado enunciado'''
    p[0] = p[1] + p[2]
    print("sentencia")

#sentencias
def p_sentencia_multi(p):
    '''sentencia : sentencia sentencia'''
    p[0] = p[1] + p[2]
    print("sentencia")

def p_sentencia(p):
    '''sentencia : sentencia'''
    p[0] = p[1]
    print("sentencia")
   

def p_sentencia_declara(p):
    '''sentencia : tipo_dato'''
    p[0] = p[1]
    print("sentencia") 



#Expresiones
def p_expresion(p):
    '''expresion : expresion expresion'''
    p[0] = p[1] + p[2]
    print("expresion")

def p_expresion(p):
    '''expresion : expresion'''
    p[0] = p[1]
    print("expresion")

def p_expresion(p):
    '''expresion : operacion'''
    p[0] = p[1]
    print("expresion")


#Operandos
def p_operando(p):
	'''operando : ID_VARIABLE
                | NUMERO
                | SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERRE'''
	p[0] = p[1]
	print("operando")    

# Tipos de datos
def p_tipo_dato(p):
    '''tipo_dato : TIPO_DATO_ENT ID_VARIABLE asignacion
                 | TIPO_DATO_DEC ID_VARIABLE asignacion
                 | TIPO_DATO_TXT ID_VARIABLE asignacion
                 | TIPO_DATO_BIN ID_VARIABLE asignacion'''
    p[0] = p[1] + p[2]
    print("TIPO_DATO")

# Asignación de datos
def p_asignacion_datos_val(p):
    '''asignacion : OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA'''
    p[0] = p[1] + p[3]
    print('asignacion con valor')

def p_asignacion_datos_No_val(p):
    'asignacion : SIMBOLO_FIN_LINEA'
    p[0] = p[1]
    print('asignacion sin valor')

#operacion
def p_operacion_basica(p):
    '''operacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA'''
    p[0] = p[1]  + p[3]
    print('operacion basica')


# Error rule for syntax errors



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