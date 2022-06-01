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
    print("enunciado_sent")

def p_enunciado_expresion(p):
    '''enunciado : expresion'''
    p[0] = p[1]
    print("enunciado_expr")

def p_enunciado_multi(p):
    '''enunciado : enunciado enunciado'''
    p[0] = p[1] + p[2]
    print("enunciado_multi")





#sentencias
def p_sentencia_multi(p):
    '''sentencia : sentencia sentencia'''
    p[0] = p[1] + p[2]
    print("sentencia_multi")

def p_sentencia(p):
    '''sentencia : sentencia'''
    p[0] = p[1]
    print("sentencia")

def p_sentencia_romper(p):
    '''sentencia : romper'''
    p[0] = p[1]
    print("romper_ciclo") 

def p_sentencia_declara(p):
    '''sentencia : tipo_dato'''
    p[0] = p[1]
    print("sentencia_tipo") 

def p_sentencia_logica(p):
    '''sentencia : logica'''
    p[0] = p[1]
    print("sentencia_logica")

def p_sentencia_ciclo(p):
    '''sentencia : ciclo'''
    p[0] = p[1]
    print("sentencia_ciclo")  

def p_sentencia_mientras(p):
    '''sentencia : mientras'''
    p[0] = p[1]
    print("sentencia_mientras") 

#def p_sentencia_imprimir(p):
#    'sentencia : imprimir'
#    p[0] = p[1]
#   print("sentencia_imrpirmir")


#Pantalla
#def p_imprimir(p):
#    'imprimir : SALIDA_DE_PANTALLA SIMBOLO_FIN_LINEA'
#    p[0] = p[1] 


#Expresiones
def p_expresion_multi(p):
    '''expresion : expresion expresion'''
    p[0] = p[1] + p[2]
    print("expresion multi")

def p_expresion(p):
    '''expresion : expresion'''
    p[0] = p[1]
    print("expresion")

def p_expresion_operacion(p):
    '''expresion : operacion'''
    p[0] = p[1]
    print("expresion operacion")


#Operandos
def p_operando(p):
	'''operando : ID_VARIABLE
                | NUMERO'''
	p[0] = p[1]
	print("operando")

def p_operando_simbolo(p):
	'operando : SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERRE'
	p[0] = p[1] , p[3]
	print("operando_simbolo") 


# Tipos de datos
def p_tipo_dato(p):
    '''tipo_dato : TIPO_DATO_ENT ID_VARIABLE asignacion
                 | TIPO_DATO_DEC ID_VARIABLE decimal
                 | TIPO_DATO_TXT ID_VARIABLE asignacion
                 | TIPO_DATO_BIN ID_VARIABLE asignacion'''
    p[0] = p[1] + p[2] + p[3]
    print("TIPO_DATO")

# Asignación de datos
def p_asignacion_datos_val(p):
    '''asignacion : OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION ID_VARIABLE SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION operacion'''
    p[0] = p[1] 
    print('asignacion con valor')

def p_asignaciondec(p):
    'decimal : OPERADOR_ASIGNACION NUMERO SIMBOLO_DECIMAL NUMERO SIMBOLO_FIN_LINEA'
    p[0] = p[1]
    print('asignacion decimal')


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
                 | operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA
                 | operando OPERADOR_ASIGNACION operando SIMBOLO_FIN_LINEA'''
    p[0] = p[1] + p[3]
    print('operacion basica')

def p_operacion_basica_resumida(p):
    '''operacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS
                 | operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_FIN_LINEA'''
    p[0] = p[1]
    print('operacion basica resumida')


#relaciones
def p_relacionAsignacion(p):
    '''relacion : SIMBOLO_OPERACION_LOGICA_MAYOR
                | SIMBOLO_OPERACION_LOGICA_MENOR
                | SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL
                | SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL
                | SIMBOLO_OPERACION_LOGICA_NO_IGUAL
                | SIMBOLO_OPERACION_LOGICA_IGUAL '''
    p[0] = p[1]            
    print("relacion asignacion")

#logica
def p_logicasoloIF(p):
    'logica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = str([1]) + str(p[3]) + str(p[6])
    print('Sentencia_IF')

def p_logicaIFcompleto(p):
    'logica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE SENTENCIA_LOGICA_SINO SIMBOLO_APERTURA_BLOQUE operacion SIMBOLO_CIERRE_BLOQUE'
    p[0] = p[1]  + p[3] +  p[6]  + p[8]  + p[10]
    print('Sentencia_IF_ELSE')

def p_romer(p):
    'romper : SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA'

def p_logicaOP(p):
    'logicaOP : operando relacion operando'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])
    print('operacion logica')


#ciclos
def p_ciclo(p):
    'ciclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = p[1] + p[3] + p[4] + p[6] + p[9]
    print('ciclo')

def p_ciclo_romper(p):
    '''ciclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA enunciado SIMBOLO_CIERRE_BLOQUE
             | SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE  enunciado SENTENCIA_SALIDA_CICLOS  SIMBOLO_FIN_LINEA SIMBOLO_CIERRE_BLOQUE'''
    p[0] = p[1] + p[3] + p[4] + p[6] + p[9]
    print('ciclo roto')

def p_mientras(p):
    'mientras : SENTENCIA_LOGICA_MIENTRAS SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = p[1] + p[3] + p[6]
    print('ciclo mientras')


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