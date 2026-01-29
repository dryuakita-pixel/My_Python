import re
a = "You just got $100.000 today"
found = re.findall(r"\$\d+\.\d+", a)
print(found)
