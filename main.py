class Student:
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll

	def show(self):
            print('New Student Name is =>', self.name, 'and Roll No. is =>', self.roll)

student = Student("Subhradeep", 100)
student.show()
