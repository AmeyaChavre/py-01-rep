def paper_doll(input_string):
    target_string=''
    for letter in input_string:
        target_string+=letter*3
    print(target_string)
    return target_string
paper_doll('Mississippi')
