def ask():
    
    while True:
        try:
            accept_value = int(input("Please enter a number:"))
            print(f"You have entered {accept_value} the square is : {accept_value**2}")
        except:
            print('Aw snapp !! Here we go again!')
            continue
        else:
            print('All you had to do was to follow the instructions CJ')
            break
        finally:
            print('Yeah I got you ninja style')
ask()
