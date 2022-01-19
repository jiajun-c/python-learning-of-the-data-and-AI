# pandas basic use
## 1. create a pandas
```python
s = pd.Series([1, 3, 5, np.nan, 7, 8])
```
using the `np.nan` means the value in this place is infite or wrong
We can also use the `data = pd.date_range("20201212", periods=6)
`to create the date in after the 202021212
If you wants to initlize every column differently, we should initlize like as json
```python
df2 = pd.DataFrame(
    {
        "A": 1,
        "B": pd.Timestamp("20121111"),
        "C": np.array([2] * 4),
        "D": pd.Series(1, index=list(range(4))),
        "E": ["11", "22", "33", "44"],
    }
)
```
the output is
```python
   A          B  C  D   E
0  1 2012-11-11  2  1  11
1  1 2012-11-11  2  1  22
2  1 2012-11-11  2  1  33
3  1 2012-11-11  2  1  44
```
## 2. silce the pandas
You can use the function to cut from the head or from the tail.
```python
df.head(1)
# it will cut from the top to the line 1
df.tail(3)
# it will cut two lines from the tail of the df
```

## 3. see the index or the column
```python
df.index()
df.columns()
```

## 4.see the specific rows or the columns
### select according to the lable
```python
df.loc["20121111"]
# It will return the line with the index "20121111"
df.loc[data[0]:data[3]m, ["A","B"]]
```
If you use the `a:b` ,it means you select from the a to b, else it is select the one with the lable list
You should be attention that the all are start from the 0

### select according to the position
```python
print(df.iloc[3])
print(df)
print(df.iloc[1:3, 0:2])

print(df.iloc[[1,3,4], [1,2]])
```