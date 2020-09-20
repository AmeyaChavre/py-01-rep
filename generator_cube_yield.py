def generate_cube(num):
    for i in range(num):
        yield i**3

for x in generate_cube(10):
    print(x)
