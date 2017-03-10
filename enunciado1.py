# -*- coding: utf-8 -*-
import json
#
#    Lista las canciones que tengan una duracion de más de 6 min
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

#tomamos las canciones, de las que tengan una duracion mayor a 6min tomamos su nombre y su duracion pasada a notacion minutos:segundos
listacanciones=[]
duracion=[]

#recorremos el json tomando la duracion de las canciones, aquellas que duran mas de 6min(360)
#las guardamos en una lista junto con su nombre

for elem in data:
    for cancion in elem["album"]["tracks"]["track"]:
        if int(cancion["duration"])>360:
            listacanciones.append(cancion["name"])
            duracion.append(str(int(cancion["duration"])/60)+":"+str(int(cancion["duration"])%60))
print "Hay",len(listacanciones),"canciones cuya duración es mayor a 6 min:\n"

#mostramos de forma paralela ambas listas mediante zip

for i,j in zip(listacanciones,duracion):
    print i,j
