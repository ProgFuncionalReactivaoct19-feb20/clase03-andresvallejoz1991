"""
andrevallejoz1991
"""

#Listado de provincias
provincias = ["Loja","Pichincha","Guayaquil","Zamora","Ibarra","Manabi","Machala","Portoviejo","Macas"]

resultado = filter(lambda x: len(x)%2 ==0,provincias)#Funcion lambda con el condicional
#El condicioanl filtra las provincias con un numero par de letras
print(list(resultado))#Impresion de resultados.



