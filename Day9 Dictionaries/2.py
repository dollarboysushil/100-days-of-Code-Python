travel_log = [
    {
        "country" : "France" ,
        "visits" : 12 ,
        "cities" : ["paris", "Lille", "Dijon"]
    },

{
        "country" : "germany",
        "visits" : 5,
        "cities" : ["Berlin" , "Hamburg" , "Stuttgart"]
},
 ]

def add_new_country(country , visits , cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)



add_new_country("russia" , 2 , ["moscow", "saint Petersburg" , "kazan"])
print(travel_log)




















