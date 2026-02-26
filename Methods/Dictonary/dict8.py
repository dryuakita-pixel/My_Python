# using the "keys" method.
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

key = cities.keys()

for key in cities.keys():
    print(key)
