def animal_crackers(text):
    target_list=text.split(' ')
    if(len(target_list)==2):
        for word in target_list:
            if target_list[0][0].lower() == target_list[1][0].lower():
                print('True')
                break
            else:
                print('False')
                break
    else:
        print('Enter a 2 word string only with a single white space separating the two words and only a single whitespace is allowed in entire string!!')
animal_crackers('Levelheaded llama')
