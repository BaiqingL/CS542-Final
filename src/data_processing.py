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

# Get a sample row from the dataset

world_happiness_dict = defaultdict()
for row in range(world_happiness_shape[0]):
    value = world_happiness.loc[row].tolist()
    keys = world_happiness_dict.keys()
    current_country = world_happiness.loc[row][0]
    if (current_country in world_happiness_dict.keys()):
        world_happiness_dict[current_country].append(value[1:])
    else:
        world_happiness_dict[current_country] = value
print(world_happiness_dict.get("Bahrain"))


# [B, 1,2,3, [1,2,3]]