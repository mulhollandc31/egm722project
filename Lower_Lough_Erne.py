

import os.path
import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import folium
import numpy as np



# Create the data frame
dfOne = gpd.read_file(os.path.abspath('data_files/FloodOne.shp'))
dfTwo = gpd.read_file(os.path.abspath('data_files/FloodTwo.shp'))
dfThree = gpd.read_file(os.path.abspath('data_files/FloodThree.shp'))
dfFour = gpd.read_file(os.path.abspath('data_files/FloodFour.shp'))
dfFive = gpd.read_file(os.path.abspath('data_files/FloodFive.shp'))
dfOne.head()
dfTwo.head()
dfThree.head()
dfFour.head()
dfFive.head()

# Change epsg to 4326
dfOne = dfOne.to_crs(epsg=4326)
print(dfOne.crs)
dfOne.head()

dfTwo = dfTwo.to_crs(epsg=4326)
print(dfTwo.crs)
dfTwo.head()

dfThree = dfThree.to_crs(epsg=4326)
print(dfThree.crs)
dfThree.head()

dfFour = dfFour.to_crs(epsg=4326)
print(dfFour.crs)
dfFour.head()

dfFive = dfFive.to_crs(epsg=4326)
print(dfFive.crs)
dfFive.head()

# Create a folium map
m = folium.Map(location=[54.44, -7.73], tiles="Stamen Terrain", zoom_start=11, control_scale=True)
m

# Add polygons to the map
for _, r in dfOne.iterrows(): # Simplify the representation of polygons
    sim_geo = gpd.GeoSeries(r["geometry"])#.simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda
        x: {"fillColor": "red"}, name='One meter flood', show=True)
    geo_j.add_to(m)
m

for _, r in dfTwo.iterrows(): # Simplify the representation of polygons
    sim_geo = gpd.GeoSeries(r["geometry"])#.simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda
        x: {"fillColor": "red"}, name='Two meter flood', show=False)
    geo_j.add_to(m)
m

for _, r in dfThree.iterrows(): # Simplify the representation of polygons
    sim_geo = gpd.GeoSeries(r["geometry"])#.simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda
        x: {"fillColor": "red"}, name= 'Three meter flood', show=False)
    geo_j.add_to(m)
m

for _, r in dfFour.iterrows(): # Simplify the representation of polygons
    sim_geo = gpd.GeoSeries(r["geometry"])#.simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda
        x: {"fillColor": "red"}, name='Four meter flood', show=False)
    geo_j.add_to(m)
m

for _, r in dfFive.iterrows(): # Simplify the representation of polygons
    sim_geo = gpd.GeoSeries(r["geometry"])#.simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda
        x: {"fillColor": "red"}, name='Five meter flood', show=False)
    geo_j.add_to(m)
m
# https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html

# Add Layer control
folium.LayerControl(collapsed=False).add_to(m)
m



# Converting shp to GeoJSON
# shp_file = gpd.read_file('C:/Users/naloa/Documents/GitHub/egm722project/data_files/Fermanagh_DCA.shp')
# shp_file.to_file('Fermanagh_DCA.geojson', driver='GeoJSON')


# Save the interactive map
m.save('Lower Lough Erne Flood Map.html')
