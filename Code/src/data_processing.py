# This code will be used to pre-possessing the data.

import numpy as np
import pandas as pd
from pandas import DataFrame
from collections import defaultdict
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

# We delte the countries with only one row of values, for which we cannot find the current column mean. 
country_with_one_row_data = []
for country in world_happiness_dict.keys():
    if len(world_happiness_dict.get(country)) == 1:
        country_with_one_row_data.append(country)
print("the countries with only one row of data are:", country_with_one_row_data)
print("We delete these 5")
for country in country_with_one_row_data:
    world_happiness_dict.pop(country, None)

# 2. find all "nan" value and replace it with the current mean of the column of the country:
# traverse all the keys in the dictionary and for each country, 
for country in world_happiness_dict.keys():
    df = pd.DataFrame(world_happiness_dict.get(country))
    for column in range (1,10) :
        mean_value=df[column].mean()
        df[column].fillna(value=mean_value, inplace=True)
        world_happiness_dict[country] = df
# test: print(world_happiness_dict.get("Algeria"))

#3. construct a dataframe to extract 80% of the data as the training data and 20% as the testing data. 
# There are 166 countries within the dataset
# Within the dataset, there are in total 1949 data entries

print(len(world_happiness_dict.keys()))
total = 0


training_set = []
testing_set = []

for country in world_happiness_dict.keys():
    total_data = world_happiness_dict.get(country)
    train, test = train_test_split(total_data, test_size=0.2, random_state=50, shuffle=True)

    training_set.append(train)
    testing_set.append(test)

training_data = pd.concat(training_set)
testing_data = pd.concat(testing_set)

print("Training data dimensions: ", training_data.shape)
print("Testing data dimensions: ", testing_data.shape)
print(training_data)
'''
# Create a Random Forest Regressor object from Random Forest Regressor class:
RFreg = RandomForestRegressor(n_estimators = 50, random_state = 0)
x_train = training_data[2:]
y_train = training_data[1]
RFreg.fit(x_train, y_train)

print(training_data)
'''