import pandas as pd
import os.path 
from stg_stations import stg_stations
from stg_parameters import stg_parameters
from get_metobs import get_recent, get_historic

parameters = [2, 5]
stations = [82230]


# Stations and Parameters data -------------------------------------------------
if not os.path.isfile("data/stg_stations.csv") or False:
    stg_stations().to_csv("data/stg_stations.csv", index=False)

if not os.path.isfile("data/stg_parameters.csv") or False:
    stg_parameters().to_csv("data/stg_parameters.csv", index=False)
# ------------------------------------------------------------------------------


# Metobs data ------------------------------------------------------------------
if not os.path.isfile("data/metobs_data.csv") or False:
    metobs_df = pd.DataFrame.from_dict({"station_id":[], "parameter_id":[]})
else:
    metobs_df = pd.read_csv("data/metobs_data.csv")

for parameter in parameters:
    for station in stations:
        if True: #station not in metobs_df["station_id"] and parameter not in metobs_df.loc[metobs_df["station_id"]==station]["parameter_id"]:
            print(f"Gathering {parameter} for {station}")
            recent = get_recent(parameter, station)
            historic = get_historic(parameter, station)
            metobs_df = pd.concat([metobs_df,
                                   recent,
                                   historic],
                                   ignore_index=True)
            metobs_df = metobs_df.drop_duplicates()
            #metobs_df["parameter_id"] = metobs_df["parameter_id"].astype("int")
            #metobs_df["station_id"] = metobs_df["station_id"].astype("int")
            metobs_df.to_csv("data/metobs_data.csv", index=False)
        else:
            print(f"Data already present for {parameter} at {station}")

print(metobs_df)
#print(metobs_df["parameter_id"].astype("int").astype("str") + "_"  + metobs_df["station_id"].astype("int").astype("str"))

"""
[x] Check for metobs_data.csv
[x] Load if present
[ ] Check if station and parameter already present
[ ] Check for last date (run get_recent if > 40 days ago)
[x] Concat to existing data
[x] Remove duplicates
[x] Save on each loop
"""