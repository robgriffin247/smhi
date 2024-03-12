import requests
import pandas as pd

from stg_stations import stg_stations
from stg_metobs_recent import stg_metobs_recent
from stg_parameters import stg_parameters

stations = stg_stations()["station_id"]
parameters = stg_parameters()["parameter_id"]

df = pd.DataFrame.from_dict({})
for parameter in parameters:
    for station in stations:
        df = pd.concat([df, stg_metobs_recent(parameter, station)], ignore_index=True)

print(df)