"""
Using "Spyder IDE"
Created on Thu Aug 13 16:41:34 2020

ANALYZING COVID-19 DATASET IN PYTHON 
- using Pandas for data handling and Seaborn for plotting

@author: aditiabhang
"""

import pandas as pd
import datetime as dt
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

# dates     location     new_cases    new_deaths    total_cases    total_deaths
col_list = ['date', 'location', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths']
covid_data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")
print("\n----------Top 5 results----------")
print(covid_data.head())

# date format : %Y-%m-%d
# converting string values of date into datetime format
covid_data['date'] = [dt.datetime.strptime(X, '%Y-%m-%d') for X in  covid_data['date']]
print("\n----------Data types----------")
print(covid_data.dtypes) # displays the data types)

# checking for any missing data
# print("\n----------Missing data----------")
#print(covid_data.isnull().sum())

# Changing column titles
#covid_data.columns = ['Date', 'Country', 'New Cases', 'New Deaths', 'Total Cases', 'Total Deaths']
#print("\n----------Top 5 results with new titles----------")
#print(covid_data.head())

# Seting all countries except for China and World, to avoid scewing the results
covid_data_no_china = covid_data.loc[~(covid_data['location'].isin(["China", "World"]))]
print("\n----------Top 5 results (without China)----------")
print(covid_data.head())

# Group them by location and date, select only total cases and deaths for closer observation
# Reset index because groupby by default makes grouped columns indices
covid_data_no_china = pd.DataFrame(covid_data_no_china.groupby(['date', 'location'])['total_cases', 'total_deaths'].sum()).reset_index()
print("\n----------Top 5 results (grouped without China)----------")
print(covid_data_no_china)

# Sorting the results by Counrty and Date
covid_data_no_china = covid_data_no_china.sort_values(['date', 'location'], ascending = False)
print("\n----------Sorted Results----------")
print(covid_data_no_china)

#---------------------------------------------------#
#---------------Plotting begins here----------------#
#---------------------------------------------------#

def plot_bar(feature, value, title, df, size):
    f, ax = plt.subplots(1,1, figsize=(4*size,4))
    df = df.sort_values([value], ascending = False).reset_index(drop = True)
    g = sns.barplot(df[feature][0:10], df[value][0:10], palette='Set3')
    g.set_title("Number of {} - highest 10 values".format(title))
    plt.show()
    
filtered_cvd_no_china = covid_data_no_china.drop_duplicates(subset = ['location'], keep = 'first')
plot_bar('location', 'total_cases', 'Total cases in the world (except China)', filtered_cvd_no_china, size=4)
plot_bar('location', 'total_deaths', 'Total deaths in the world (except China)', filtered_cvd_no_china, size=4)

#---------------------------------------------------#

def plot_world_aggregate(df, title='Aggregate Plot', size=1):
    f, ax = f, ax = plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x ='date', y = 'total_cases', data = df, color = 'blue', label = 'Total Cases')
    g = sns.lineplot(x ='date', y = 'total_deaths', data = df, color = 'red', label = 'Total Deaths')
    plt.xlabel('date')
    plt.ylabel(f'Total {title} cases')
    plt.xticks(rotation = 90)
    plt.title(f'Total {title} cases')
    ax.grid(color = 'black', linestyle = 'dotted', linewidth = 0.75)
    plt.show()
    
covid_no_china_aggregate = covid_data_no_china.groupby(['date']).sum().reset_index()
print("\n----------Aggregate World Data----------")
print(covid_no_china_aggregate)

plot_world_aggregate(covid_no_china_aggregate, 'Rest of the World', size = 4)

#---------------------------------------------------#

def plot_aggregate_countries()




