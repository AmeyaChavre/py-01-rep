def spy_game(nums):
    list1 = []
    for i in nums:
        if i == 0 or i == 7:
            list1.append(i)
    str1=''
    for i in list1:
        str1+=str(i)
    if '007' in str1:
        print('True')
        return True
    else:
        print('False')
        return False
spy_game([1,7,2,4,5,0,1,7])

