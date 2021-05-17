import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import datasets, linear_model
import requests
import io

#Request teams file
requestData = requests.get('https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/Teams.csv').content

#Import Teams file
teams_df = pd.read_csv(io.StringIO(requestData.decode('utf-8')))

#Filter by brewers only
#And before 2020
brewers_df = teams_df[teams_df["franchID"] == "MIL"]
brewers_df = brewers_df[brewers_df["yearID"] < 2020]

print(brewers_df[["yearID", "W", "3B"]])

#Generate scatterplot

brewers_df.plot.scatter(x="W", y='3B',c='Black')
#Linear regression, generate X and Y values

x_values = brewers_df["W"].values
y_values = brewers_df["3B"].values

x_values = x_values.reshape(-1, 1)
y_values = y_values.reshape(-1, 1)

#Calculate Linear Regression data
regr = linear_model.LinearRegression()
regr.fit(x_values, y_values)

print("Coefficient: {0} Intercept: {1}".format(regr.coef_, regr.intercept_))

slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(x_values[:,0], y_values[:,0])
print("Wins vs 3b slope: {0} intercept: {1} p_value: {2} std_err: {3}".format(slope_1, intercept_1, r_value_1, p_value_1, std_err_1))

# plot it as in the example at http://scikit-learn.org/
plt.plot(x_values, regr.predict(x_values), color='blue', linewidth=3)
plt.show()