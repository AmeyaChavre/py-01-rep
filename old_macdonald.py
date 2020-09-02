def old_macdonald(name):
    target_name=''
    for letter in range(0,len(name)):
        if letter==0 or letter==3:
            target_name+=name[letter].upper()
        else:
            target_name+=name[letter]
    #print(target_name)
    return(target_name)
old_macdonald('macdonald')
        

