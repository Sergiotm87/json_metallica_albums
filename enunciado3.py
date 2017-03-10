# -*- coding: utf-8 -*-
import json
#
#	Introduce el nombre de una canción, muestra a que album pertenece
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

#print data