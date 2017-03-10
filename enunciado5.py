# -*- coding: utf-8 -*-
import json
#
#	Introduce un año, indica si algun album fue publicado en esa fecha (nota: los años de publicación están entre 1983 y 1988)
#
with open('Metallica.json') as data_file:
    data = json.load(data_file)

#print data