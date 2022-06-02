
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMENTARIOS_UNA_LINEA COMENTARIOS_VARIAS_LINEAS ID_VARIABLE LECTURA_DE_TECLADO NUMERO OPERADOR_ASIGNACION SALIDA_DE_PANTALLA SENTENCIA_LOGICA_CICLO SENTENCIA_LOGICA_MIENTRAS SENTENCIA_LOGICA_OPCIONES SENTENCIA_LOGICA_SI SENTENCIA_LOGICA_SINO SENTENCIA_RETORNO SENTENCIA_SALIDA_CICLOS SIMBOLO_APERTURA_ARREGLO SIMBOLO_APERTURA_BLOQUE SIMBOLO_CADENA_TEXTO SIMBOLO_CIERRE_ARREGLO SIMBOLO_CIERRE_BLOQUE SIMBOLO_DECIMAL SIMBOLO_DELIMITADOR_APERTURA SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_FIN_LINEA SIMBOLO_OPCIONES SIMBOLO_OPERACION_ARITMETICA_DIVISION SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MENOS SIMBOLO_OPERACION_ARITMETICA_MOD SIMBOLO_OPERACION_ARITMETICA_POR SIMBOLO_OPERACION_LOGICA_IGUAL SIMBOLO_OPERACION_LOGICA_MAYOR SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL SIMBOLO_OPERACION_LOGICA_MENOR SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL SIMBOLO_OPERACION_LOGICA_NO_IGUAL TEXTO TIPO_DATO_BIN TIPO_DATO_DEC TIPO_DATO_ENT TIPO_DATO_TXTprogram : bloquebloque : sentencia enunciadoenunciado : sentenciaenunciado : expresionenunciado : enunciado enunciadosentencia : sentencia sentenciasentencia : sentenciasentencia : rompersentencia : tipo_datosentencia : logicasentencia : ciclosentencia : mientrasexpresion : expresion expresionexpresion : expresionexpresion : operacionoperando : ID_VARIABLE\n                | NUMEROoperando : SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERREtipo_dato : TIPO_DATO_ENT ID_VARIABLE asignacion\n                 | TIPO_DATO_DEC ID_VARIABLE decimal\n                 | TIPO_DATO_TXT ID_VARIABLE asignacion\n                 | TIPO_DATO_BIN ID_VARIABLE asignacionasignacion : OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA\n                  | OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA\n                  | OPERADOR_ASIGNACION ID_VARIABLE SIMBOLO_FIN_LINEAasignacion : OPERADOR_ASIGNACION operaciondecimal : OPERADOR_ASIGNACION NUMERO SIMBOLO_DECIMAL NUMERO SIMBOLO_FIN_LINEAasignacion : SIMBOLO_FIN_LINEAoperacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA\n                 | operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA\n                 | operando OPERADOR_ASIGNACION operando SIMBOLO_FIN_LINEAoperacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MASoperacion : operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_FIN_LINEArelacion : SIMBOLO_OPERACION_LOGICA_MAYOR\n                | SIMBOLO_OPERACION_LOGICA_MENOR\n                | SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL\n                | SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL\n                | SIMBOLO_OPERACION_LOGICA_NO_IGUAL\n                | SIMBOLO_OPERACION_LOGICA_IGUAL logica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUElogica : SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE SENTENCIA_LOGICA_SINO SIMBOLO_APERTURA_BLOQUE operacion SIMBOLO_CIERRE_BLOQUEromper : SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEAlogicaOP : operando relacion operandociclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUEciclo : SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA enunciado SIMBOLO_CIERRE_BLOQUE\n             | SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE  enunciado SENTENCIA_SALIDA_CICLOS  SIMBOLO_FIN_LINEA SIMBOLO_CIERRE_BLOQUEmientras : SENTENCIA_LOGICA_MIENTRAS SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE'
    
_lr_action_items = {'SENTENCIA_SALIDA_CICLOS':([0,3,4,5,6,7,8,17,18,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[9,9,-8,-9,-10,-11,-12,9,9,-4,-15,-45,9,9,9,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,9,9,9,9,-27,-43,-50,105,108,-47,9,-44,-45,9,-49,-48,]),'TIPO_DATO_ENT':([0,3,4,5,6,7,8,17,18,19,20,25,31,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[10,10,-8,-9,-10,-11,-12,10,10,-4,-15,-45,10,10,10,10,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,10,10,10,10,-27,-43,-50,10,10,-47,10,-44,-45,10,-49,-48,]),'TIPO_DATO_DEC':([0,3,4,5,6,7,8,17,18,19,20,25,31,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[11,11,-8,-9,-10,-11,-12,11,11,-4,-15,-45,11,11,11,11,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,11,11,11,11,-27,-43,-50,11,11,-47,11,-44,-45,11,-49,-48,]),'TIPO_DATO_TXT':([0,3,4,5,6,7,8,17,18,19,20,25,31,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[12,12,-8,-9,-10,-11,-12,12,12,-4,-15,-45,12,12,12,12,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,12,12,12,12,-27,-43,-50,12,12,-47,12,-44,-45,12,-49,-48,]),'TIPO_DATO_BIN':([0,3,4,5,6,7,8,17,18,19,20,25,31,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[13,13,-8,-9,-10,-11,-12,13,13,-4,-15,-45,13,13,13,13,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,13,13,13,13,-27,-43,-50,13,13,-47,13,-44,-45,13,-49,-48,]),'SENTENCIA_LOGICA_SI':([0,3,4,5,6,7,8,17,18,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[14,14,-8,-9,-10,-11,-12,14,14,-4,-15,-45,14,14,14,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,14,14,14,14,-27,-43,-50,14,14,-47,14,-44,-45,14,-49,-48,]),'SENTENCIA_LOGICA_CICLO':([0,3,4,5,6,7,8,17,18,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[15,15,-8,-9,-10,-11,-12,15,15,-4,-15,-45,15,15,15,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,15,15,15,15,-27,-43,-50,15,15,-47,15,-44,-45,15,-49,-48,]),'SENTENCIA_LOGICA_MIENTRAS':([0,3,4,5,6,7,8,17,18,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,89,92,94,96,97,98,100,102,104,107,109,110,111,112,113,114,],[16,16,-8,-9,-10,-11,-12,16,16,-4,-15,-45,16,16,16,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,16,16,16,16,-27,-43,-50,16,16,-47,16,-44,-45,16,-49,-48,]),'$end':([1,2,4,5,6,7,8,17,18,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,97,98,100,107,110,113,114,],[0,-1,-8,-9,-10,-11,-12,-3,-2,-4,-15,-45,-6,-3,-5,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,-27,-43,-50,-47,-44,-49,-48,]),'ID_VARIABLE':([3,4,5,6,7,8,10,11,12,13,17,18,19,20,25,30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,49,50,53,57,66,69,70,71,72,73,74,75,78,79,80,81,82,83,84,85,86,87,89,91,92,94,96,97,98,100,102,103,104,107,109,110,111,112,113,114,],[21,-8,-9,-10,-11,-12,26,27,28,29,-3,21,21,-15,-45,21,21,-6,-3,21,21,21,21,21,21,21,21,-19,65,-28,-20,-21,-22,21,-35,-26,21,-37,-38,-39,-40,-41,-42,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,21,21,21,21,21,-27,-43,-50,21,21,21,-47,21,-44,-45,21,-49,-48,]),'NUMERO':([3,4,5,6,7,8,17,18,19,20,22,25,30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,53,57,66,69,70,71,72,73,74,75,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,96,97,98,100,102,103,104,107,109,110,111,112,113,114,],[24,-8,-9,-10,-11,-12,-3,24,24,-15,37,-45,24,24,-6,-3,24,24,24,24,24,24,24,24,-19,63,-28,-20,67,-21,-22,24,-35,-26,24,-37,-38,-39,-40,-41,-42,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,93,24,24,24,24,24,-27,-43,-50,24,24,24,-47,24,-44,-45,24,-49,-48,]),'SIMBOLO_DELIMITADOR_APERTURA':([3,4,5,6,7,8,14,15,16,17,18,19,20,25,30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,49,50,53,57,66,69,70,71,72,73,74,75,78,79,80,81,82,83,84,85,86,87,89,91,92,94,96,97,98,100,102,103,104,107,109,110,111,112,113,114,],[22,-8,-9,-10,-11,-12,30,31,32,-3,22,22,-15,-45,22,22,-6,-3,22,22,22,22,22,22,22,22,-19,22,-28,-20,-21,-22,22,-35,-26,22,-37,-38,-39,-40,-41,-42,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,22,22,22,22,22,-27,-43,-50,22,22,22,-47,22,-44,-45,22,-49,-48,]),'SIMBOLO_CIERRE_BLOQUE':([4,5,6,7,8,19,20,25,33,34,35,36,44,46,47,49,50,57,66,78,79,80,81,82,83,84,85,86,87,94,96,97,98,100,104,106,107,109,110,111,112,113,114,],[-8,-9,-10,-11,-12,-4,-15,-45,-6,-3,-5,-13,-19,-28,-20,-21,-22,-35,-26,-29,-36,-30,-31,-32,-33,-34,-23,-24,-25,98,100,-27,-43,-50,107,110,-47,-45,-44,113,114,-49,-48,]),'SIMBOLO_FIN_LINEA':([9,21,24,26,28,29,55,56,57,58,59,60,61,62,63,64,65,76,90,93,105,108,],[25,-16,-17,46,46,46,-18,78,79,80,81,82,83,84,85,86,87,91,-46,97,109,111,]),'SIMBOLO_OPERACION_ARITMETICA_MAS':([21,23,24,38,55,63,65,],[-16,38,-17,57,-18,-17,-16,]),'SIMBOLO_OPERACION_ARITMETICA_MENOS':([21,23,24,55,63,65,],[-16,39,-17,-18,-17,-16,]),'SIMBOLO_OPERACION_ARITMETICA_POR':([21,23,24,55,63,65,],[-16,40,-17,-18,-17,-16,]),'SIMBOLO_OPERACION_ARITMETICA_DIVISION':([21,23,24,55,63,65,],[-16,41,-17,-18,-17,-16,]),'SIMBOLO_OPERACION_ARITMETICA_MOD':([21,23,24,55,63,65,],[-16,42,-17,-18,-17,-16,]),'OPERADOR_ASIGNACION':([21,23,24,26,27,28,29,55,63,65,],[-16,43,-17,45,48,45,45,-18,-17,-16,]),'SIMBOLO_OPERACION_LOGICA_MAYOR':([21,24,52,55,],[-16,-17,70,-18,]),'SIMBOLO_OPERACION_LOGICA_MENOR':([21,24,52,55,],[-16,-17,71,-18,]),'SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL':([21,24,52,55,],[-16,-17,72,-18,]),'SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL':([21,24,52,55,],[-16,-17,73,-18,]),'SIMBOLO_OPERACION_LOGICA_NO_IGUAL':([21,24,52,55,],[-16,-17,74,-18,]),'SIMBOLO_OPERACION_LOGICA_IGUAL':([21,24,52,55,],[-16,-17,75,-18,]),'SIMBOLO_DELIMITADOR_CIERRE':([21,24,37,51,54,55,57,78,79,80,81,82,83,84,90,95,],[-16,-17,55,68,77,-18,-35,-29,-36,-30,-31,-32,-33,-34,-46,99,]),'TEXTO':([45,],[64,]),'SIMBOLO_DECIMAL':([67,],[88,]),'SIMBOLO_APERTURA_BLOQUE':([68,77,99,101,],[89,92,102,103,]),'SENTENCIA_LOGICA_SINO':([98,],[101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'bloque':([0,],[2,]),'sentencia':([0,3,17,18,33,34,35,89,92,94,96,102,104,109,112,],[3,17,33,34,33,33,34,34,34,34,34,34,34,34,34,]),'romper':([0,3,17,18,33,34,35,89,92,94,96,102,104,109,112,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'tipo_dato':([0,3,17,18,31,33,34,35,89,92,94,96,102,104,109,112,],[5,5,5,5,53,5,5,5,5,5,5,5,5,5,5,5,]),'logica':([0,3,17,18,33,34,35,89,92,94,96,102,104,109,112,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'ciclo':([0,3,17,18,33,34,35,89,92,94,96,102,104,109,112,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'mientras':([0,3,17,18,33,34,35,89,92,94,96,102,104,109,112,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'enunciado':([3,18,35,89,92,94,96,102,104,109,112,],[18,35,35,94,96,35,35,104,35,112,35,]),'expresion':([3,18,19,35,36,89,92,94,96,102,104,109,112,],[19,19,36,19,36,19,19,19,19,19,19,19,19,]),'operacion':([3,18,19,35,36,45,89,91,92,94,96,102,103,104,109,112,],[20,20,20,20,20,66,20,95,20,20,20,20,106,20,20,20,]),'operando':([3,18,19,30,32,35,36,38,39,40,41,42,43,45,53,69,89,91,92,94,96,102,103,104,109,112,],[23,23,23,52,52,23,23,56,58,59,60,61,62,23,52,90,23,23,23,23,23,23,23,23,23,23,]),'asignacion':([26,28,29,],[44,49,50,]),'decimal':([27,],[47,]),'logicaOP':([30,32,53,],[51,54,76,]),'relacion':([52,],[69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> bloque','program',1,'p_program','analizador_sintactico.py',27),
  ('bloque -> sentencia enunciado','bloque',2,'p_bloque','analizador_sintactico.py',33),
  ('enunciado -> sentencia','enunciado',1,'p_enunciado_sentencia','analizador_sintactico.py',40),
  ('enunciado -> expresion','enunciado',1,'p_enunciado_expresion','analizador_sintactico.py',45),
  ('enunciado -> enunciado enunciado','enunciado',2,'p_enunciado_multi','analizador_sintactico.py',50),
  ('sentencia -> sentencia sentencia','sentencia',2,'p_sentencia_multi','analizador_sintactico.py',60),
  ('sentencia -> sentencia','sentencia',1,'p_sentencia','analizador_sintactico.py',65),
  ('sentencia -> romper','sentencia',1,'p_sentencia_romper','analizador_sintactico.py',70),
  ('sentencia -> tipo_dato','sentencia',1,'p_sentencia_declara','analizador_sintactico.py',75),
  ('sentencia -> logica','sentencia',1,'p_sentencia_logica','analizador_sintactico.py',80),
  ('sentencia -> ciclo','sentencia',1,'p_sentencia_ciclo','analizador_sintactico.py',85),
  ('sentencia -> mientras','sentencia',1,'p_sentencia_mientras','analizador_sintactico.py',90),
  ('expresion -> expresion expresion','expresion',2,'p_expresion_multi','analizador_sintactico.py',108),
  ('expresion -> expresion','expresion',1,'p_expresion','analizador_sintactico.py',113),
  ('expresion -> operacion','expresion',1,'p_expresion_operacion','analizador_sintactico.py',118),
  ('operando -> ID_VARIABLE','operando',1,'p_operando','analizador_sintactico.py',125),
  ('operando -> NUMERO','operando',1,'p_operando','analizador_sintactico.py',126),
  ('operando -> SIMBOLO_DELIMITADOR_APERTURA NUMERO SIMBOLO_DELIMITADOR_CIERRE','operando',3,'p_operando_simbolo','analizador_sintactico.py',131),
  ('tipo_dato -> TIPO_DATO_ENT ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',138),
  ('tipo_dato -> TIPO_DATO_DEC ID_VARIABLE decimal','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',139),
  ('tipo_dato -> TIPO_DATO_TXT ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',140),
  ('tipo_dato -> TIPO_DATO_BIN ID_VARIABLE asignacion','tipo_dato',3,'p_tipo_dato','analizador_sintactico.py',141),
  ('asignacion -> OPERADOR_ASIGNACION NUMERO SIMBOLO_FIN_LINEA','asignacion',3,'p_asignacion_datos_val','analizador_sintactico.py',147),
  ('asignacion -> OPERADOR_ASIGNACION TEXTO SIMBOLO_FIN_LINEA','asignacion',3,'p_asignacion_datos_val','analizador_sintactico.py',148),
  ('asignacion -> OPERADOR_ASIGNACION ID_VARIABLE SIMBOLO_FIN_LINEA','asignacion',3,'p_asignacion_datos_val','analizador_sintactico.py',149),
  ('asignacion -> OPERADOR_ASIGNACION operacion','asignacion',2,'p_asignacion_datos_val_op','analizador_sintactico.py',154),
  ('decimal -> OPERADOR_ASIGNACION NUMERO SIMBOLO_DECIMAL NUMERO SIMBOLO_FIN_LINEA','decimal',5,'p_asignaciondec','analizador_sintactico.py',159),
  ('asignacion -> SIMBOLO_FIN_LINEA','asignacion',1,'p_asignacion_datos_No_val','analizador_sintactico.py',165),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MAS operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',171),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MENOS operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',172),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_POR operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',173),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_DIVISION operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',174),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MOD operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',175),
  ('operacion -> operando OPERADOR_ASIGNACION operando SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica','analizador_sintactico.py',176),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS','operacion',3,'p_operacion_basica_resumida','analizador_sintactico.py',181),
  ('operacion -> operando SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_OPERACION_ARITMETICA_MAS SIMBOLO_FIN_LINEA','operacion',4,'p_operacion_basica_resumida_fin','analizador_sintactico.py',186),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_MAYOR','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',193),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_MENOR','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',194),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_MAYOR_IGUAL','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',195),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_MENOR_IGUAL','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',196),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_NO_IGUAL','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',197),
  ('relacion -> SIMBOLO_OPERACION_LOGICA_IGUAL','relacion',1,'p_relacionAsignacion','analizador_sintactico.py',198),
  ('logica -> SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE','logica',7,'p_logicasoloIF','analizador_sintactico.py',204),
  ('logica -> SENTENCIA_LOGICA_SI SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE SENTENCIA_LOGICA_SINO SIMBOLO_APERTURA_BLOQUE operacion SIMBOLO_CIERRE_BLOQUE','logica',11,'p_logicaIFcompleto','analizador_sintactico.py',209),
  ('romper -> SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA','romper',2,'p_romer','analizador_sintactico.py',214),
  ('logicaOP -> operando relacion operando','logicaOP',3,'p_logicaOP','analizador_sintactico.py',218),
  ('ciclo -> SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE','ciclo',10,'p_ciclo','analizador_sintactico.py',225),
  ('ciclo -> SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA enunciado SIMBOLO_CIERRE_BLOQUE','ciclo',12,'p_ciclo_romper','analizador_sintactico.py',230),
  ('ciclo -> SENTENCIA_LOGICA_CICLO SIMBOLO_DELIMITADOR_APERTURA tipo_dato logicaOP SIMBOLO_FIN_LINEA operacion SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SENTENCIA_SALIDA_CICLOS SIMBOLO_FIN_LINEA SIMBOLO_CIERRE_BLOQUE','ciclo',12,'p_ciclo_romper','analizador_sintactico.py',231),
  ('mientras -> SENTENCIA_LOGICA_MIENTRAS SIMBOLO_DELIMITADOR_APERTURA logicaOP SIMBOLO_DELIMITADOR_CIERRE SIMBOLO_APERTURA_BLOQUE enunciado SIMBOLO_CIERRE_BLOQUE','mientras',7,'p_mientras','analizador_sintactico.py',236),
]
