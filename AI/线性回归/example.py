import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

train = pd.read_csv("./training_data/train.csv")
test = pd.read_csv("./training_data/test.csv")
train = train.dropna()
test = test.dropna()
# 使用dropna方法去删除我们数据中的空格行

train.head()
X_train = np.array(train.iloc[:, :-1].values)
y_train = np.array(train.iloc[:, 1].values)
X_test = np.array(test.iloc[:, :-1].values)
y_test = np.array(test.iloc[:, 1].values)
# smodel = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=-1)
# this model is a old style, and it will get the warning
model = make_pipeline(StandardScaler(with_mean=False), LinearRegression())
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)

plt.plot(X_train, model.predict(X_train), color='green')
plt.savefig("./output_img/out1.png")
print(accuracy)
