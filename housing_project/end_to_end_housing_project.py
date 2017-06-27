#############################################
# load data and end to end project on that
#############################################

import os
import pandas as pd

# folder name for the data file
HOUSING_PATH = "data_science\housing_project\housing_data"
print(HOUSING_PATH)

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
housing.head()

housing.info()
housing["ocean_proximity"].value_counts()
# summary of numerical attribute
housing.describe()


##############################################
# plotting by matplotlib
#############################################

import matplotlib.pyplot as plt

# histogram for numerical attribute
housing.hist(bins = 50, figsize=(20, 15))
plt.show()

#############################################
# training and test set
#############################################

import numpy as np
import numpy.random as rnd

def split_train_test(data, test_ratio):
    shuffled_indices = rnd.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
train_set.head()
print(len(train_set), "train +", len(test_set), "test")

# if the prgoram is run again, it will generate different test set, over time
# machine learning algorithm will get to see the whole data set, avoid this by setting
# rnd.seet(42) before calling rnd.permutation(), so that it always generate the same shuffled indices



# for updated data set, the above solution breakdown.

###################################################
# discover and visualize the data to gain insights
###################################################