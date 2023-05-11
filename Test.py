import os.path
import geopandas as gpd
import pandas as pd
import numpy as np

# pd.set_option('display.max_columns', None)

# Load the datasets
loughs = gpd.read_file(os.path.abspath('data_files/major_loughs.shp'))
roads = gpd.read_file(os.path.abspath('data_files/Fermanagh roads.shp'))
FloodOne = gpd.read_file(os.path.abspath('data_files/FloodOne.shp'))
FloodTwo = gpd.read_file(os.path.abspath('data_files/FloodTwo.shp'))
FloodThree = gpd.read_file(os.path.abspath('data_files/FloodThree.shp'))
FloodFour = gpd.read_file(os.path.abspath('data_files/FloodFour.shp'))
FloodFive = gpd.read_file(os.path.abspath('data_files/FloodFive.shp'))

# Intersect operation to find roads already crossing the lough polygon, these are bridges.
bridges = gpd.overlay(roads, loughs, how='intersection')

# Intersect operation to find the roads intersected by the different flood levels
FloodOneRoads = gpd.overlay(roads, FloodOne, how='intersection')
FloodTwoRoads = gpd.overlay(roads, FloodTwo, how='intersection')
FloodThreeRoads = gpd.overlay(roads, FloodThree, how='intersection')
FloodFourRoads = gpd.overlay(roads, FloodFour, how='intersection')
FloodFiveRoads = gpd.overlay(roads, FloodFive, how='intersection')

# Rename the primary key column in bridges dataset
bridges = bridges.rename(columns={'OBJECTID_1': 'Key'})

# Rename the primary key column in the flood datasets
FloodOneRoads = FloodOneRoads.rename(columns={'OBJECTID': 'Key'})
FloodTwoRoads = FloodTwoRoads.rename(columns={'OBJECTID': 'Key'}),
FloodThreeRoads = FloodThreeRoads.rename(columns={'OBJECTID': 'Key'}),
FloodFourRoads = FloodFourRoads.rename(columns={'OBJECTID': 'Key'}),
FloodFiveRoads = FloodFiveRoads.rename(columns={'OBJECTID': 'Key'})

# Spatial Difference Operation
spatial_join = gpd.sjoin(FloodOneRoads, bridges, how='left', predicate='intersects')
FloodOneFinal = spatial_join[spatial_join.index_right.isna()]
FloodOneFinal.to_csv('outputs/FloodOne.csv')

# Read the CSV file into a DataFrame
data = pd.read_csv('outputs/FloodOne.csv')

# Find the empty columns
empty_columns = data.columns[data.isnull().all()]

# Find the populated columns
populated_columns = data.columns[data.notnull().any()]

# Filter the DataFrame to keep only the populated columns
data = data[populated_columns]

# Save the modified DataFrame to a new CSV file
data.to_csv('outputs/FloodOne.csv', index=False)

print(FloodOneFinal)




