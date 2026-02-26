# This is how to get the list from the collection by using the ".get".
cities = {
    "Japan": "Tokyo",
    "China": "Hong kong",
    "Rusia": "Moscow",
    "America": "Los angelos"
}

#print(dir(cities)) # you can use this method.
#print(help(cities)) # you can use this method.
print(cities.get("America"))
print(cities.get("India"))
