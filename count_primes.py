def count_primes(num):
    list_of_primes=[]
    target_list=[]
    for i in range(2,num+1):
        if i not in list_of_primes:
            target_list.append(i)
            for j in range(i*i,num+1,i):
                list_of_primes.append(j)
    #print(target_list)
    return len(target_list)
count_primes(100)
        
