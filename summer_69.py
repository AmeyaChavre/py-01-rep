def summer_69(arr):
    if sum(arr) == 0:
        print(sum(arr))
        return sum(arr)
    elif 6 in arr:
        new_arr = arr[arr.index(6):arr.index(9)+1]
        for i in new_arr:
            arr.remove(i)
        print(sum(arr))
        return sum(arr)
    else:
        print(sum(arr))
        return sum(arr)
summer_69([2, 1, 6, 9, 11])
    

