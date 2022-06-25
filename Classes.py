class Person():
	def insert(self, name, age,idNum):
		self.name =name
		self.age=age
		self.idNum=idNum
	def output(self):
		print("Your name is: "+self.name+"\nyour age is: "+self.age+"\nyour idNum is: "+self.idNum)

j=Person()
j.insert("Manu","22","E18ECE011")
j.output()