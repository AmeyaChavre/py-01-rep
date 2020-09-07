def ispangram(str1):
    alphabet_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    target_list = ''.join(str1.split()).lower()
    proc_list = sorted(list(set(target_list)))
    alphabet_string = ''.join(alphabet_list)
    proc_string = ''.join(proc_list)
    if proc_string == alphabet_string:
        print('True')
    else:
        print('False')
ispangram("The quick brown fox jumps over the lazy dog")
    

