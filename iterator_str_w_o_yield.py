some_string = 'Hello'
g = iter(some_string)
for i in range(len(some_string)):
    print(next(g))
