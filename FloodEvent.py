import os.path

import geopandas as gpd
# import pandas as pd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs

# Make the map plotting interactive
plt.ion()

# Generate matplotlib handles, these are used to create a legend of map items.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

# Creates a scale bar
def scale_bar(ax, location=(0.92, 0.95)):
    x0, x1, y0, y1 = ax.get_extent()
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    ax.plot([sbx, sbx - 20000], [sby, sby], color='k', linewidth=9, transform=ax.projection)
    ax.plot([sbx, sbx - 10000], [sby, sby], color='k', linewidth=6, transform=ax.projection)
    ax.plot([sbx-10000, sbx - 20000], [sby, sby], color='w', linewidth=6, transform=ax.projection)

    ax.text(sbx, sby-4500, '20 km', transform=ax.projection, fontsize=8)
    ax.text(sbx-12500, sby-4500, '10 km', transform=ax.projection, fontsize=8)
    ax.text(sbx-24500, sby-4500, '0 km', transform=ax.projection, fontsize=8)

# Loading datasets
outline = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh_DCA.shp'))
loughs = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/major_loughs.shp'))
roads = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh roads.shp'))
rivers = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/fer_main_river.shp'))

# Creates a figure of size 10x10 inches
myFig = plt.figure(figsize=(10, 10))

# create a Universal Transverse Mercator reference system to transform the data.
myCRS = ccrs.UTM(29)

# Creates an axes object, can project our data

ax = plt.axes(projection=myCRS)

# Add the outline of County Fermanagh using cartopy's ShapelyFeature
outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='k', facecolor='w')
xmin, ymin, xmax, ymax = outline.total_bounds

# Create lough features for the map
lough_features = ShapelyFeature(loughs['geometry'],
                                myCRS,
                                edgecolor='mediumblue',
                                facecolor='mediumblue',
                                linewidth=1)

# Create road features for the map
road_features = ShapelyFeature(roads['geometry'],
                               myCRS,
                               edgecolor='grey',
                               facecolor='none',
                               linewidth=0.5)

# Create the main river features for the map
river_features = ShapelyFeature(rivers['geometry'],
                                myCRS,
                                edgecolor='royalblue',
                                facecolor='none',
                                linewidth=1)


# add the features we've created to the map.
ax.add_feature(outline_feature)
ax.add_feature(lough_features)
ax.add_feature(road_features)
ax.add_feature(river_features)


# using the boundary of the shapefile features, zoom the map to our area of interest
ax.set_extent([xmin-5000, xmax+5000, ymin-5000, ymax+5000], crs=myCRS)  # because total_bounds

scale_bar(ax)


# Save the map
myFig.savefig('map.png', bbox_inches='tight', dpi=300)


