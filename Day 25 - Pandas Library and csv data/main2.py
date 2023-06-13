import pandas





data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")




grey_count = print(len(data[data["Primary Fur Color"] == "Gray"]))
cinnamon_count = print(len(data[data["Primary Fur Color"] == "Cinnamon"]))
black_count = print(len(data[data["Primary Fur Color"] == "Black"]))


data_dict = {
    "Fur Color" : ["Gray" , "Cinnamon", "Black" ],
    "Count" : [grey_count , cinnamon_count, black_count]
}



df = (pandas.DataFrame(data_dict))
df.to_csv("output.csv")