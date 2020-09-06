def ran_check(num,low,high):
    if low <= num <= high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not between {low} and {high}')
ran_check(5,2,7)
