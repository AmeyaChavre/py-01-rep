def run_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    
a = run_in(True,False)
print(f"{hex(a)}{bin(a)}")