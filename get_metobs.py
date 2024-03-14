# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def get_recent(parameter, station):
    url = f'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}/station/{station}/period/latest-months/data.json'
    response = requests.get(url)
    if response.status_code == 200:
        values = response.json()["value"]
        df = pd.DataFrame.from_dict(values)
        df["parameter_id"] = parameter
        df["station_id"] = station
        return df
    #else:
    #    print(f"Returned {response.status_code} for station {station}, parameter {parameter}")




def get_historic(parameter, station):
    url = f"https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}/station/{station}/period/corrected-archive/data.csv"
    response = requests.get(url)
    #response.raise_for_status()
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        lines = [[element for element in line.split(";")] for line in content.split("\n")][50:-1]
        df = pd.DataFrame(lines, columns=["from", "to", "date", "value", "quality"])
        df["parameter_id"] = parameter
        df["station_id"] = station

        return df