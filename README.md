##Ett projekt för att öva på min visualiseringsförmåga och göra mig bekväm i seaborn och pandas 

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Datan är hämtad från OECD "https://data.oecd.org/price/housing-prices.htm"
Pandas är som tur är väldigt likt Tidyverse, så det är bara att läsa in en csv-fil
och sedan är det mindre formalia att tvätta datan och ta fram vad en är ute efter.
Genom att göra en funktion med "indicator" som input kan jag fritt välja vilken indicator jag vill undersöka från bostadsmarknadsdata
```
house_price = pd.read_csv("HOUSE_PRICES.csv").replace(' ', '')

og_house_price = house_price
def graph_nordic(house_price, indicator):
    house_price = house_price
    indicator = indicator
    price = house_price.loc[house_price["Indicator"] == indicator]
    price = price.loc[0:, ["Country", "Time", "Value"]]
    price["Rent prices"] = price["Value"]
    price["Rent prices"] = price["Rent prices"]-4
    price[["Quarter", "Year"]] = price["Time"].str.split("-", expand=True)
    price = price.loc[house_price["Country"].isin(["Sweden", "Norway", "Finland", "Denmark"])]

    return price
```

##Genom att använda seaborn och matplotlib kan jag enkelt formatera några fina grafer över hur prisutvecklingen skiljer sig mellan bostadsmarknaden
##och hyresmarknaden
```
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))

sns.set(font_scale=1)
g1=sns.lineplot(ax=axes[0], data=graph_nordic(og_house_price, "Rent prices, s.a."), x="Time", y="Rent prices", hue="Country")
g2=sns.lineplot(ax=axes[1], data=graph_nordic(og_house_price, "Real house price indices, s.a."), x="Time", y="Rent prices", hue="Country")
g1.set(title="House price development of the Nordic countries")
g2.set(title ="Rent price development of the Nordic countries")
g1.tick_params(labelsize=5)
g2.tick_params(labelsize=5)
g1.set_ylim([90, 140])
g1.set_ylabel("Cost to buy (%)")
g2.set_ylim([90, 140])
g1.set_ylabel("Cost to rent (%)")
plt.show()
```
![Figure_1](https://user-images.githubusercontent.com/106667697/228610412-d7ec103d-7568-46f4-9de8-1b7a631bbd5f.png)
