def blackjack(a,b,c):
    sum_of_numbers = a + b + c
    if sum_of_numbers<=21:
        #print(sum_of_numbers)
        return sum_of_numbers
    elif sum_of_numbers>21:
        if a==11 or b==11 or c==11:
            reduce_by_10 = sum_of_numbers-10
            if reduce_by_10 > 21:
                #print('BUST')
                return 'BUST'
            else:
                #print(reduce_by_10)
                return reduce_by_10
        elif a!=11 or b!=11 or c!=11:
            if sum_of_numbers>21:
                #print('BUST')
                return 'BUST'
blackjack(9,9,11)
