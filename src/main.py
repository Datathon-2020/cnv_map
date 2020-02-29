import os
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd

geo_data = "../data/custom.geo.json"

confirmed_data_path = "../data/time_series_covid_19_confirmed.csv"
#deaths_data = pd.read_csv("../data/time_series_covid_19_deaths.csv", delimiter=",")
#recovered_data = pd.read_csv("../data/time_series_covid_19_recovered.csv", delimiter=",")


m = f.Map(
    location=[30.97564, 112.2707],
    zoom_start = 6        
)

HEADERS = list(confirmed_data.columns)

def collect_data(csv_file):
    data_in = pd.read_csv(csv_file, delimiter=",")
    data_out = {}
    max = 0
    for i in range(len(data_in[0:])):
        loc_data = {}
        for j in range(2, len(HEADERS)):
            loc_data[HEADERS[j]] = data_in.loc[i, HEADERS[j]]
            if j > 3:
                if data_in.loc[i, HEADERS[j]] > max:
                    max = data_in.loc[i, HEADERS[j]]
            data_out[f"{confirmed_data.loc[i, 'Province/State']}, {confirmed_data.loc[i, 'Country/Region']}"] = loc_data
    data_out["max"] = max
    return data_out
    
def date_data(date, data):
    date_data = []
    for loc in data:
        if loc == "max":
            continue
        point = []
        point.append(round(data[loc]["Lat"],4))
        point.append(round(data[loc]["Long"],4))
        point.append(data[loc][date[0:7]] / float(data["max"]))
        date_data.append(point)
    return date_data

print(date_data("1/22/2020", collect_data(confirmed_data_path)))

#HeatMap(
#    data=date_data("1/22/2020"),
#    name="confirmed",
    
#)

#m.save("index.html")