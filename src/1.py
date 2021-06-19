# This code will be used to pre-possessing the data.
# This is to teach Jax about local git merging

import numpy as np
import pandas as pd

world_happiness = pd.read_csv ('../data/world-happiness-report.csv')
world_happiness_shape = world_happiness.shape
# print(world_happiness)

world_happiness_2021 = pd.read_csv ('../data/world-happiness-report-2021.csv')
world_happiness_2021_shape = world_happiness_2021.shape
# print(world_happiness_2021)

# there are 373 null values in world_happiness and we currently find which country the null value belongs to 
# and replace it with the mean of the column of that country.

# Get a sample row from the dataset
for element in world_happiness:
    i = 1
    country_array = []
    country_data_array = []
    temp_data = []
    for country in world_happiness.iloc[0][1:]:
        print(country)
        break
        if country not in country_array:
            country_array.append(country)
            country_data_array.append(temp_data)
            temp_data = []
            temp_data.append(world_happiness.loc[i])
            i+=1
        else:
            temp_data.append(world_happiness.loc[i])
            i+=1
# print(country_array)

