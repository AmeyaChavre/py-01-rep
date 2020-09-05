target_list = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda num: num **2, target_list)))
print(list(filter(lambda num: num%2 == 0, target_list)))
