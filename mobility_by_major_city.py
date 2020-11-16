#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:12:12 2020

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

#select city
#london(city)
df1 = df[(df['sub_region_1']=="Greater London")&(df['sub_region_2']=="City of London")]
df1['City']="London(city)"

#newyork
df2 = df[(df['sub_region_1']=="New York")&(df['sub_region_2']=="New York County")]
df2['City']="New York(NYC)"

#paris
df3 = df[df['iso_3166_2_code']=="FR-IDF"]
df3['City']="Paris"

#frunk
df4 = df[df['sub_region_1']=="Hessen"]
df4['City']="Frunkfrut"

#tokyo
df5 = df[df['sub_region_1']=="Tokyo"]
df5['City']="Tokyo"

#prague
df6 = df[df['sub_region_1']=="Prague"]
df6['City']="Praha"

#warsaw
df7 = df[(df['sub_region_1']=="Masovian Voivodeship")&(df['sub_region_2']=="Warszawa")]
df7['City']="Warsawa"

#budapest
df8 = df[df['sub_region_1']=="Budapest"]
df8['City']="Budapest"

#bucharest
df9 = df[df['sub_region_1']=="Bucharest"]
df9['City']="Bucharest"

#roma
df10 = df[(df['sub_region_1']=="Lazio")&(df['sub_region_2']=="Metropolitan City of Rome")]
df10['City']="Roma"

#madrid
df11 = df[df['sub_region_1']=="Community of Madrid"]
df11['City']="Madrid"

#dublin
df12 = df[df['sub_region_1']=="County Dublin"]
df12['City']="Dublin"


#merge
#inc CEE
#major
dff=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12])
dff=dff.iloc[:,7:15]
dff=dff.interpolate()

#moving average
dff = dff.set_index('date')
dff.index = pd.to_datetime(dff.index, format='%Y-%m-%d')
office = dff.groupby('City')['workplaces_percent_change_from_baseline'].rolling(7).mean().reset_index()
stations=dff.groupby('City')['transit_stations_percent_change_from_baseline'].rolling(7).mean().reset_index()
retail_recreation=dff.groupby('City')['retail_and_recreation_percent_change_from_baseline'].rolling(7).mean().reset_index()
grocery_and_pharmacy=dff.groupby('City')['grocery_and_pharmacy_percent_change_from_baseline'].rolling(7).mean().reset_index()
parks=dff.groupby('City')['parks_percent_change_from_baseline'].rolling(7).mean().reset_index()


#plot
office.groupby(['date','City']).sum()['workplaces_percent_change_from_baseline'].unstack().plot()
stations.groupby(['date','City']).sum()['transit_stations_percent_change_from_baseline'].unstack().plot()
retail_recreation.groupby(['date','City']).sum()['retail_and_recreation_percent_change_from_baseline'].unstack().plot()
grocery_and_pharmacy.groupby(['date','City']).sum()['grocery_and_pharmacy_percent_change_from_baseline'].unstack().plot()
parks.groupby(['date','City']).sum()['parks_percent_change_from_baseline'].unstack().plot()

#export csv
office2=office.groupby(['date','City']).sum()['workplaces_percent_change_from_baseline'].unstack()
office2.to_csv('office_city.csv')

retail2=retail_recreation.groupby(['date','City']).sum()['retail_and_recreation_percent_change_from_baseline'].unstack()
retail2.to_csv('retail_city.csv')

grocery2=grocery_and_pharmacy.groupby(['date','City']).sum()['grocery_and_pharmacy_percent_change_from_baseline'].unstack()
grocery2.to_csv('grocery_city.csv')




