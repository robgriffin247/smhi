import pandas as pd

df = pd.read_csv("data/metobs_data.csv")

print(len(df))
print(len(df.drop_duplicates(station, date, from, to)))