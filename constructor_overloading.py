class Person:
    def __init__(self, name, age=None):
        self.name = name
        if age is not None:
            self.age = age

    def introduce(self):
        if hasattr(self, 'age'):            
            print(f"I am {self.name} and my age is {self.age}")
        else:
            print(f"I am {self.name}")

person1 = Person("A")
person2 = Person("B", 25)

person1.introduce()
person2.introduce()
