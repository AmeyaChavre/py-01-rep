def lesser_of_two_evens(a,b):
    if a < b:
        if a%2==0 and b%2==0:
            print(a)
        elif a%2!=0 and b%2!=0:
            print(b)
        elif a%2!=0 and b%2==0:
            print(b)
        elif a%2==0 and b%2!=0:
            print(b)
    elif a > b:
        if a%2==0 and b%2==0:
            print(b)
        elif a%2!=0 and b%2!=0:
            print(a)
        elif a%2!=0 and b%2==0:
            print(a)
        elif a%2==0 and b%2!=0:
            print(a)
    elif a == b:
        print(a)
lesser_of_two_evens(400,200)
        
            
            
        
        
    
        

        
        

