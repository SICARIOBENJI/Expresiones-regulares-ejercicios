import re

print("*****************Instituto Tecnologico Superior de Valladolid*****************\n"
    + "*******************Ejercicios con expresiones regulares*******************\n"
    + "***********************Oscar Benjamin Chi Canche*******************\n")

asignado1= """
Programación es el proceso de tomar un algoritmo y codificarlo en una notación, 
un lenguaje de programación, de modo que pueda ser ejecutado por una computadora.
"""

asignado2= """
Palabra que inicia con (M) donde la segunda letra no es vocal: Mmariposa 
Expresion en comillas: "COD" "Mobile" "ArigamePlays"
Direcciones ip: 192.168.0.1   192.168.12.1202
Horas: 12:30am  11:59pm
Telefonos: 985-110-1588   o    999-238-3641
Correo electronico: oscar10034769@hmail.com  o  oscar.chicanche@itsva.edu.mx
Url: www.brazzers.com/   o    www.wikipedia.com/
Codigo postal: 97770  o  98675   o  99685
"""


print("Todas las palabras que tengan una longitud de 7 o mas letras")


metodo1 = r"(\w{7,})"

coincidencias1 = re.findall(metodo1, asignado1)

for coincidencia1 in coincidencias1:
    print(coincidencia1)

#****************************************************************

print()
print("Expresiones que No finalicen con una vocal")
print()

metodo2 = r"\w+[b-df-hj-np-tv-z]\b"

coincidencias2 = re.findall(metodo2, asignado1)

for coincidencia2 in coincidencias2:
    print(coincidencia2)

#****************************************************************
print()
print("Las palabras que inicien con “M” donde la segunda letra no sea vocal")
print()

metodo3 = r"[M][^aeiou]\w{1,}"

coincidencias3 = re.findall(metodo3, asignado2)

for coincidencia3 in coincidencias3:
    print(coincidencia3)

#****************************************************************
print()
print("Expresiones encerradas entre comillas")
print()

metodo4 = r"\"(\w{1,})\""

coincidencias4 = re.findall(metodo4, asignado2)

for coincidencia4 in coincidencias4:
    print(coincidencia4)

print()
print("Direcciones ip's")
print()

metodo5 = r"(\d{3})\.(\d{3})\.(\d{,3})\.(\d{,3})"

coincidencias5 = re.findall(metodo5, asignado2)

for coincidencia5 in coincidencias5:
    print(coincidencia5)

#*****************************************************************
print()
print("Busqueda de horas")
print()

metodo6 = r"(\d\d)(:(\d\d))(am|pm)"

coincidencias6 = re.findall(metodo6, asignado2)

for coincidencia6 in coincidencias6:
    print(coincidencia6)

#*****************************************************************
print()
print("Busqueda de telefonos")
print()

metodo7 = r"\d{3}-\d{3}-\d{4}"

coincidencias7 = re.findall(metodo7, asignado2)

for coincidencia7 in coincidencias7:
    print(coincidencia7)

#*****************************************************************
print()
print("Correos electronicos")
print()

metodo8 = r"[a-z0-9\.-_]+@[\w\d]+\.\w"

coincidencias8 = re.findall(metodo8, asignado2)

for coincidencia8 in coincidencias8:
    print(coincidencia8)

#******************************************************************
print()
print("Busqueda de url's")
print()

metodo9 = r"(\w+).([\w\-\.]+)/"

coincidencias9 = re.findall(metodo9, asignado2)

for coincidencia9 in coincidencias9:
    print(coincidencia9)

#*******************************************************************
print()
print("Busqueda de codigo postal")
print()

metodo10 = r"[0-9]{5}"

coincidencias10 = re.findall(metodo10, asignado2)

for coincidencia10 in coincidencias10:
    print(coincidencia10)