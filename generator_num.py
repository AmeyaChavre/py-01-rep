def generator_num():
    for i in range(3):
        yield i

g = generator_num()

print(next(g))
print(next(g))
print(next(g))