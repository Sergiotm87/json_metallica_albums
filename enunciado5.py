# -*- coding: utf-8 -*-
import json
import re
#
#	Introduce un año, indica si algun album fue publicado en esa fecha (nota: los años de publicación están entre 1983 y 1988)
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

anyo=int(raw_input("Introduce el año a buscar: "))

#dentro de cada texto buscamos una cadena de caracteres que corresponda a un año, si encontramos
#uno igual al introducido tomamos el nodo padre con el nombre del album
#usamos una expresion regular para que tome las coincidencias

encontrado=False

for elem in data:
    match = re.search(r'\d{4}', elem["album"]["wiki"]["summary"])
    if int(match.group(0))==anyo:
        print "En",match.group(0),"fué publicado",elem["album"]["name"]
        encontrado=True

if not encontrado:
    print "no se ha encontrado un album publicado en el año",anyo

