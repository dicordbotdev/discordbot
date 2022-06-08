# import urllib library
from urllib import response
from urllib.request import urlopen

import json
import pandas as pd
import matplotlib.pyplot as plt

city = input("Enter City: ")
tier = input("Select Tier: ")
ench = input("Select Enchantment: ")

if int(ench)==int(0):
    url = "https://www.albion-online-data.com/api/v2/stats/prices/T" + tier + "_ARMOR_CLOTH_SET3?locations=" + city + "&qualities="
else:
    url = "https://www.albion-online-data.com/api/v2/stats/prices/T"+ tier + "_ARMOR_CLOTH_SET3@" + ench + "?locations=" + city + "&qualities="

response = urlopen(url)

data_json = json.loads(response.read())

df = pd.json_normalize(data_json)
print(df["quality"],df["sell_price_min"])