import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing, cluster
import scipy

import folium
import geopy

import warnings

warnings.filterwarnings('ignore')

from sklearn.cluster import KMeans

df = pd.read_csv("C:/Users/Ансар/PycharmProjects/GeekBrainsBusinessAnalysPractic4/Lesson_5.csv")
print(df.head(3))

del df["State/Province"]
del df["Postcode"]
del df["Phone Number"]
del df["Store Name"]

print(df.head(3))

print(df["Store Number"].value_counts().sort_values(ascending=False))

print(df.loc[df["Store Number"] == "19773-160973"])

df = df.drop(np.where(df["Store Number"] == "19773-160973") and np.where(pd.isna(df['Longitude']) == True)[0])

print(df["Store Number"].value_counts().sort_values(ascending=False))

df.set_index(df["Store Number"], inplace = True)

df.info()

df.fillna("No_data", inplace=True)


import sweetviz as sv

feature_config = sv.FeatureConfig(skip=["Store Number", "Street Address"])

report = sv.analyze(df, feat_cfg=feature_config)

report.show_html('Lesson_5_report.html')


