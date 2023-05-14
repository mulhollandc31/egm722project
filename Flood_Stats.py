"""
This file will out put a CSV file for each of the flood levels, the CSV file will contain data for all the roads which
are flooded. In the Python console the total length of road flooded for each flood level as well as a count of the
different class of roads flooded will be output.

"""

import os.path
import geopandas as gpd
import pandas as pd

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

# Spatial Difference Operation
spatial_joinOne = gpd.sjoin(FloodOneRoads, bridges, how='left', predicate='intersects')
FloodOneFinal = spatial_joinOne[spatial_joinOne.index_right.isna()]
FloodOneFinal.to_csv('outputs/FloodOne.csv')

spatial_joinTwo = gpd.sjoin(FloodTwoRoads, bridges, how='left', predicate='intersects')
FloodTwoFinal = spatial_joinTwo[spatial_joinTwo.index_right.isna()]
FloodTwoFinal.to_csv('outputs/FloodTwo.csv')

spatial_joinThree = gpd.sjoin(FloodThreeRoads, bridges, how='left', predicate='intersects')
FloodThreeFinal = spatial_joinThree[spatial_joinThree.index_right.isna()]
FloodThreeFinal.to_csv('outputs/FloodThree.csv')

spatial_joinFour = gpd.sjoin(FloodFourRoads, bridges, how='left', predicate='intersects')
FloodFourFinal = spatial_joinFour[spatial_joinFour.index_right.isna()]
FloodFourFinal.to_csv('outputs/FloodFour.csv')

spatial_joinFive = gpd.sjoin(FloodFiveRoads, bridges, how='left', predicate='intersects')
FloodFiveFinal = spatial_joinFive[spatial_joinFive.index_right.isna()]
FloodFiveFinal.to_csv('outputs/FloodFive.csv')

FloodInputs = ['outputs/FloodOne.csv', 'outputs/FloodTwo.csv', 'outputs/FloodThree.csv',
               'outputs/FloodFour.csv', 'outputs/FloodFive.csv']
for FloodInput in FloodInputs:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(FloodInput)

    # Find the empty columns
    empty_columns = data.columns[data.isnull().all()]

    # Find the populated columns
    populated_columns = data.columns[data.notnull().any()]

    # Filter the DataFrame to keep only the populated columns
    data = data[populated_columns]

    # Define the output filename
    output_filename = FloodInput.replace('.csv', 'Final.csv')

    # Save the modified DataFrame to a new CSV file
    data.to_csv(output_filename, index=False)

# Select the length column from each flood csv file
LengthOne = FloodOneFinal['Length_left']
LengthTwo = FloodTwoFinal['Length_left']
LengthThree = FloodThreeFinal['Length_left']
LengthFour = FloodFourFinal['Length_left']
LengthFive = FloodFiveFinal['Length_left']

# Select the class column from each flood csv file
CountOne = FloodOneFinal['CLASS_left']
CountTwo = FloodTwoFinal['CLASS_left']
CountThree = FloodThreeFinal['CLASS_left']
CountFour = FloodFourFinal['CLASS_left']
CountFive = FloodFiveFinal['CLASS_left']

# Print the total length of roads flooded as well as a count of the types of roads affected by the floods
FloodOneLength = LengthOne.sum()/1000
print('Total length of roads flooded by the lough rising by 1m is {} kilometers'.format(FloodOneLength))
FloodOneCount = CountOne.value_counts()
print('A count of all the class of roads affected by the floods')
print(FloodOneCount)
FloodTwoLength = LengthTwo.sum()/1000
print('Total length of roads flooded by the lough rising by 2m is {} kilometers'.format(FloodTwoLength))
FloodTwoCount = CountTwo.value_counts()
print('A count of all the class of roads affected by the floods')
print(FloodTwoCount)
FloodThreeLength = LengthThree.sum()/1000
print('Total length of roads flooded by the lough rising by 3m is {} kilometers'.format(FloodThreeLength))
FloodThreeCount = CountThree.value_counts()
print('A count of all the class of roads affected by the floods')
print(FloodThreeCount)
FloodFourLength = LengthFour.sum()/1000
print('Total length of roads flooded by the lough rising by 4m is {} kilometers'.format(FloodFourLength))
FloodFourCount = CountFour.value_counts()
print('A count of all the class of roads affected by the floods')
print(FloodFourCount)
FloodFiveLength = LengthFive.sum()/1000
print('Total length of roads flooded by the lough rising by 5m is {} kilometers'.format(FloodFiveLength))
FloodFiveCount = CountFive.value_counts()
print('A count of all the class of roads affected by the floods')
print(FloodFiveCount)