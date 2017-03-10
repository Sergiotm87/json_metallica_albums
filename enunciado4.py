# -*- coding: utf-8 -*-
import json
#
#	Introduce el nombre de un album, indica cuales canciones han sido reproducidos más veces
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

album=raw_input("Introduce el nombre de un album: ")
#ej. Master of Puppets,Ride the Lightning

#tomamos el numero de reproducciones de las canciones del album introducido

listareproducciones=[]
listacanciones=[]

for elem in data:
    if elem["album"]["name"]==album:
        for cancion in elem["album"]["tracks"]["track"]:
            reproducciones=cancion["streamable"]["playcount"]
            tema=cancion["name"]
            item=str(tema+" "+str(reproducciones))
            listacanciones.append(item)

#usamos una funcion lambda que sepera el ultimo elemento numerico de cada registro temporalmente para ordenar la lista descendentemente

listacanciones.sort(key=lambda x:int(x.split()[-1]),reverse=True)

#print listacanciones

#pedimos por teclado cuantos resultados quiere mostrar y lo mostramos

resultado=int(raw_input("¿cuantos resultados quieres mostrar?: "))

if resultado<len(listacanciones):
    for i in listacanciones[0:resultado]:
        print i