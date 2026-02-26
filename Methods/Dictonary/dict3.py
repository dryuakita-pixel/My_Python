# This is how to update the dict by using the ".update" method.
cities = {
    "Japan": "Tokyo",
    "China": "Hong kong",
    "Rusia": "Moscow",
    "America": "Los angelos"
}

#print(dir(cities)) # you can use this method.
#print(help(cities)) # you can use this method.

cities.update({"Chine": "Beijing"})

print(cities)
