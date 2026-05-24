size=input("What size pizza you want (S/M/L)?")
bill=0
if size=='s' or size=='S':
    bill+=100
    print("Small size price Rs.100")
elif size=='m' or size=='M':
    bill+=200
    print("Medium pizza price Rs.200")
else:
    bill+=300
    print("Large pizza price Rs.300")

add_pepper=input("Do you want to add_pepper (Y/N)?")
if add_pepper =='Y'  or add_pepper=="y":
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50


extra_cheese=input("Do you want extra_cheese (Y/N)?")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20

print(f"Your final bill is {bill}")


