print(f"Hexadecimal 1024 : {hex(1024)} \nBinary 1024 : {bin(1024)}")

num=5.23922 
print(f"{num} rounded to 2 places : {round(num,2)}")

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1.intersection(set2))

myDict = {x: x**3 for x in [0,1,2,3,4]} 
print (myDict)

list1 = [1,2,3,4]
print(list1[::-1])

list2 = [3,4,2,5,1]
print(sorted(list2))
