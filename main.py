# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import matplotlib.pyplot as plt
import cbsodata

######Uncomment the print lines only for detailed information regarding the raw data!

######identifying relevant Identifier for analysis for renewable energy CBS data online
tables = cbsodata.get_table_list()
df_tables = pd.DataFrame(tables)
#print(df_tables.head())
keyword = df_tables[df_tables['Title'].str.contains("renewable energy", case=False)]  
#print(keyword[['Identifier', 'Title']].head())

#####filtering the renewable energy data
raw_data = pd.DataFrame(cbsodata.get_data('84918ENG')) 
#print(raw_data.columns)
meta = pd.DataFrame(cbsodata.get_meta('84918ENG', 'DataProperties')) ### to obtain units of measurement
#print(meta['Unit'].unique())
#print(raw_data['EnergySourcesTechniques'].unique())
#print(raw_data['Periods'].unique())
#print(raw_data['EnergyApplication'].unique())
#print(raw_data['AvoidedEmissionRelative_4'].unique())
raw_data = raw_data.dropna(subset=['Periods', 'EnergySourcesTechniques', 'EnergyApplication','AvoidedEnergy_1','AvoidedEmission_3']) #remove missing data
sources = ['Total energy sources', 'Wind energy on shore', 'Wind energy off shore', 'Solar photovoltaic', 'Total biomass'] ### data filtering  = removal of too detailed breakdowns & low significance
filtered_data = raw_data[raw_data['EnergySourcesTechniques'].isin(sources)]  
filtered_data = filtered_data[filtered_data['EnergyApplication'] == 'Electricity']
filtered_data = filtered_data[filtered_data['Periods'] >= '2010']  
filtered_data = filtered_data.pivot(index='Periods', columns='EnergySourcesTechniques', values = 'AvoidedEmissionRelative_4')
filtered_data = filtered_data.iloc[:,[0,1,3,4,2]]  #reordering columns
filtered_data.index = filtered_data.index.astype(int)  #converting string to integer

######plotting final data
data_stack = filtered_data.drop(columns=['Total energy sources'])
data_line = filtered_data['Total energy sources']
plt.figure(figsize=(10,6))
plt.stackplot(data_stack.index, data_stack.T, labels=["Solar PV","Biomass","Wind offshore","Wind onshore"],alpha=0.95)
plt.plot(data_line.index, data_line, linewidth=2, linestyle='--', marker='8', color = 'k', label = 'Total')
plt.title('% of National CO2 Emissions Avoided by Renewable Sources \n (Electricity sector, Netherlands 2010-2024)', fontsize = '12', fontweight = "bold")
plt.ylim(0,25)
plt.xlim(2010, 2024)
plt.xticks(range(2010, 2025, 2))  # alternate years
plt.grid(axis="y", color = "k", linestyle='--', linewidth = 0.5)
plt.xlabel("Year", fontsize = 12, color = "k")
plt.ylabel("% of Total National CO2 Emissions Avoided", fontsize = 12, color = "k")
plt.legend(loc='upper left',fontsize = 12)
plt.annotate('Total: 22.2%', xy=(2024, data_line.loc[2024]),xytext=(2021, 22.5), arrowprops=dict(arrowstyle='->'),fontsize = '12', fontweight = "bold")
plt.annotate('Total: 3.9%', xy=(2010, data_line.loc[2010]),xytext=(2010.5, 6), arrowprops=dict(arrowstyle='->'),fontsize = '12', fontweight = "bold")
y_start = data_stack['Solar photovoltaic'].loc[2010]
y_end = data_stack['Solar photovoltaic'].loc[2024]
plt.annotate('',xy=(2023.9, y_start),xytext=(2023.9, y_end),arrowprops=dict(arrowstyle='<->', linewidth=2))
plt.text(2021.8,(y_start + y_end)/2,'Solar PV: 35%\nof total',fontsize=12,weight='bold')
plt.figtext(0.5, 0.01, "Source: CBS Statline | https://opendata.cbs.nl/#/CBS/nl/navigatieScherm/thema | Renewable Energy - Electricity", ha="center", fontsize=6, style='italic')
plt.tight_layout()
plt.savefig("image.png", dpi = 200, bbox_inches = "tight")
