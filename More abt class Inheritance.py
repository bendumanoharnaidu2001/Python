class Person():

	def __init__(self,name,age,idNum):
		self.name=name
		self.age=age
		self.idNum=idNum
	def output(self):
		print("Your name is "+self.name+" your age is "+self.age+" your idNum is "+ self.idNum)

class Man():
	def strong(self):
		print("Men are strong")


class Child(Person,Man):
	pass

kid= Child("Joe","5","efasdaw")
kid.output()

kid.strong()