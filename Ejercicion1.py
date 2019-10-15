"""
andresvallejoz1991
"""
#Funcion
def palindromas(x):
	lista = ["oro","ojo","oso","radar","seres"]#palabras palindromas
	if x in reversed (lista):#Condiconal para la reversa
		return True
	else:
		return False
		
#Listado de las palabras
datos = ["oro","pais","ojo","oso","radar","sol","seres"]

resultado = filter(lambda x: x == "".join(reversed (x)),datos)#Condicional Lambda
#Filtra las palabras que son iguales al derecho y al reves
print(list(resultado))#Impresion resultado			
			
