# egm722project

Hello thank you for downloading this Python Script. 
The purpose of this script is to detect all roads which will be flooded using predetermined flood projections.

------------------------------------------------------------------------------------How to Install the Python Package----------------------------------------------------------------------------------
The following steps will provide a step-by-step guide on how to access and run the code to create the desired outputs.

1.	Using the link above access the GitHub repository, from here the python package can be downloaded.
2.	Create a fork of the repository, this will copy the entire repository over to the GitHub account you are signed into.
3.	To clone the repository, open the GitHub desktop app. Cloning the repository will download the repository to your computer and create a local version.
4.	From the GitHub main screen select “Show in Explore”, this will open the cloned folder in Windows Explorer. 
5.	The environment file must be installed to ensure all the required dependencies are available. Using Anaconda Navigator install the environment file, this is called “environmentFlooding.YML”.

-------------------------------------------------------------------------------------Running the Python Files-------------------------------------------------------------------------------------------
The following steps will provide a guide of how to access, run and view the outputs generated from the Python package. All input data is provided within the “data_files” folder in the repository.

1.	From the previously opened Windows Explorer window right click on the file “Fermanagh_Map” and select open with PyCharm.
2.	Run this script and it will produce a map of the study area, this image can be found within the “outputs” folder, it is called “StudyAreaMap”. The map will open in an image viewer.
3.	From the Windows Explorer window right click on the file “Lower_Lough_Erne” and select open with PyCharm.
4.	Run the code in this file, an interactive map will be created and saved within the “outputs” folder as “LowerLoughErneFloodMap”. 
5.	The map can be opened using a web browser, flood layers can be toggle on and off allowing for flooded roads to be identified on the base map.
6.	From the Windows Explorer window right click on the file “Flood_Stats” and select open with PyCharm.
7.	Running this file will create CSV file in the outputs folder, the folder of interest are ladled “FloodxxxxFinal”, these files contain a list of all the roads flooded in each flood scenario.
8.	In the console window the total length of roads flooded will be printed, as well as a count of how many of each type of road is flooded.
