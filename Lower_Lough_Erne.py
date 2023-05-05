

import os.path

import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches

# Makes the plotting interactive
plt.ion()

# Generate matplotlib handles, used to create a legend
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)
    handles =[]
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

# Load the dataset
FloodOneLLE = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/FloodOne.shp'))
FloodTwoLLE = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/FloodTwo.shp'))
FloodThreeLLE = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/FloodThree.shp'))
FloodFourLLE = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/FloodFour.shp'))
FloodFiveLLE =gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/FloodFive.shp'))
outline = gpd.read_file(os.path.abspath('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh_DCA.shp'))

# Creates a figure which is 10x10 inches
myFig = plt.figure(figsize=(10, 10))

# Create a UTM reference system to transform the data
myCRS = ccrs.TransverseMercator(29903)

# Creates an axes object, can project data

ax =  plt.axes(projection=myCRS)

# Add the 1m flood layer to the map
FloodOneLLE_feature = ShapelyFeature(FloodOneLLE['geometry'], myCRS, edgecolor='k', facecolor='blue')
xmin, ymin, xmax, ymax = FloodOneLLE.total_bounds

# Add the outline for Fermanagh
outline_feature = ShapelyFeature(outline['geometry'],
                                 myCRS,
                                 edgecolor='black',
                                 facecolor='none',
                                 linewidth=1)

# Add features to the map
ax.add_feature(FloodOneLLE_feature)
ax.add_feature(outline_feature)

# Using the boundary of the shapefile, zoom the map to the area of interest
ax.set_extent([xmin-5000, xmax+5000, ymin-5000, ymax+5000], crs=myCRS)

scale_bar(ax)

# Save my map
myFig.savefig('Flood_Extent', bbox_inches='tight', dpi=300)

print(outline.crs)
print(FloodOneLLE.crs)