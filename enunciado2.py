# -*- coding: utf-8 -*-
import json
#
#    Muestra las etiquetas de los albumes, elije una y cuenta en cuantos albumes aparece esta etiqueta
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

#tomamos la lista de etiquetas y las mostramos
listaetiquetas=[]

for elem in data:
    for etiqueta in elem["album"]["tags"]["tag"]:
        listaetiquetas.append(etiqueta["name"])

#print listaetiquetas
for p in listaetiquetas: print p

#pedimos que se introduzca alguna por teclado y recorremos los albumes en busca de la elejida
#etiqueta=raw_input("introduce el nombre de una etiqueta")




#mostramos los albumes en los que aparece la etiqueta