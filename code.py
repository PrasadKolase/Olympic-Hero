# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace=True)

print(data.head(10))

#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',
                    (np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter')))

print(data.head())

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
# print(top_countries.tail(1))

top_countries.drop(top_countries.index.values[-1], axis=0, inplace=True)
# print(top_countries.tail(1))
print(top_countries.head())

def top_ten(df,column_name):
    country_list = []
    country_list = df.nlargest(10,column_name)
    return list(country_list['Country_Name'])

top_10_summer = top_ten(top_countries,'Total_Summer')
print(top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10)

common = list(set(top_10_summer).intersection(set(top_10_winter).intersection(set(top_10))))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
print(summer_df.head())
winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

plt.plot(kind='bar', x=summer_df['Country_Name'], y=summer_df['Total_Summer'])

plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')

plt.show()



# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
print(summer_max_ratio)
summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio].values[0]
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
print(winter_max_ratio)
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio].values[0]
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
print(top_max_ratio)
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio].values[0]
print(top_country_gold)


# --------------
#Code starts here

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

most_points = max(data_1['Total_Points'])

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(best_country,"is best country with",most_points,"points")


# --------------
#Code starts here

best = data[data['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)

plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation=45)



