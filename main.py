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

class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

child_obj = Child()
child_obj.parent_method()
child_obj.child_method()

class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Child method")

child_obj = Child()
child_obj.method1()
child_obj.method2()
child_obj.child_method()

class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

child_obj = Child()
child_obj.grandparent_method()
child_obj.parent_method()
child_obj.child_method()
