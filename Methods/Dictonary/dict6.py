# This is how to fully remove all the dictionary by using the ".clear" method.
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
#cities.popitem()
cities.clear()

print(cities)
