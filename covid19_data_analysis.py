# -*- coding: utf-8 -*-
"""
Covid 19 Data Analysis using Pandas

Covid 19 Dataset: 
"""
import pandas as pd
import datetime as dt
import matplotlib
from matplotlib import pyplot as plt

# dates     location     new_cases    new_deaths    total_cases    total_deaths
covid_data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")


covid_data['date'] = [dt.datetime.strptime(X, '%Y-%m-%d') for X in  covid_data['date']]
#print(covid_data.dtypes) # displays the data types

# looking at subset if countries
countries = ['United States', 'India', 'Italy']

# creating a subset of data frame
covid_data_country = covid_data[covid_data.location.isin(countries)]

# making the date as an index
covid_data_country.set_index('date', inplace = True)
#print(covid_data_country.head()) # shows the top 5 results

# view data plot between specific dates
covid_data_country = covid_data_country.loc['2020-03-01': '2020-08-13']

# adding a mortality rate column
covid_data_country['mortality_rate'] = covid_data_country['total_deaths']/covid_data_country['total_cases']
# print(covid_data_country.tail())

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14,14))

covid_data_country.groupby('location')['new_cases'].plot(ax=axes[0,0], legend = True)
covid_data_country.groupby('location')['new_deaths'].plot(ax=axes[0,1], legend = True)
covid_data_country.groupby('location')['total_cases'].plot(ax=axes[1,0], legend = True)
covid_data_country.groupby('location')['total_deaths'].plot(ax=axes[1,1], legend = True)

axes[0,0].set_title('New Cases')
axes[0,1].set_title('New Deaths')
axes[1,0].set_title('Total Cases')
axes[1,1].set_title('Total Deaths')

fig.tight_layout()  # adjusting the subplot parameters to give specified padding.
