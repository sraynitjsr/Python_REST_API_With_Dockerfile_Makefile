class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

def start():
    print('Inside Classes in Python')
    p1 = Person("Sachin", 10)
    print(p1.name)
    print(p1.age)
