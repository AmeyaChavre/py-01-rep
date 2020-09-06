def up_low(s):
    print('Original String: ', s)
    target_list = s.split()
    target_string = ''.join(target_list)
    lower_case_count = 0
    upper_case_count = 0
    for i in target_string:
        if i.islower():
            lower_case_count+=1
        elif i.isupper():
            upper_case_count+=1
        else:
            continue
    print('No. of Upper case characters : ',upper_case_count)
    print('No. of Lower case characters : ',lower_case_count)
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
