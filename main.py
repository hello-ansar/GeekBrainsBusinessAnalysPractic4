import json
import requests

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import pandas as pd
import io

from sklearn.decomposition import PCA


response = requests.get("https://gbcdn.mrgcdn.ru/uploads/asset/2923229/attachment/244a368bcc9591465beba7609ef3ebea.json")
todos = json.loads(response.text)

with open("data_file.json", "w") as write_file:
    json.dump(todos, write_file)

file_ = io.TextIOWrapper(open("data_file.json", "rb"), 'windows-1251')

df = pd.read_json(file_)
print(df.head(5))

df["Operator"] = df.apply(lambda row: row["StationInfo"][0]["Operator"], axis = 1)
df["Base_station"] = df.apply(lambda row: row["StationInfo"][0]["BaseStation"], axis = 1)

del df["ID"]
del df["OnTerritoryOfMoscow"]
del df["StationInfo"]
del df["geoData"]
del df["geodata_center"]

df.rename(columns={"Longitude_WGS84": "Longitude", "Latitude_WGS84": "Latitude"}, inplace=True)

print(df.head(2))


