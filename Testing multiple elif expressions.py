print("This programm checks the ZOO discounts\n")
print("and enterance price is $120")

price = 120
times=int(input("How many times did you visit the ZOO before:"))

if(times==3):
	price=120-30
	print("Your total included discount will be $",price)

elif(times==4):
	price=120-50
	print("Your total included discount will be $", price)

elif(times==5):
	print=120-70
	print("Your total included discount will be $", price)

else:
	print("Your total price is $",price,"and you are not eligble for discount in this time")
