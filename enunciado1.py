# -*- coding: utf-8 -*-
import json
#
#    Lista las canciones que tengan una duracion de más de 6 min
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

#tomamos las canciones, de las que tengan una duracion mayor a 6min tomamos su nombre y su duracion pasada a notacion minutos:segundos

#recorremos el json tomando la duracion de las canciones, aquellas que duran mas de 6min(300)
#las guardamos en una lista junto con su nombre

for elem in data:
    for cancion in elem["album"]["tracks"]["track"]:
        print cancion["duration"]
