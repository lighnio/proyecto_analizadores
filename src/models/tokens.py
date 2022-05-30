# Definicion de palabras reservadas

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

exports = tokens