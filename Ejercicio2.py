"""
andresvallejoz1991
"""
#Nombre de la funcion 
def Placs (x):
	# Listado de las palabras iniciales de las provincias
	Provincia = ["l","p","e","a","i"]
	#Condicional para la posicion 0
	if x[0] in Provincia:
		return True#Retorna falso o veradero
	else:
		return False
		
#Placas 
placas = ["lba-001", "gma-002", "azx-003", "ess-004",  "oro-100", "mab-001", "iaj-002"] 
#Impresion del resuktado
resultado = filter(Placs, placas)	
print(list(resultado))#Impresion del resultado