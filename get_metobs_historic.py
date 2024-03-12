# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def get_metobs_historic(parameter, station):
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