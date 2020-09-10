class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an Animal")
    
    def eat(self):
        print("I am eating")
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    #over-riding who_am_i
        
    def who_am_i(self):
        print("I am a Dog")

class Cat(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")
    
    def who_am_i(self):
        print("I am a Cat")

animal_obj = Animal()
animal_obj.who_am_i()
animal_obj.eat()

dog_obj = Dog()
dog_obj.who_am_i()

cat_obj = Cat()
cat_obj.who_am_i()

