# -*- coding: utf-8 -*-
import json
#
#	Introduce el nombre de una canción, muestra a que album pertenece
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

tema=raw_input("introduce el nombre de una cancion: ")
#ej. "...and Justice for All","Orion","Fade to Black"

#recorremos el json en busca de estas canciones y tomamos el nombre del album correspondiente


for elem in data:
    for cancion in elem["album"]["tracks"]["track"]:
        print cancion["name"]


#print "La cancion",tema,"pertenece al album",album