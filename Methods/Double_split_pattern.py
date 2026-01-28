line = "From Nathan Nathanjones@gmail.com sat first"
words = line.split()
email = words[2]
pieces = email.split('@')
domain = pieces[1]
print(domain)
