import pandas as pd
import requests
import os
import base64
import json
import matplotlib.pyplot as plt
import seaborn as sns


house_price = pd.read_csv("HOUSE_PRICES.csv").replace(' ', '')

og_house_price = house_price
def graph_nordic(house_price, indicator):
    house_price = house_price
    indicator = indicator
    rent_price = house_price.loc[house_price["Indicator"] == indicator]
    rent_price = rent_price.loc[0:, ["Country", "Time", "Value"]]
    rent_price["Rent prices"] = rent_price["Value"]
    rent_price["Rent prices"] = rent_price["Rent prices"]-4
    rent_price[["Quarter", "Year"]] = rent_price["Time"].str.split("-", expand=True)
    rent_price = rent_price.loc[house_price["Country"].isin(["Sweden", "Norway", "Finland", "Denmark"])]

    return rent_price

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))

sns.set(font_scale=1)
g1=sns.lineplot(ax=axes[0], data=graph_nordic(og_house_price, "Rent prices, s.a."), x="Time", y="Rent prices", hue="Country")
g2=sns.lineplot(ax=axes[1], data=graph_nordic(og_house_price, "Real house price indices, s.a."), x="Time", y="Rent prices", hue="Country")
g1.set(title="House price development of the Nordic countries")
g2.set(title ="Rent price development of the Nordic countries")
g1.tick_params(labelsize=5)
g2.tick_params(labelsize=5)
g1.set_ylim([100, 140])
g2.set_ylim([100, 140])
plt.show()