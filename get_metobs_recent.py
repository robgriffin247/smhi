# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def get_metobs_recent(parameter, station):
    url = f'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}/station/{station}/period/latest-months/data.json'
    response = requests.get(url)
    if response.status_code == 200:
        values = response.json()["value"]
        df = pd.DataFrame.from_dict(values)
        df["parameter_id"] = parameter
        df["station_id"] = station
        #print(f"Data collected for station {station} and parameter {parameter}.")
        return df
    #else:
        #print(f"Returned {response.status_code} for station {station}, parameter {parameter}")