import os

import geopandas as gpd
import cartopy.crs as ccrs

outline = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh_DCA.shp'))
flood = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/4mFloodLLE.shp'))

print(outline.crs)
print(flood.crs)

