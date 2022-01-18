import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

train = pd.read_csv("./training_data/train.csv")
test = pd.read_csv("./training_data/test.csv")
x = np.array(train.iloc[:, :-1].values)
y = np.array(train.iloc[:, :-1].values)
x_test = np.array(train.iloc[:, :-1].values)
y_test = np.array(train.iloc[:, :-1].values)
model = make_pipeline(StandardScaler(with_mean=False), LinearRegression())
# model = make_pipeline(StandarderScaler())
# model = LinearRegression(fit_intercept=1, normalize=1, copy_X=1, n_jobs=-1)
model.fit(x, y)

y_prd = model.predict(x_test)
accuracy = model.score(x_test, y_test)

plt.plot(x, model.predict(x))
plt.show()
print(accuracy)
# data = np.loadtxt("./training_data/train.csv", delimiter=",")
