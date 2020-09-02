def makes_twenty(n1,n2):
    if n1 == n2 == 20:
        print('True')
    elif n1 == 20 or n2 == 20:
        print('True')
    elif n1 + n2 == 20:
        print('True')
    else:
        print('False')
makes_twenty(2,3)
