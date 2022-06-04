# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)
#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)


# temperature_list = data['temp'].to_list()
# result = sum(temperature_list) / len(temperature_list)
# print(result)

# print(data['temp'].max())

# monday = (data[data.temp == data['temp'].max()])
# mon_temp = int(monday.temp)
# mon_temp = mon_temp*1.8+32
# print(mon_temp)

import pandas

data = pandas.read_csv('central_park.csv')
gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrel_count = {
    "Fur_colour": ['Gray', 'Black', 'Cinnamon'],
    "Squirrel_count": [gray_squirrels, black_squirrels, cinnamon_squirrels]
}

final = pandas.DataFrame(squirrel_count)
final.to_csv('count.csv')