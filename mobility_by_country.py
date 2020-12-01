#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:26:02 2020

@author: mayuoji
"""
##import lib
import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#import data
df=pd.read_csv('Global_Mobility_Report.csv')

#select data
# select no subcategory data
df1=df[df['sub_region_1'].isnull()] 
# select country
#df2=df1[(df1['country_region']=="United Kingdom")|(df1['country_region']=="France")|(df1['country_region']=="Germany")|(df1['country_region']=="Spain")|(df1['country_region']=="Italy")|(df1['country_region']=="Czechia")|(df1['country_region']=="Poland")|(df1['country_region']=="Hungary")|(df1['country_region']=="Romania")]                                                   
df2=df1[(df1['country_region']=="United Kingdom")|(df1['country_region']=="Ireland")|(df1['country_region']=="United States")|(df1['country_region']=="Japan")|(df1['country_region']=="France")|(df1['country_region']=="Germany")|(df1['country_region']=="Spain")|(df1['country_region']=="Italy")|(df1['country_region']=="Czechia")|(df1['country_region']=="Poland")|(df1['country_region']=="Hungary")|(df1['country_region']=="Romania")]                                                   


df2=df2.interpolate()

#movig avaraged
df2 = df2.set_index('date')
df2.index = pd.to_datetime(df2.index, format='%Y-%m-%d')
office = df2.groupby('country_region')['workplaces_percent_change_from_baseline'].rolling(7).mean().reset_index()
stations=df2.groupby('country_region')['transit_stations_percent_change_from_baseline'].rolling(7).mean().reset_index()
retail_recreation=df2.groupby('country_region')['retail_and_recreation_percent_change_from_baseline'].rolling(7).mean().reset_index()
grocery_and_pharmacy=df2.groupby('country_region')['grocery_and_pharmacy_percent_change_from_baseline'].rolling(7).mean().reset_index()
parks=df2.groupby('country_region')['parks_percent_change_from_baseline'].rolling(7).mean().reset_index()

#graph
office.groupby(['date','country_region']).sum()['workplaces_percent_change_from_baseline'].unstack().plot()
stations.groupby(['date','country_region']).sum()['transit_stations_percent_change_from_baseline'].unstack().plot()
retail_recreation.groupby(['date','country_region']).sum()['retail_and_recreation_percent_change_from_baseline'].unstack().plot()
grocery_and_pharmacy.groupby(['date','country_region']).sum()['grocery_and_pharmacy_percent_change_from_baseline'].unstack().plot()
parks.groupby(['date','country_region']).sum()['parks_percent_change_from_baseline'].unstack().plot()

#export csv
office2=office.groupby(['date','country_region']).sum()['workplaces_percent_change_from_baseline'].unstack()
office2.to_csv('office_country.csv')

retail2=retail_recreation.groupby(['date','country_region']).sum()['retail_and_recreation_percent_change_from_baseline'].unstack()
retail2.to_csv('retail_country.csv')

grocery2=grocery_and_pharmacy.groupby(['date','country_region']).sum()['grocery_and_pharmacy_percent_change_from_baseline'].unstack()
grocery2.to_csv('grocery_country.csv')




