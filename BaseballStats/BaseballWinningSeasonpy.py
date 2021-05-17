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

cubs_df = teams_df[teams_df["franchID"] == "CHC"]
cubs_df = cubs_df[cubs_df["yearID"] < 2020]
cubs_df = cubs_df[cubs_df["yearID"] > 1968]

averageWinsB_df = brewers_df[["W", "G", "Ghome"]].mean()
averageWinsC_df = cubs_df[["W", "G", "Ghome"]].mean()

print(averageWinsB_df)
print(averageWinsC_df)

print(stats.ttest_ind(brewers_df['W'], cubs_df['W'], equal_var=False))
