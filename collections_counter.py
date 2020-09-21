from collections import Counter

#Usecases

my_list = [1,2,5,6,7,3,5,9,0,2,4,6,7,8,4,5,6,8,9,8,7,6,3,6,2]

print(Counter(my_list))

my_string = 'ThisisaSampleString'

print(Counter(my_string.lower()))

my_sentence = 'This is a sample string with no sub string'

print(Counter(my_sentence.lower().split()))

some_string = 'aaaaabbbbbbbccccccccccdddddddddddddddeeeeeeeeeeeeeeeee'
print("Most Common in some_string : ", Counter(some_string).most_common())
print("Highest Frequency Letter in some_string : ", Counter(some_string).most_common(1))



