import pandas as pd
import os.path 
from stg_stations import stg_stations
from stg_parameters import stg_parameters
from get_metobs import get_recent


if not os.path.isfile("data/stg_stations.csv") or False:
    stg_stations().to_csv("data/stg_stations.csv", index=False)

if not os.path.isfile("data/stg_parameters.csv") or False:
    stg_parameters().to_csv("data/stg_parameters.csv", index=False)


parameters = [2, # Daily average temperature
              5, # Daily rainfall
              4, # Hourly wind speed (10 min average)
              3, # Hourly wind direction (10 min average)
              21,# Hourly wind gust strength
              16,# Hourly cloud coverage (%)
              10,# Hourly sunshine (seconds)
              ]

stations = [82230, # Vänersborg
            97200, # Sthlm Bromma
            ]





stations_df = pd.read_csv("data/stg_stations.csv")
parameters_df = pd.read_csv("data/stg_parameters.csv")


#print(stations_df["name"][stations_df["station_id"]==82230].values)

metobs_data = pd.DataFrame.from_dict({})
for station in stations:
    station_name = stations_df["name"][stations_df["station_id"]==station].values[0]
    for parameter in parameters:
        parameter_name = parameters_df["name"][parameters_df["parameter_id"]==parameter].values[0]
        print(f"Getting {parameter_name} data for {station_name}")
        metobs_data = pd.concat([metobs_data, get_recent(parameter, station)], ignore_index=True)

metobs_data.to_csv("data/metobs_data.csv", index=False)