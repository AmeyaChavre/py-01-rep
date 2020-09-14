def my_func():
    print("my_func() in one.py")
    
if __name__ == '__main__':
    print("one.py is executed directly")
else:
    print("one.py was imported from two.py")