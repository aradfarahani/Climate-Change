# Datasheet: *Global temperature data* Lab 3

Author: DeepLearning.AI (DLAI)

Files:
	global_temperature.csv
	.png files in NASA subfolder

## Motivation

The data is a collection of global temperature mesurements. The data comes from two sources: National Oceanic and Atmospheric Administration (NOAA) and National Aeronautics and Space Administration (NASA).

The dataframe global_temperature.csv was downloaded from the National Oceanic and Atmospheric Administration (NOAA) (various datasets available here: https://www.ncei.noaa.gov/access/search/index)
The .png files are from National Aeronautics and Space Administration (NASA) (available here: https://climate.nasa.gov/climate_resources/139/video-global-warming-from-1880-to-2022/)

The data was downloaded to be used in the DLAI course "AI for Climate Change". 

## Composition

global_temperature.csv

The dataset contains the temperature measurements for various (794) stations around the world between 1880 and 2021. The dataset includes the following columns: STATION, NAME, LATITUDE, LONGITUDE. The rest of the column names are years from 1880 to 2021. Each row represents one measuring station and the yearly data is in the corresponding columns.
The metadata columns are all fully populated, but there is some missing temperature data for various years at some stations.

.png files in NASA subfolder

The files are global world maps with a superimposed heatmap of the temperature change with respect to the NASA's baseline period (1951-1980). The images show the time range between years 1884 and 2020. 
