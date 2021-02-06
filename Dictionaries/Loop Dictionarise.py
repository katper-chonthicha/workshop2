thisdict = {"brand": "Ford","model":"Mustang","year": 1964}

# EX1
for key in thisdict:
    print(key)

# EX2
thisdict = {"brand": "Ford","model":"Mustang","year": 1964}
for key in thisdict:
    print(thisdict[key])

# EX3
thisdict = {"brand": "Ford","model":"Mustang","year": 1964}
for key in thisdict.keys():
    print(key)

# EX4
thisdict = {"brand": "Ford","model":"Mustang","year": 1964}
for value in thisdict.values():
    print(value)

# EX5
thisdict = {"brand": "Ford","model":"Mustang","year": 1964}
for key,value in thisdict.items():
    print(key,value)