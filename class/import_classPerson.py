import classPerson

name = "chonthicha sitnoi"
age = 21
address = "London"

person = classPerson.Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info()