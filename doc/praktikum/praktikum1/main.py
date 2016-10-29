#!/bin/python

import shapefile

sf = shapefile.Reader("country/ne_10m_admin_0_countries.shp")
print sf
shapes = sf.shapes()
print len(shapes)
