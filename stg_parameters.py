# https://opendata.smhi.se/apidocs/metobs/
import requests
import pandas as pd

def stg_parameters():
    response = requests.get(f"https://opendata-download-metobs.smhi.se/api/version/1.0.json")
    resource = response.json()["resource"]
    df = pd.DataFrame.from_dict({
        "parameter_id":[resource["key"] for resource in resource], 
        "name":[resource["title"] for resource in resource], 
        "summary":[resource["summary"] for resource in resource], 
        "unit":[resource["unit"] for resource in resource]})
    return df.drop_duplicates(subset=["parameter_id"], keep="first")
