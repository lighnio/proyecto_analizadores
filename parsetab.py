
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMENTARIOS_UNA_LINEA COMENTARIOS_VARIAS_LINEAS ID_VARIABLE NUMERO OPERADOR_ASIGNACION SENTENCIA_LOGICA_CICLO SENTENCIA_LOGICA_MIENTRAS SENTENCIA_LOGICA_OPCIONES SENTENCIA_LOGICA_SI SENTENCIA_LOGICA_SINO SENTENCIA_RETORNO SENTENCIA_SALIDA_CICLOS SIMBOLO_APERTURA_ARREGLO SIMBOLO_APERTURA_BLOQUE SIMBOLO_CADENA_TEXTO SIMBOLO_CIERRE_ARREGLO SIMBOLO_CIERRE_BLOQUE SIMBOLO_DELIMITADOR_APERTURA SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_FIN_LINEA SIMBOLO_OPCIONES SIMBOLO_OPERACION_ARITMETICA_DIVISION SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MENOS SIMBOLO_OPERACION_ARITMETICA_MOD SIMBOLO_OPERACION_ARITMETICA_POR SIMBOLO_OPERACION_LOGICA_IGUAL SIMBOLO_OPERACION_LOGICA_MAYOR SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL SIMBOLO_OPERACION_LOGICA_MENOR SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL SIMBOLO_OPERACION_LOGICA_NO_IGUAL TEXTO TIPO_DATO_BIN TIPO_DATO_DEC TIPO_DATO_ENT TIPO_DATO_TXTprogram : bloquebloque : sentencia enunciadoenunciado : sentenciaenunciado : expresionenunciado : enunciado enunciadosentencia : sentencia sentenciasentencia : sentenciasentencia : tipo_datoexpresion : operacionoperando : ID_VARIABLE\n                | NUMERO\n                | SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERREtipo_dato : TIPO_DATO_ENT ID_VARIABLE asignacion\n                 | TIPO_DATO_DEC ID_VARIABLE asignacion\n                 | TIPO_DATO_TXT ID_VARIABLE asignacion\n                 | TIPO_DATO_BIN ID_VARIABLE asignacionasignacion : OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA\n                  | OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEAasignacion : SIMBOLO_FIN_LINEAoperacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA'
    
_lr_action_items = {'TIPO_DATO_ENT':([0,3,4,9,10,11,12,21,22,23,30,32,33,34,35,44,45,46,47,48,49,50,],[5,5,-8,5,5,-4,-9,5,5,5,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'TIPO_DATO_DEC':([0,3,4,9,10,11,12,21,22,23,30,32,33,34,35,44,45,46,47,48,49,50,],[6,6,-8,6,6,-4,-9,6,6,6,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'TIPO_DATO_TXT':([0,3,4,9,10,11,12,21,22,23,30,32,33,34,35,44,45,46,47,48,49,50,],[7,7,-8,7,7,-4,-9,7,7,7,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'TIPO_DATO_BIN':([0,3,4,9,10,11,12,21,22,23,30,32,33,34,35,44,45,46,47,48,49,50,],[8,8,-8,8,8,-4,-9,8,8,8,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'$end':([1,2,4,9,10,11,12,21,22,23,30,32,33,34,35,44,45,46,47,48,49,50,],[0,-1,-8,-3,-2,-4,-9,-6,-3,-5,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'ID_VARIABLE':([3,4,5,6,7,8,9,10,11,12,21,22,23,24,25,26,27,28,30,32,33,34,35,44,45,46,47,48,49,50,],[13,-8,17,18,19,20,-3,13,-4,-9,-6,-3,13,13,13,13,13,13,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'NUMERO':([3,4,9,10,11,12,16,21,22,23,24,25,26,27,28,30,31,32,33,34,35,44,45,46,47,48,49,50,],[15,-8,-3,15,-4,-9,29,-6,-3,15,15,15,15,15,15,-13,42,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'SIMBOLO_DELIMITADOR_APERTURA':([3,4,9,10,11,12,21,22,23,24,25,26,27,28,30,32,33,34,35,44,45,46,47,48,49,50,],[16,-8,-3,16,-4,-9,-6,-3,16,16,16,16,16,16,-13,-19,-14,-15,-16,-20,-21,-22,-23,-24,-17,-18,]),'SIMBOLO_OPERACION_ARITMETICA_MAS':([13,14,15,41,],[-10,24,-11,-12,]),'SIMBOLO_OPERACION_ARITMETICA_MENOS':([13,14,15,41,],[-10,25,-11,-12,]),'SIMBOLO_OPERACION_ARITMETICA_POR':([13,14,15,41,],[-10,26,-11,-12,]),'SIMBOLO_OPERACION_ARITMETICA_DIVISION':([13,14,15,41,],[-10,27,-11,-12,]),'SIMBOLO_OPERACION_ARITMETICA_MOD':([13,14,15,41,],[-10,28,-11,-12,]),'SIMBOLO_FIN_LINEA':([13,15,17,18,19,20,36,37,38,39,40,41,42,43,],[-10,-11,32,32,32,32,44,45,46,47,48,-12,49,50,]),'OPERADOR_ASIGNACION':([17,18,19,20,],[31,31,31,31,]),'SIMBOLO_DELIMITADOR_CIERRE':([29,],[41,]),'TEXTO':([31,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'bloque':([0,],[2,]),'sentencia':([0,3,9,10,21,22,23,],[3,9,21,22,21,21,22,]),'tipo_dato':([0,3,9,10,21,22,23,],[4,4,4,4,4,4,4,]),'enunciado':([3,10,23,],[10,23,23,]),'expresion':([3,10,23,],[11,11,11,]),'operacion':([3,10,23,],[12,12,12,]),'operando':([3,10,23,24,25,26,27,28,],[14,14,14,36,37,38,39,40,]),'asignacion':([17,18,19,20,],[30,33,34,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> bloque','program',1,'p_program','analizador_sintactico.py',26),
  ('bloque -> sentencia enunciado','bloque',2,'p_bloque','analizador_sintactico.py',32),
  ('enunciado -> sentencia','enunciado',1,'p_enunciado_sentencia','analizador_sintactico.py',38),
  ('enunciado -> expresion','enunciado',1,'p_enunciado_expresion','analizador_sintactico.py',43),
  ('enunciado -> enunciado enunciado','enunciado',2,'p_enunciado_multi','analizador_sintactico.py',48),
  ('sentencia -> sentencia sentencia','sentencia',2,'p_sentencia_multi','analizador_sintactico.py',54),
  ('sentencia -> sentencia','sentencia',1,'p_sentencia','analizador_sintactico.py',59),
  ('sentencia -> tipo_dato','sentencia',1,'p_sentencia_declara','analizador_sintactico.py',65),
  ('expresion -> operacion','expresion',1,'p_expresion','analizador_sintactico.py',83),
  ('operando -> ID_VARIABLE','operando',1,'p_operando','analizador_sintactico.py',90),
  ('operando -> NUMERO','operando',1,'p_operando','analizador_sintactico.py',91),
  ('operando -> SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERRE','operando',3,'p_operando','analizador_sintactico.py',92),
  ('tipo_dato -> TIPO_DATO_ENT ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',98),
  ('tipo_dato -> TIPO_DATO_DEC ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',99),
  ('tipo_dato -> TIPO_DATO_TXT ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',100),
  ('tipo_dato -> TIPO_DATO_BIN ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',101),
  ('asignacion -> OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA','asignacion',3,'p_asignacion_datos_val','analizador_sintactico.py',107),
  ('asignacion -> OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA','asignacion',3,'p_asignacion_datos_val','analizador_sintactico.py',108),
  ('asignacion -> SIMBOLO_FIN_LINEA','asignacion',1,'p_asignacion_datos_No_val','analizador_sintactico.py',113),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',119),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',120),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',121),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',122),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',123),
]
