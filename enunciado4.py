# -*- coding: utf-8 -*-
import json
#
#	Introduce el nombre de un album, indica cuales canciones han sido reproducidos más veces
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

album=raw_input("Introduce el nombre de un album: ")
#ej. Master of Puppets,Ride the lightning

#tomamos el numero de reproducciones de las canciones del album introducido

listareproducciones=[]
listacanciones=[]

for elem in data:
    if elem["album"]["name"]==album:
        for cancion in elem["album"]["tracks"]["track"]:
            listareproducciones.append(cancion["streamable"]["playcount"])
            listacanciones.append(cancion["name"])


#pedimos por teclado cuantos resultados quiere mostrar y lo mostramos

resultado=int(raw_input("¿cuantos resultados quieres mostrar?: \n"))

if resultado<len(listacanciones):
    for i,j in zip(listacanciones[0:resultado],listareproducciones[0:resultado]):
        print i+":",j,"reproducciones"

#falta ordenar listas