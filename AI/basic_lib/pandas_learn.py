import pandas as pd

train = pd.read_csv("../线性回归/training_data/train.csv")

print(train.iloc[:, :1].values)
