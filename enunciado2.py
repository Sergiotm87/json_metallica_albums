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
    for tag in elem["album"]["tags"]["tag"]:
        listaetiquetas.append(tag["name"])

for p in list(set(listaetiquetas)): print p

#pedimos que se introduzca alguna por teclado y recorremos los albumes en busca de la elejida
etiqueta=raw_input("\nintroduce el nombre de una etiqueta: ")

listaalbumes=[]

for elem in data:
    for tag in elem["album"]["tags"]["tag"]:
        if tag["name"]==etiqueta:
            listaalbumes.append(elem["album"]["name"])

print "Los albumes en los que aparece la etiqueta",etiqueta,"son:\n"
for elem in listaalbumes: print elem

