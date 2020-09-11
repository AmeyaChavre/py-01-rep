class Dog():
    
    def __init__(self,name):
        print("Dog Created")
        self.name=name
        
    def speak(self):
        return self.name + " says Woof"
    
class Cat():
    
    def __init__(self,name):
        print("Cat Created")
        self.name=name
        
    def speak(self):
        return self.name + " says Meow"
        
oliver = Dog('oliver')
garfield = Cat('garfield')

for pet in [oliver,garfield]:
    print(pet.speak())

    
 
