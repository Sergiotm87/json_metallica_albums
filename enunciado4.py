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

for elem in data:
    if elem["album"]["name"]==album:
        for cancion in elem["album"]["tracks"]["track"]:
            print cancion["streamable"]["playcount"]

#pedimos por teclado cuantos resultados quiere mostrar y lo mostramos