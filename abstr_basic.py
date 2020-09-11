class Animal():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this Abstract class")

class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof"
    
class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow"
    
fido = Dog('fido')
isis = Cat('isis')

print(fido.speak())
print(isis.speak())
