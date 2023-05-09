import os.path
import geopandas as gpd


# Load the datasets
loughs = gpd.read_file(os.path.abspath('data_files/major_loughs.shp'))
roads = gpd.read_file(os.path.abspath('data_files/Fermanagh roads.shp'))
FloodOne = gpd.read_file(os.path.abspath('data_files/FloodOne.shp'))
FloodTwo = gpd.read_file(os.path.abspath('data_files/FloodTwo.shp'))
FloodThree = gpd.read_file(os.path.abspath('data_files/FloodThree.shp'))
FloodFour = gpd.read_file(os.path.abspath('data_files/FloodFour.shp'))
FloodFive = gpd.read_file(os.path.abspath('data_files/FloodFive.shp'))

gpd.sjoin(roads, loughs)

roads.within(loughs)