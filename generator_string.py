def generator_string():
    some_string = 'hello'
    for letter in some_string:
        yield letter
        
g = generator_string()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))