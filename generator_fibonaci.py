def generate_fibonacci(num):
    first_num=1
    second_num=1
    for i in range(num):
        yield first_num
        first_num,second_num = second_num,first_num+second_num

for x in generate_fibonacci(10):
    print(x)