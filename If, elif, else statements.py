print("This program checks if you are eligible for a bank lone or not")

salary = int(input("How much is your salary\n"))

if (salary>1000):
	amount=200
	print("You are eligible to get a bank loan by paying $",amount,"monthly")
elif(salary==1000):
	amount=500
	print("You are eligible to get a bank lone by paying $",amount,"monthly")
else:
	print("You are not eligible")