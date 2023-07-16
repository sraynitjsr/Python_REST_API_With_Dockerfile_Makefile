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

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

print(dog.name)
print(cat.name)
