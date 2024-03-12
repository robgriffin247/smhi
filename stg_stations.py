# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def stg_stations():
    df = pd.DataFrame.from_dict({})
    response = requests.get(f"https://opendata-download-metobs.smhi.se/api/version/1.0.json")

    # Get all the parameter ids to iterate through
    for parameter in [resource["key"] for resource in response.json()["resource"]]:
        # Get the stations for iterated parameter and append to df
        response = requests.get(f"https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}.json")
        station_ids = [station["key"] for station in response.json()["station"]]
        station_names = [station["title"].split("- ")[1] for station in response.json()["station"]]
        df = pd.concat([df, 
                        pd.DataFrame.from_dict({"station_id": station_ids, 
                                                "station_name": station_names, 
                                                #"parameter": parameter
                                                })], 
                                                ignore_index=True)
    
    return df.drop_duplicates()
