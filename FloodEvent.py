import os.path

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs

# Loading Fermanagh outline
outline = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh_DCA.shp'))

# Creates a figure of size 10x10 inches
myFig = plt.figure(figsize=(10, 10))

# create a Universal Transverse Mercator reference system to transform the data.
myCRS = ccrs.UTM(29)

# Creates an axes object, can project our data

ax = plt.axes(projection=myCRS)

# first, we just add the outline of County Fermanagh using cartopy's ShapelyFeature
outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='k', facecolor='w')
xmin, ymin, xmax, ymax = outline.total_bounds

# add the features we've created to the map.
ax.add_feature(outline_feature)

# using the boundary of the shapefile features, zoom the map to our area of interest
ax.set_extent([xmin-5000, xmax+5000, ymin-5000, ymax+5000], crs=myCRS)  # because total_bounds

# gives output as xmin, ymin, xmax, ymax,
# but set_extent takes xmin, xmax, ymin, ymax, we re-order the coordinates here.

# Save the map
myFig.savefig('map.png', bbox_inches='tight', dpi=300)