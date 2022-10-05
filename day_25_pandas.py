# import csv
# with open('Day25_weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv('Day25_weather_data.csv')
# # print(data['temp'])
# # temp_list = data['temp'].to_list()
# # average = data['temp'].mean()
# # print(round(average,2))
# # maximum_value = data['temp'].max()
# # print(maximum_value)
# # print(data.temp.max())
# # print(data[data.temp == data.temp.max()])
# monday = (data[data.day == 'Monday'])
# monday_fahrenheit = (monday.temp * 1.8) + 32
# print(round(monday_fahrenheit, 2))

data = pandas.read_csv('day_25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey = (data['Primary Fur Color'].value_counts()['Gray'])
red = (data['Primary Fur Color'].value_counts()['Cinnamon'])
black = (data['Primary Fur Color'].value_counts()['Black'])

data_dict = {f'Fur Color': ['grey', 'red', 'black'],
             'count': [grey, red, black]
             }
data_count = pandas.DataFrame(data_dict)
data_count.to_csv('squirrel_count.csv')
