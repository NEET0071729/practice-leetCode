import pandas as pd
import numpy as np

#CTRL + SHIFT + F10 Run python File

# instance from 1d array it automatically add a index
s = pd.Series(np.random.rand(5))
print(s)

# from a dictionary
s = {'a': 1, 'b' : 2, 'c' : 3}
s = pd.Series(s, dtype="int8")
print(s)

# if index is given it will compare
s = {'a': 1, 'b' : 2, 'c' : 3}
s = pd.Series(s, index= ['b', 'c', 'a', 'd'])
print(s) #NaN(Not a Number) used for missing data in pandas

#pandas specific iloc is location similar to s[0]
print(s.iloc[0])

# the values will be Shown by e^x but the s will remain the same
print(np.exp(s))
print(s)

#like numpy we only have one data type for one column
print(s.dtype)

# making a dataframe using dates
dates = pd.date_range("20200102", periods=6)
print(dates)

# dataframe using a numpy 2d array where row are labeled using dates from before and columns are given by the list function
df = pd.DataFrame(np.random.randn(6 ,4), index=dates, columns=list("ABCD"))
print(df)

# dataframe from dictionary where row are key and column are values
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20000713"),
        "C": pd.Series(1, index=list(range(4)), dtype="int8"),
        "D": np.array([4]*4, dtype="int8"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "Foo"    
    }
)
print(df2)

#print(df2.dtypes)

#To view the top of dataframe
print(df.head())        # Removes last row
print(df.head(1))       # Only one row
#To view the last row of dataframe
print(df.tail())        # Removes only top row
print(df.tail(1))       # Only takes 1 last row

#convert to numpy it doesn't affect df
print(df.to_numpy())

#quick summary of data
print(df.describe())

#Transposing the data (rows into column and column into row)
print(df.T)

# A sorting the column name axis=1 means column AND axis=0 means row name
print(df.sort_index(axis=1, ascending=False))

# A sorting by values in a column
print(df.sort_values(by="B"))

# For a dataframe single label is column it returns a series
print(df["A"])

# For a dataframe a slice[:] then it gives rows, it follows same numbering as list
print(df[1:3])
print(df["20200103":"20200104"]) # this includes both date

#Selecting using loc[] getting a row
print(df.loc[dates[0]])

#Selecting column using column label
print(df.loc[:, ["A", "B"]])

#Label slicing includes the two values
print(df.loc["20200102":"20200104", ["A", "B"]])

#finding a single value
print(df.loc[dates[0], "A"])

#finding a better fast method
print(df.at[dates[0], "A"])

#finding by using position
print(df.iloc[3]) # getting the 4th row
print(df.iloc[3:5, 0:2]) # getting the 4 to 5 row AND 0 to 1 Column
print(df.iloc[[ 1, 2, 4], [0, 2]]) # getting the 2nd, 3rd AND 4th Row while the 1st, 3rd Column
print(df.iloc[3:5, :]) # getting the 4 to 5 row
print(df.iloc[:, 1:3]) # getting the 2 to 3 column
print(df.iloc[3,1]) #getting a value
print(df.iat[ 3, 1]) #getting a value faster

#Boolean editing using condition
print(df[df["A"]>0]) #rows where column A is greater than 0
print(df[df > 0])    #getting the values where value>0
#method for filtering out
df2 = df.copy()
df2["E"] = [ "one", "two", "three", "four", "five", "six"]
print(df2[df2["E"].isin([ "two", "three"])])

#setting a column while the index are compared
s1 = pd.Series([ 1, 2, 3, 4, 5, 6], index=pd.date_range("20200103", periods=6))
df["F"] = s1
print(df)

#Setting value
df.at[dates[0], "A"] = 0 #by column name
print(df)
df.iat[0, 1] = 0         #by using position
print(df)
df.loc[:, "D"] = np.array([5] * len(df)) #can use array or numpy array it also require length of array = number of rows the/ len function gives no. of rows
print(df)
# there is also a where operation
df2 = df.copy()
df2[df2 > 0] = -df
print(df2)

# reindex gives a copy with new index and column
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)

#drop any row that is missing data
print(df1.dropna(how="any"))

#fill any missing data
print(df1.fillna(value=5))

#get the table showing mapping existence of values
print(pd.isna(df1))

#Operation but excluding missing data
print(df.mean())   #mean of each column
print(df.mean(axis=1)) #mean of each row

import matplotlib.pyplot as plt
plt.close(s)