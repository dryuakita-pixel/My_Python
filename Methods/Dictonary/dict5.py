# This is how to remove the latest dict by using the ".popitem" method.
cities = {
    "Japan": "Tokyo",
    "China": "Hong kong",
    "Rusia": "Moscow",
    "America": "Los angelos"
}

#print(dir(cities)) # you can use this method.
#print(help(cities)) # you can use this method.

#cities.update({"Chine": "Beijing"})
#cities.pop("Rusia")
cities.popitem()

print(cities)
