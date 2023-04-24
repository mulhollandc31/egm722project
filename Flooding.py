
import geopandas as gps
import pandsa as pd
import matplotlib.pyplot as plt

fermanagh_poly = '\data\Fermanagh_DCA.shp'

shape = gpd.read_file(fermanagh_poly)
print(shape.head())

