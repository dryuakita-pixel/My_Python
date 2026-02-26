# using the ".value" method.
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
#cities.clear()

value = cities.values()
for value in cities.values():
    print(value)
