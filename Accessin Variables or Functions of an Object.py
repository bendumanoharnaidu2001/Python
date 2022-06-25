class Person():

	def __init__(self,name,age,idNum):
		self.name=name
		self.age=age
		self.idNum=idNum
	def output(self):
		print("Your name is "+self.name+" your age is "+self.age+" your idNum is "+ self.idNum)

j=Person("John","22","E18ECE011")

print(j.name)
print(j.age)
print(j.idNum)
j.output()