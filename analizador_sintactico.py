# Importes
# Modelos de Datos (Tokens)
# from src.models.tokens import tokens
from analizador_lexico import tokens
from src.functions.leerFichero import datosFichero
from analizador_semantico import *
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
    p[0] = program(p[1],"program")
    print("program")


def p_bloque(p):
    '''bloque : sentencia enunciado'''
    p[0] = bloque(p[1],p[2],"bloque")
    print("bloque")  


#enunciados
def p_enunciado_sentencia(p):
    '''enunciado : sentencia'''
    p[0] = enunciado_sentencia(p[1],"enunciado_sentencia")
    print("enunciado_sent")

def p_enunciado_expresion(p):
    '''enunciado : expresion'''
    p[0] = enunciado_expresion(p[1],"enunciado_expresion")
    print("enunciado_expr")

def p_enunciado_multi(p):
    '''enunciado : enunciado enunciado'''
    p[0] = enunciado_multi(p[1] , p[2],"enunciado_multi")
    print("enunciado_multi")





#sentencias
def p_sentencia_multi(p):
    '''sentencia : sentencia sentencia'''
    p[0] = sentencia_multi(p[1] , p[2],"sentencia_multi")
    print("sentencia_multi")

def p_sentencia(p):
    '''sentencia : sentencia'''
    p[0] = sentencia(p[1],"sentencia")
    print("sentencia")

def p_sentencia_romper(p):
    '''sentencia : romper'''
    p[0] = sentencia_romper(p[1],"sentencia_romper")
    print("romper_ciclo") 

def p_sentencia_declara(p):
    '''sentencia : tipo_dato'''
    p[0] =sentencia_declara(p[1],"sentencia_declara")
    print("sentencia_tipo") 

def p_sentencia_logica(p):
    '''sentencia : logica'''
    p[0] = sentencia_logica(p[1],"sentencia_logica")
    print("sentencia_logica")

def p_sentencia_ciclo(p):
    '''sentencia : ciclo'''
    p[0] = sentencia_ciclo(p[1],"sentencia_ciclo")
    print("sentencia_ciclo")  

def p_sentencia_mientras(p):
    '''sentencia : mientras'''
    p[0] = sentencia_mientras(p[1],"sentencia_mientras")
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
    p[0] = expresion_multi(p[1] , p[2],"expresion_multi")
    print("expresion multi")

def p_expresion(p):
    '''expresion : expresion'''
    p[0] = expresion(p[1],"expresion")
    print("expresion")

def p_expresion_operacion(p):
    '''expresion : operacion'''
    p[0] = expresion_operacion(p[1],"expresion_operacion")
    print("expresion operacion")


#Operandos
def p_operando(p):
	'''operando : ID_VARIABLE
                | NUMERO'''
	p[0] = operando(p[1],"operando")
	print("operando")

def p_operando_simbolo(p):
	'operando : SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERRE'
	p[0] = operando_simbolo(p[1] , p[2] , p[3],"operando_simbolo")
	print("operando_simbolo") 


# Tipos de datos
def p_tipo_dato(p):
    '''tipo_dato : TIPO_DATO_ENT ID_VARIABLE asignacion
                 | TIPO_DATO_DEC ID_VARIABLE decimal
                 | TIPO_DATO_TXT ID_VARIABLE asignacion
                 | TIPO_DATO_BIN ID_VARIABLE asignacion'''
    p[0] = tipo_dato(p[1] , p[2] , p[3],"tipo_dato")
    print("TIPO_DATO")

# Asignación de datos
def p_asignacion_datos_val(p):
    '''asignacion : OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA
                  | OPERADOR_ASIGNACION ID_VARIABLE SIMBOLO_FIN_LINEA'''
    p[0] = asignacion_datos_val(p[1],p[2],p[3],"asignacion_datos_val")
    print('asignacion con valor')

def p_asignacion_datos_val_op(p):
    'asignacion : OPERADOR_ASIGNACION operacion'
    p[0] = asignacion_datos_val_op(p[1] ,p[2],"asignacion_datos_val_op")
    print('asignacion con valor')

def p_asignaciondec(p):
    'decimal : OPERADOR_ASIGNACION NUMERO SIMBOLO_DECIMAL NUMERO SIMBOLO_FIN_LINEA'
    p[0] = asignaciondec(p[1],p[2],p[3],p[4],p[5],"asignaciondec")
    print('asignacion decimal')


def p_asignacion_datos_No_val(p):
    'asignacion : SIMBOLO_FIN_LINEA'
    p[0] = asignacion_datos_No_val(p[1],"asignacion_datos_No_val")
    print('asignacion sin valor')

#operacion
def p_operacion_basica(p):
    '''operacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA
                 | operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA
                 | operando OPERADOR_ASIGNACION operando SIMBOLO_FIN_LINEA'''
    p[0] = operacion_basica(p[1] ,p[2] , p[3] , p[4],"operacion_basica")
    print('operacion basica')

def p_operacion_basica_resumida(p):
    'operacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS'
    p[0] = operacion_basica_resumida(p[1],p[2],p[3],"operacion_basica_resumida")
    print('operacion basica resumida')

def p_operacion_basica_resumida_fin(p):
    'operacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_FIN_LINEA'
    p[0] = operacion_basica_resumida_fin(p[1],p[2],p[3],p[4],"operacion_basica_resumida_fin")
    print('operacion basica resumida fin')


#relaciones
def p_relacionAsignacion(p):
    '''relacion : SIMBOLO_OPERACION_LOGICA_MAYOR
                | SIMBOLO_OPERACION_LOGICA_MENOR
                | SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL
                | SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL
                | SIMBOLO_OPERACION_LOGICA_NO_IGUAL
                | SIMBOLO_OPERACION_LOGICA_IGUAL '''
    p[0] = relacionAsignacion(p[1],"relacionAsignacion")            
    print("relacion asignacion")

#logica
def p_logicasoloIF(p):
    'logica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = logicasoloIF([1] ,p[2],p[3],p[4],p[5],p[6],p[7],"logicasoloIF")
    print('Sentencia_IF')

def p_logicaIFcompleto(p):
    'logica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE SENTENCIA_LOGICA_SINO SIMBOLO_APERTURA_BLOQUE operacion SIMBOLO_CIERRE_BLOQUE'
    p[0] = logicaIFcompleto(p[1]  ,p[2] , p[3] , p[4] , p[5] ,  p[6] , p[7] , p[8]  , p[9] ,  p[10],p[11],"logicaIFcompleto")
    print('Sentencia_IF_ELSE')

def p_romer(p):
    'romper : SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA'
    p[0] = romer(p[1], p[2], "romer")

def p_logicaOP(p):
    'logicaOP : operando relacion operando'
    p[0] = logicaOP(p[1] ,p[2],p[3],"logicaOP")
    print('operacion logica')


#ciclos
def p_ciclo(p):
    'ciclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = ciclo(p[1] ,p[2] ,  p[3] , p[4] , p[5] ,  p[6] , p[7] , p[8] , p[9],p[10] ,"ciclo")
    print('ciclo')

def p_ciclo_romper(p):
    '''ciclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA enunciado SIMBOLO_CIERRE_BLOQUE
             | SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE  enunciado SENTENCIA_SALIDA_CICLOS  SIMBOLO_FIN_LINEA SIMBOLO_CIERRE_BLOQUE'''
    p[0] = ciclo_romper(p[1], p[2] ,  p[3] , p[4] , p[5] ,  p[6] , p[7] , p[8] , p[9], p[10] , p[11] , p[12] , "ciclo_romper")
    print('ciclo roto')

def p_mientras(p):
    'mientras : SENTENCIA_LOGICA_MIENTRAS SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    p[0] = mientras(p[1] ,p[2],p[3] , p[4] , p[5] ,p[6], p[7],"mientras")
    print('ciclo mientras')


# Error rule for syntax errors



# Definiendo el analizador sintáctico
#yacc()

# for clas in dir(parser):
#     print(clas)

# Bucle para analizar y validar


def traducir(analizador):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(analizador.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

analizador = yacc().parse(datosFichero())

#AST



traducir(analizador)

#analizador.imprimir("")
#print(analizador.traducir())

#graphFile = open('graphviztrhee,vz','w')
#graphFile.write(analizador.traudcir())
#graphFile.close()








# while True:
#     try:
#         s = input('analizador sintactico > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = yacc().parse(s, debug=0)
#     print(result)