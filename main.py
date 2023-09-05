# Define a simple class called "Person"
class Person:
    # Constructor method to initialize the object with a name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information about the person
    def display_info(self):
        print(f"Name=> {self.name}, Age=> {self.age}")

# Define a main function for the script
def main():
    # Create instances of the Person class
    person1 = Person("A", 25)
    person2 = Person("B", 50)

    # Access and display information about the persons
    person1.display_info()
    person2.display_info()

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()
