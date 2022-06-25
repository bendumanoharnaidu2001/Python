#Simple programm to calculate age

print ("Answer the questions to know how long you have lived")
name = input('Name:')
print("what's your age",(name))
age = int(input('age:'))

#int means integer such as 1,2,3 or -1,-2,-3
days = age*365
hours = days*24
minutes = age*525948
seconds = age*31556926

print(name,'has been alive for',days,'days',hours,'hours',minutes,'minutes',seconds,'seconds')
print('Thanks for using my age calc program!')