txt = ""
cont = 0
def incrementarContador():
    global cont
    cont +=1
    return "%d" %cont

class Nodo():
	pass

class program(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1  =  son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print(ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		son1 = self.son1.traducir()

		txt += id +"[label = "+self.name+"]"+"\n \t"
		txt += id +"->"+son1+"\n \t"

		return "diagraph G {\n\t"+txt+"}"


class bloque(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):

		#if str(type(self.son1)) == "<type 'tuple'>":
		if type(self.son1) == type(tuple()):
			#print "entro tupla"
			self.son1[0].imprimir(" "+ident)
		#elif str(type(self.son1)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son1.imprimir(" "+ident)

		#if str(type(self.son2)) == "<type 'tuple'>":
		if type(self.son2) == type(tuple()):
			#print "entro tupla"
			self.son2[0].imprimir(" "+ident)
		#elif str(type(self.son2)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son2.imprimir(" "+ident)



		print (ident + "Nodo: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.son1) == type(tuple()):
			son1 = son1=self.son1[0].traducir()
		else:
			son1 = son1=self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2 = son2=self.son2[0].traducir()
		else:
			son2 = son2=self.son2.traducir()

		if type(self.son3) == type(tuple()):
			son3 = son3=self.son3[0].traducir()
		else:
			son3 = son3=self.son3.traducir()

		if type(self.son3) == type(tuple()):
			son4 = son4=self.son4[0].traducir()
		else:
			son4 = son4=self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id
    

#enunciados
class enunciado_sentencia(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):

		
		if type(self.son1) == type(tuple()):

			self.son1[0].imprimir(" "+ident)

		else:
			
			self.son1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.son1) == type(tuple()):
			son1 = son1=self.son1[0].traducir()
		else:
			son1 = son1=self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		return id

class enunciado_expresion(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):

		
		if type(self.son1) == type(tuple()):

			self.son1[0].imprimir(" "+ident)
		else:
			self.son1.imprimir(" "+ident) 

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.son1) == type(tuple()):
			son1=son1=self.son1[0].traducir()
		else:
			son1=son1=self.son1.traducir()
			  
		txt += id +"[label= "+self.name+"]"+"\n\t"
		txt += id +"->"+son1+"\n\t"
		return id

class enunciado_multi(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):

		if type(self.son1) == type(tuple()):
			self.son1[0].imprimir(" "+ident)
		else:
			self.son1.imprimir(" "+ident)
        
		if type(self.son2) == type(tuple()):
			self.son2[0].imprimir(" "+ident)
		else:
			self.son2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.son1) == type(tuple()):
			son1=son1=self.son1[0].traducir()
		else:
			son1=son1=self.son1.traducir()
			
		if type(self.son2) == type(tuple()):
			son2=son2=self.son2[0].traducir()
		else:
			son2=son2=self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id





#sentencias
class sentencia_multi(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):

		if type(self.son1) == type(tuple()):
			self.son1[0].imprimir(" "+ident)
		else:
			self.son1.imprimir(" "+ident)

		if type(self.son2) == type(tuple()):
			self.son2[0].imprimir(" "+ident)
		else:
			self.son2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.son1) == type(tuple()):
			son1=son1=self.son1[0].traducir()
		else:
			son1=son1=self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2=son2=self.son2[0].traducir()
		else:
			son2=self.son2.traducir()
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class sentencia(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
    
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)   

        

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=son1=self.son1[0].traducir()
        else:
            son1=son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class sentencia_romper(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)          

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=son1=self.son1[0].traducir()
        else:
            son1=son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class sentencia_declara(Nodo): 
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)  

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=son1=self.son1[0].traducir()
        else:
            son1=son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class sentencia_logica(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)         

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class sentencia_ciclo(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        
    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name) 

        
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class sentencia_mientras(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)         

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

#class sentencia_imprimir(Nodo):
#    'sentencia : imprimir'
#    p[0] = p[1]
#   print("sentencia_imrpirmir")


#Pantalla
#class imprimir(Nodo):
#    'imprimir : SALIDA_DE_PANTALLA SIMBOLO_FIN_LINEA'
#    p[0] = p[1] 


#Expresiones
class expresion_multi(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)          

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class expresion(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)           

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class expresion_operacion(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)          

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


#Operandos
class operando(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)            

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class operando_simbolo(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 - son3

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)         

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


# Tipos de datos
class tipo_dato(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident)	:
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)        

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

# Asignación de datos
class asignacion_datos_val(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)         

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class asignacion_datos_val_op(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        
        print (ident + "Nodo: "+self.name)           

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class asignaciondec(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)         

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id


class asignacion_datos_No_val(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        
    
    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)  

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

#operacion
class operacion_basica(Nodo):
    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son4

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)    

        print (ident + "Nodo: "+self.name)      

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class operacion_basica_resumida(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)  
        else:
            self.son3.imprimir(" "+ident)    

        print (ident + "Nodo: "+self.name)    

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class operacion_basica_resumida_fin(Nodo):
    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self,ident)	:
    
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)      

        print (ident + "Nodo: "+self.name) 

    def traducir(self):
        global txt
        id = incrementarContador()  

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            self.son4.traducir    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id


#relaciones
class relacionAsignacion(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name) 


    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

#logica
class logicasoloIF(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
        
        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else:
            self.son7.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name) 

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()
        
        if type(self.son6) == type(tuple()):
            sson6=self.son6[0].traducir()
        else:
            son6=self.son6.traducir()
        
        if type(self.son7) == type(tuple()):
            son7=self.son7[0].traducir()
        else:
            son7=self.son7.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id

class logicaIFcompleto(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,son10,son11,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10
        self.son11 = son11

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
        
        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else:
            self.son7.imprimir(" "+ident)
        
        if type(self.son8) == type(tuple()):
            self.son8[0].imprimir(" "+ident)
        else:
            self.son8.imprimir(" "+ident)
        
        if type(self.son9) == type(tuple()):
            self.son9[0].imprimir(" "+ident)
        else:
            self.son9.imprimir(" "+ident)
        
        if type(self.son10) == type(tuple()):
            self.son10[0].imprimir(" "+ident)
        else:
            self.son10.imprimir(" "+ident)
        
        if type(self.son11) == type(tuple()):
            self.son11[0].imprimir(" "+ident)
        else:
            self.son11.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name)        

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()
        
        if type(self.son6) == type(tuple()):
            sson6=self.son6[0].traducir()
        else:
            son6=self.son6.traducir()
        
        if type(self.son7) == type(tuple()):
            son7=self.son7[0].traducir()
        else:
            son7=self.son7.traducir()
        
        if type(self.son8) == type(tuple()):
            son8=self.son8[0].traducir()
        else:
            son8=self.son8.traducir()
        
        if type(self.son9) == type(tuple()):
            son9=self.son9[0].traducir()
        else:
            son9=self.son9.traducir()
        
        if type(self.son10) == type(tuple()):
            son10=self.son10[0].traducir()
        else:
            son10=self.son10.traducir()
        
        if type(self.son11) == type(tuple()):
            son11=self.son11[0].traducir()
        else:
            son11=self.son11.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"
        txt += id + " -> " + son10 + "\n\t"
        txt += id + " -> " + son11 + "\n\t"

        return id

class romer(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident)	:
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        
        print (ident + "Nodo: "+self.name)   

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class logicaOP(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3


    def imprimir(self,ident)	:
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        print (ident + "Nodo: "+self.name) 


    def traducir(self):
        global txt
        id = incrementarContador()
        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


#ciclos
class ciclo(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,son10,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
        
        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else:
            self.son7.imprimir(" "+ident)
        
        if type(self.son8) == type(tuple()):
            self.son8[0].imprimir(" "+ident)
        else:
            self.son8.imprimir(" "+ident)
        
        if type(self.son9) == type(tuple()):
            self.son9[0].imprimir(" "+ident)
        else:
            self.son9.imprimir(" "+ident)
        
        if type(self.son10) == type(tuple()):
            self.son10[0].imprimir(" "+ident)
        else:
            self.son10.imprimir(" "+ident)    

        print (ident + "Nodo: "+self.name)     

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()
        
        if type(self.son6) == type(tuple()):
            sson6=self.son6[0].traducir()
        else:
            son6=self.son6.traducir()
        
        if type(self.son7) == type(tuple()):
            son7=self.son7[0].traducir()
        else:
            son7=self.son7.traducir()
        
        if type(self.son8) == type(tuple()):
            son8=self.son8[0].traducir()
        else:
            son8=self.son8.traducir()
        
        if type(self.son9) == type(tuple()):
            son9=self.son9[0].traducir()
        else:
            son9=self.son9.traducir()
        
        if type(self.son10) == type(tuple()):
            son10=self.son10[0].traducir()
        else:
            son10=self.son10.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"
        txt += id + " -> " + son10 + "\n\t"

        return id

class ciclo_romper(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,son10,son11,son12,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10
        self.son11 = son11
        self.son12 = son12

    def imprimir(self,ident)	:

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
        
        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else:
            self.son7.imprimir(" "+ident)
        
        if type(self.son8) == type(tuple()):
            self.son8[0].imprimir(" "+ident)
        else:
            self.son8.imprimir(" "+ident)
        
        if type(self.son9) == type(tuple()):
            self.son9[0].imprimir(" "+ident)
        else:
            self.son9.imprimir(" "+ident)
        
        if type(self.son10) == type(tuple()):
            self.son10[0].imprimir(" "+ident)
        else:
            self.son10.imprimir(" "+ident)  

        if type(self.son11) == type(tuple()):
            self.son11[0].imprimir(" "+ident)
        else:
            self.son11.imprimir(" "+ident)
        
        if type(self.son12) == type(tuple()):
            self.son12[0].imprimir(" "+ident)
        else:
            self.son12.imprimir(" "+ident) 

        print (ident + "Nodo: "+self.name)        

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()
        
        if type(self.son6) == type(tuple()):
            sson6=self.son6[0].traducir()
        else:
            son6=self.son6.traducir()
        
        if type(self.son7) == type(tuple()):
            son7=self.son7[0].traducir()
        else:
            son7=self.son7.traducir()
        
        if type(self.son8) == type(tuple()):
            son8=self.son8[0].traducir()
        else:
            son8=self.son8.traducir()
        
        if type(self.son9) == type(tuple()):
            son9=self.son9[0].traducir()
        else:
            son9=self.son9.traducir()
        
        if type(self.son10) == type(tuple()):
            son10=self.son10[0].traducir()
        else:
            son10=self.son10.traducir()
        
        if type(self.son11) == type(tuple()):
            son11=self.son11[0].traducir()
        else:
            son11=self.son11.traducir()
        
        if type(self.son12) == type(tuple()):
            self.son12[0].traducir()
        else:
            son12=self.son12.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"
        txt += id + " -> " + son10 + "\n\t"
        txt += id + " -> " + son11 + "\n\t"
        txt += id + " -> " + son12 + "\n\t"

        return id

class mientras(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
        self.name = name
        self.son1 = son1
        self.som2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self,ident)	:
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else:
            self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else:
            self.son6.imprimir(" "+ident)
        
        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else:
            self.son7.imprimir(" "+ident)    

        print (ident + "Nodo: "+self.name)     



    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1=self.son1[0].traducir()
        else:
            son1=self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].traducir()
        else:
            son2=self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3=self.son3[0].traducir()
        else:
            son3=self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4=self.son4[0].traducir()
        else:
            son4=self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5=self.son5[0].traducir()
        else:
            son5=self.son5.traducir()
        
        if type(self.son6) == type(tuple()):
            sson6=self.son6[0].traducir()
        else:
            son6=self.son6.traducir()
        
        if type(self.son7) == type(tuple()):
            son7=self.son7[0].traducir()
        else:
            son7=self.son7.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id