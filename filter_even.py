def check_even(num):
    return num%2 == 0    # True or False
iterator_list = [1,2,3,4,5,6,7,8,9]

print("Even List: ", list(filter(check_even,iterator_list)))
