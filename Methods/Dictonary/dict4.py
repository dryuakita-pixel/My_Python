# This is how to remove one of the dict by using the ".pop" method.
cities = {
    "Japan": "Tokyo",
    "China": "Hong kong",
    "Rusia": "Moscow",
    "America": "Los angelos"
}

#print(dir(cities)) # you can use this method.
#print(help(cities)) # you can use this method.

#cities.update({"Chine": "Beijing"})
cities.pop("Rusia")

print(cities)
