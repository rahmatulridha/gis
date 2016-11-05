#!/bin/python

import shapefile

sf = shapefile.Reader("/home/ali/Materi/MATERI SEMESTER V/SISTEM INFORMASI GEOGRAFIS/github/doc/praktikum/praktikum2/negara.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#		if not name.startswitch('__'):
#				print name
