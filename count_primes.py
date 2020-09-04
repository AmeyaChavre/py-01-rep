def count_primes(num):
    list_of_primes=[]
    for i in range(2,num+1):
        if i not in list_of_primes:
            print(i)
            for j in range(i*i,num+1,i):
                list_of_primes.append(j)
count_primes(100)
        
