def palindrome(s):
    if ' ' in s:
        s=s.replace(' ','')
        if s == s[::-1]:
            print('True')
        else:
            print('False')
    else:
        if s == s[::-1]:
            print('True')
        else:
            print('False')
palindrome('helleh')
