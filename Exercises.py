import numpy as np
import pandas as pd

# Exercises
# Exercise 01: Create a series from a list, a Numpy array and a dictionary and print it.
print("Creation of Series and DataFrames")
print("Exercise 01: Create a series from a list, a Numpy array and a dictionary and print it.")
print("From list: ")
l = [1, 2, 3, 4, 5]
s = pd.Series(l)
print(s)
print("From Numpy array: ")
a = np.array([1, 2, 3, 4, 5])
s = pd.Series(a)
print(s)
print("From dictionary: ")
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s = pd.Series(d)
print(s)
print('*****')
# Exercise 02: Create a DataFrame from a Numpy array, a dictionary and a list of tuples and print it
print("Exercise 02: Create a DataFrame from a Numpy array, a dictionary and a list of tuples and print it")
print("From Numpy array: ")
a = np.random.randint(0, 10, size= (5, 5)) # 5x5 matrix with random numbers between 0 and 10
df = pd.DataFrame(a)
print(df)
print(" ")
print("From dictionary: ")
d = {
    "A": np.random.randint(10, 100, size= 5),
    "B": np.linspace(1, 10, 5), # 5 numbers between 1 and 10
    "C": np.random.randn(5)
}
df = pd.DataFrame(d)
print(df)
print(" ")
print("From list of tuples: ")
t = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
df = pd.DataFrame(t)
print(df)
print(' ')
# Exercise 03: Create 2 series and use them to build a DataFrame
print("Exercise 03: Create 2 series and use them to build a DataFrame")
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([6, 7, 8, 9, 10])
# Method 1
df = pd.DataFrame({
    "A": s1,
    "B": s2
})
print(df)
print(" ")
# Method 2
df = pd.DataFrame()
df["A"] = s1
df["B"] = s2
print(df)
print(' ')
# Method 3 using concat function
df = pd.concat([s1, s2], axis=1)
print(df)
print(' ')
# Method 4 using join() function and pd.Series.to_frame() function


# Exercise 04: Use the series created in the previous exercise and select the positions of the elements of the first series that are in the second series
print("Filtering and updating")
print("Exercise 04: Use the series created in the previous exercise and select the positions of the elements of the first series that are in the second series")
print("Method 1: ")
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
filtering_results = s1.isin(s2)
indices = s1[filtering_results].index
print(indices)
print(" ")
print("Method 2: using numpy where() function")
indices = np.where(s1.isin(s2))
print(indices)
print(' ')
print("Method 3: using python")
indices = []
for i in range(len(s1)):
    if s1[i] in s2.values:
        indices.append(i)
print(indices)
# Exercise 05: Use the series created in exercise 04 and list the elements that are not common between both series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
print("Exercise 05: Use the series created in exercise 04 and list the elements that are not common between both series")
print("Method 1: using numpy concatenate() function")
s1_uniques = s1[~s1.isin(s2)]
s2_uniques = s2[~s2.isin(s1)]
unique_elements = np.concatenate([s1_uniques, s2_uniques]) # concatenate both series
print(unique_elements)
print(" ")
print("Method 2: using pandas concat() function")
s1_uniques = s1[~s1.isin(s2)]
s2_uniques = s2[~s2.isin(s1)]
unique_elements = pd.concat([s1_uniques, s2_uniques]) # concatenate both series
print(unique_elements)
print(" ")
print("Method 3: using python")
unique_elements = []
for i in range(len(s1)):
    if s1[i] not in s2.values:
        unique_elements.append(s1[i])
for i in range(len(s2)):
    if s2[i] not in s1.values:
        unique_elements.append(s2[i])
print(unique_elements)
print(' ')
# Exercise 06: Create a DataFrame of random numbers with 5 columns and 10 rows and sort one of its columns from smallest to largest 
print("Exercise 06: Create a DataFrame of random numbers with 5 columns and 10 rows and sort one of its columns from smallest to largest ")
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 5)))
print(df)
print(" ")
print("Sorting column 0: ")
df = df.sort_values(by=[0])
print(df)
print(' ')
# Exercise 07: Modify the name of the 5 columns of the above DataFrame to the following format: N_column where N is the column number 
print("Exercise 07: Modify the name of the 5 columns of the above DataFrame to the following format: N_column where N is the column number ")
df.columns = ["{}_column".format(i) for i in range(5)]  # using list comprehension
print(df)
print(' ')
# Exercise 08: Modify the index of the rows of the DataFrame of exercise 06
print("Exercise 08: Modify the index of the rows of the DataFrame of exercise 06")  
df.index = ["row_{}".format(i) for i in range(10)]  # using list comprehension
print(df)
print(' ')
 


