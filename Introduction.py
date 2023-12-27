import pandas as pd
import numpy as np


# 1. Series
# One-dimensional labeled data structure. It is similar to a 1D array in Numpy, but has an index that allows access to the values by label
print('1. Series')
serie = pd.Series([1, 2, 3, 4, 5]) # using Series class
print(serie)
# This will create a series with elements 1, 2, 3, 4 and 5. In addition, since we have not included information about the indexes, an automatic index is generated starting at 0.
print('*****')
serie = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']) # using Series class
print(serie)
# the previous series has an index composed of letters.
# In a series its elements can be accessed by index or by position (the latter is what we did in Numpy). Below are some operations that can be performed using the above series:
print('*****')
# Access the third element of the series
print(serie["c"]) # Using index
print(serie[2]) # Using position
print('*****')
# Change the value of the second element
serie["b"] = 7 # Using index
print(serie)
print('*****')
# Add 10 to all elements of the series
serie = serie + 10 # also serie += 10
print(serie)
print('*****')
# Calculate the sum of the elements of the series
sum_all = serie.sum()
print(sum_all)
print('*****')
# 2. DataFrame
# Two-dimensional labeled data structure. It is similar to a 2D array in Numpy, but has an index that allows access to the values by label and rows and columns can be labeled.
print('2. DataFrame')
# dataframe = pd.DataFrame(data, index, columns)
# data: data to be inserted in the dataframe
# index: index of the dataframe
# columns: columns of the dataframe
# Let's create a dataframe using the DataFrame class:
dataframe = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # using DataFrame class, this will create a DataFrame with three rows and three columns each row.
print(dataframe)
print('*****')
# create a new DataFrame with concrete indexes for rows and columns 
data = {
    "col A": [1, 2, 3],
    "col B": [4, 5, 6],
    "col C": [7, 8, 9]
}

dataframe = pd.DataFrame(data, index=["a", "b", "c"]) # Custom index is provided for the columns (labeling rows within a dictionary)
print(dataframe)
print('*****')
# The above elements can be accessed by index or by position. Below are some operations that can be performed using the above dataframe:
# Access all the data in a column
print(dataframe["col A"]) # Using index
print(dataframe.loc[:, "col A"]) # Using index
print(dataframe.iloc[:, 0]) # Using position
print('*****')
# Access all the data in a row
print(dataframe.loc["a"]) # Using index
print(dataframe.iloc[0]) # Using position
print('*****')
# Access a specific element
print(dataframe["col A"]["a"]) # Using index
print(dataframe.loc["a", "col A"]) # Using index
print(dataframe.iloc[0, 0]) # Using position
print('*****')
# create a new column
dataframe["col D"] = [10, 11, 12]
print(dataframe)
print('*****')
# create a new row
dataframe.loc["d"] = [13, 14, 15, 16]   
print(dataframe)
print('*****')
# multiply by 10 to elements of a column
dataframe["col A"] = dataframe["col A"] * 10 # also dataframe["col A"] *= 10
print(dataframe)
print('*****')
# calculate the sum of all elements 
sum_all = dataframe.sum()          
print(sum_all)  
print('*****')


