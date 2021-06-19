# This code will be used to pre-possessing the data.
# This is to teach Jax about local git merging

import numpy as np
import pandas as pd
from collections import defaultdict

world_happiness = pd.read_csv ('../data/world-happiness-report.csv')
world_happiness_shape = world_happiness.shape
# print(world_happiness)

world_happiness_2021 = pd.read_csv ('../data/world-happiness-report-2021.csv')
world_happiness_2021_shape = world_happiness_2021.shape

# print(world_happiness_2021)

# there are 373 null values in world_happiness and we currently find which country the null value belongs to 
# and replace it with the mean of the column of that country.

# 1. create a dictionary with keys of countries and values of their data:

world_happiness_dict = defaultdict()
for row in range(world_happiness_shape[0]):
    value = world_happiness.loc[row].tolist()
    keys = world_happiness_dict.keys()
    current_country = world_happiness.loc[row][0]
    if (current_country in world_happiness_dict.keys()):
        world_happiness_dict[current_country].append(value[1:])
    else:
        world_happiness_dict[current_country] = [value[1:]]

# 2. find all "nan" value and replace it with the current mean of the column of the country:
# traverse all the keys in the dictionary and for each country, 
print("Before:",pd.DataFrame(world_happiness_dict.get("Algeria")))
for country in world_happiness_dict.keys():
    df = pd.DataFrame(world_happiness_dict.get(country))
    for column in range (1,10) :
        mean_value=df[column].mean()
        df[column].fillna(value=mean_value, inplace=True)
        world_happiness_dict[country] = df
print("After:", world_happiness_dict.get("Algeria"))