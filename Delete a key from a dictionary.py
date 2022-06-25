OS={"Apple":"Mac","Microsoft":"Windows","At&t":"PC"}

#To edit that

print("Before"+ OS["At&t"])
OS["At&t"]="Linux"

print("NOw is"+ OS["At&t"])
print(OS)

del OS["At&t"]
print("After printing:")
print(OS)