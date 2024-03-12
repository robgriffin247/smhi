# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def stg_parameters():
    response = requests.get(f"https://opendata-download-metobs.smhi.se/api/version/1.0.json")
    parameter_ids = [resource["key"] for resource in response.json()["resource"]]
    parameter_names = [resource["title"] for resource in response.json()["resource"]]
    df =pd.DataFrame.from_dict({'parameter_id':parameter_ids, 'parameter_name':parameter_names})    
    return df.drop_duplicates()
