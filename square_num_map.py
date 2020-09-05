def square_num(num):
    return num*num

list_of_numbers = [1,2,3,4,5,6,7,8,9]
for item in map(square_num,list_of_numbers):
    print(item)
