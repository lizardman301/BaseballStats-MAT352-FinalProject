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

#Get 5 teams brewers, cubs, twins, and yankees

brewers_df = teams_df[teams_df["franchID"] == "MIL"]
brewers_df = brewers_df[brewers_df["yearID"] < 2020]
brewers_df = brewers_df[brewers_df["yearID"] > 2010]
print(brewers_df)

observed = []
totalWins = 0
totalYears = 0
for index, row in brewers_df.iterrows():
    observed.append(row["W"])
    totalWins += row["W"]
    totalYears += 1

expected = []
for o in observed:
    expected.append(totalWins/totalYears)
observedExpected = []
oeSquared = []

for o,e in zip(observed, expected):
    observedExpected.append(o-e)

for x in observedExpected:
    oeSquared.append(x * x)

print("Observed = {0}\nExpected = {1}\nO-E = {2}\n(O-E)^2 = {3}".format(observed, expected, observedExpected, oeSquared))

print(stats.chisquare(observed, f_exp=expected))