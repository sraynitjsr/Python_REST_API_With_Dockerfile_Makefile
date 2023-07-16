print("Learning Python From Scratch")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"My name is {self.name} & I am {self.age} years old.")

person1 = Person("Ray", 30)
person2 = Person("Joy", 25)

person1.display()
person2.display()
