import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 7, 8])
print(s)

data = pd.date_range("20201212", periods=6)
print(data)

# the np.random.randn(d0,d1)means the shape of the function
df = pd.DataFrame(np.random.randn(6, 4), index=data, columns=list("ABCD"))
print(df)

normal_disturute = 4 + 4 * np.random.randn(100000)
# 使用此可以得到N(4,4)的正太分布
plt.hist(normal_disturute, bins=100)
# plt.show()

df2 = pd.DataFrame(
    {
        "A": 1,
        "B": pd.Timestamp("20121111"),
        "C": np.array([2] * 4),
        "D": pd.Series(1, index=list(range(4))),
        "E": ["11", "22", "33", "44"],
    }
)
print(df2)

# view the data
# if you do not pass the parament to it, it will see the all
print("start from the tail\n")
print(df2.head(3))
print(df2.tail(2))
# see from the tail
print(df2.tail(2))

# see the index, it is the index of the row
print(df.index)

# see the columns, it is the index of the columns
print(df.columns)

# turn the pd to the np
print(df.to_numpy())

# you can also transport the pd
print(df.T)

# select the row
# get the single column
print(df['A'])
print(df[0:3])
print(df["20201212": "20201214"])

# select by the label

print(df.loc[data[0]])
print(df[0:1])

# they are different because they have the different return type

print(df.loc["20201212", ["A", "B"]])

print(df.loc[data[0]: data[3], ["A", "B"]])

# select by the position
# it is the third line
print(df.iloc[3])
print(df)
print(df.iloc[1:3, 0:2])

print(df.iloc[[1,3,4], [1,2]])