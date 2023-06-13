#
# with open("weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)


import  csv



# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures =[]
#     for item in data:
#         if item[1] == "temp":
#             pass
#
#         else:
#
#             tempratures.append(int((item[1])))
#
#
# print (tempratures)



import pandas

data = pandas.read_csv("weather_data.csv")
print(data["condition"])