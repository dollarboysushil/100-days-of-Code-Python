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
# print(data["condition"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# sum = 0
# count = 0
# for i in temp_list :
#     sum = sum + i
#     count += 1
# print(count)
# print(sum/count)


print(data["temp"].max())


mon_data = (data[data.temp == 12])
print(mon_data.temp)