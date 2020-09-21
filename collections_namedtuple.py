from collections import namedtuple

Dog = namedtuple('Dog',['age','name','breed'])

oliver = Dog(age=5,name='Oliver',breed='Beagle')

print(f"Meet {oliver.name} the dog , he's a {oliver.age} year old {oliver.breed}.")
print(f"Meet {oliver[1]} the dog , he's a {oliver[0]} year old {oliver[2]}.")
