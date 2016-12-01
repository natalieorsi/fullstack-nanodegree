class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print "Last name -",self.last_name
		print "Eye color -",self.eye_color

teruzane = Parent("Utada","nebula")
print teruzane.last_name

class Child(Parent):
	def __init__(self,last_name,eye_color,num_toys):
		print("Child constructor called")
		Parent.__init__(self,last_name,eye_color)
		self.num_toys = num_toys

	def show_info(self):
		print "Last name -",self.last_name
		print "Eye color -",self.eye_color
		print "Number of toys -",self.num_toys

hikaru = Child("Utada","radiant",9999999)
hikaru.show_info()