import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change the working directory to where your full_data.csv file is stored
os.chdir("/Users/jiayifan/IBI1_2020-21/Practical7")

### The code for importing the .csv file works
covid_data = pd.read_csv("full_data.csv")

### There is correct code for showing all columns, and every second row between (and including) 0 and 10
covid_data.iloc[0:12:2,:]

### You have successfully used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
covid_data.loc[covid_data['location']=="Afghanistan","total_cases"]
covid_data.loc[covid_data.loc[:,"location"] == "Afghanistan", "total_cases"]

### You have correctly computed the mean and median of new cases for the entire world.
# world_new_cases to store only the data on new cases for the entire world
world_new_cases = covid_data.loc[covid_data.loc[:,"location"] == "World", ["date","new_cases"]]
np.mean(world_new_cases)
np.median(covid_data.loc[covid_data.loc[:,"location"] == "World", "new_cases"])

### You have successfully created a boxplot of new cases worldwide.
boxprops = dict(color  = 'teal',facecolor = 'paleturquoise', linewidth=2.0)
medianprops = dict(linestyle='-.', linewidth=2.0, color='teal')
capprops = dict(color = 'teal', linewidth=2.0)
whiskerprops = dict(color = 'teal', linewidth=2.0)
labels = [' ']
#plot
fig, ax = plt.subplots()
ax.boxplot(covid_data.loc[covid_data.loc[:,"location"] == "World", "new_cases"],
    patch_artist=True,
    boxprops = boxprops,
    medianprops = medianprops,
    capprops = capprops,
    whiskerprops = whiskerprops,
    labels = labels)
ax.set_title('World New Cases',fontsize=20)
# names for axes
for ax in [ax]:
    ax.set_ylabel('case distribution')

# horizontal grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

plt.show()

### You have successfully plotted both new cases and new deaths worldwide.
# new cases
world_dates = covid_data.loc[covid_data.loc[:,"location"] == "World", "date"]
world_cases = covid_data.loc[covid_data.loc[:,"location"] == "World", "new_cases"]
plt.figure(figsize=(6,5))
plt.plot(world_dates, world_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.tick_params(labelsize = 8)
plt.title("New Cases")
plt.xlabel("date")
plt.ylabel("number")
plt.show()
# new deaths
world_deaths = covid_data.loc[covid_data.loc[:,"location"] == "World", "new_deaths"]
plt.figure(figsize=(6,5))
plt.plot(world_dates, world_deaths, 'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.tick_params(labelsize = 8)
plt.title("New Deaths")
plt.xlabel("date")
plt.ylabel("number")
plt.show()

### There is code to answer the question stated in file question.txt
### The code to answer the question runs without errors
### The code to answer the question does what it is meant to do
### All plots are clearly labelled
# How have new cases and total cases developed over time in Spain?
spain_new_cases = covid_data.loc[covid_data.loc[:,"location"] == "Spain", "new_cases"]
spain_total_cases = covid_data.loc[covid_data.loc[:,"location"] == "Spain", "total_cases"]
plt.plot(world_dates, spain_new_cases, 'r+')
plt.plot(world_dates, spain_total_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.tick_params(labelsize = 8)
plt.title("Spain")
plt.xlabel("date")
plt.ylabel("number")
plt.show()
