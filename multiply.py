def multiply(numbers):
    product = numbers[0]
    for i in range(0,len(numbers)-1):
        product*=numbers[i+1]
    print(product)
multiply([1,2,3,-4])
