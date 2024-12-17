
print("add")
print("sub")
print("multi")
print("div")

a=input("enter your choice:")

print(a)
list=["add","sub","multi","div"]
if a  in  list:
    n1=int(input("enter the 1 number"))
    n2=int(input("enter the 2 number"))
    if a=="add":
        print(f"The addition of {n1} and {n2} is {n1+n2}")
    elif a=="sub":
        print(f"The subtraction of {n1} and {n2} is {n1-n2}")
    elif a=="multi":
        print(f"the multiplication of {n1} and {n2} is {n1*n2}")
    elif a=="div":
        if n2==0:
           print("give a number except zero")
           n2=int(input("enter the 2 number"))
        else:
            print(f"the division of {n1} and {n2} is {n1/n2}")

else:
    print("please choose a correct choice given to you")