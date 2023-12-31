import pandas as pd
# Functions
# Pandas provide a large number of predefined functions that can be applied on the data structures seen above. Some of the most used in data analysis are:

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
d1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
d2 = pd.DataFrame([[7, 8, 9], [10, 11, 12]])

print(s1)
print(s2)
print(d1)
print(d2)
print('*****')
# Arithmetic operations
print("Sum of series: ",s1.add(s2)) # also s1 + s2
print("Sum of DataFrames: ",d1.add(d2))
print('*****')
# Statistical operations
# They can be applied to both series and dataframes.
# Pandas provide a large number of predefined functions that can be applied on the data structures seen above. Some of the most used in data analysis are:
print("Mean: ",s1.mean())
print("Median: ",s1.median())
print("Number of elements: ",s1.count())
print("Standard deviation: ",s1.std())
print("Variance: ",s1.var())
print("Maximum value: ",s1.max())
print("Minimum value: ",s1.min())
print("Correlation: ",s1.corr(s2))
print("Statistic summary: ",s1.describe())
print('*****')
# Custom functions can also be applied to the data structures seen above. To do this, we have to program the function to receive a value (or a column or row in the case of a DataFrame) 
# and return another modified one, and reference it with apply. In addition, this function allows using lambda expressions for the anonymous declaration of functions.
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# Explicit function
def squared(x):
    return x**2
s1 = s.apply(squared)
print(s1)
# Lambda expression or anonymous function
s2 = s.apply(lambda x: x**2)
print(s2)
print('*****')
# Custom functions to DataFrames
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})
print(df)
# Apply function along a column
df["A"] = df["A"].apply(lambda x: x**2)
print(df)
# Apply function along a row
df.loc[0] = df.loc[0].apply(lambda x: x**2)
print(df)
print('*****')
# Apply function to all elements
df = df.applymap(lambda x: x**2)    # applymap applies a function to all the elements of the DataFrame
print(df)
print('*****')

