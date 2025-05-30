


'''
#eg 3:

num1 = int(input("give value: "))
num2 = int(input("give value: "))
operator = input("give operator: ")

if operator=="+":
    print(f"addition of two numbers is{num1+num2}")
elif operator=="-":
    print(f"subraction of two numbers is {num1-num2}")
elif operator=="*":
    print(f"multiplication of two numbers is {num1*num2}")
elif operator=="/":
    print(f"division of two numbers is {num1/num2}")


else:
    print("invalid operator")


#eg 2:

w = input()
t = input()

if w=="b":
    if t == "n":
        print("yes")
    else : 
        print("no")

elif w=="r":
    print("a")

elif w=="s":
    if t == "n":
        print("b")
    else:
        print("c")

else:
    print("d")


#eg 1:

weather = input("enter weather:")
time_of_day = input("enter time of day:")

if weather == "sunny":
    print("you can play with your car toy.")

elif weather == "rainy":
    print("you can play with your boat toy.")

elif weather == "snowy" and time_of_day == "night":
    print("you can plaay with your teddy bear toy")

else:
    print("you can play with your snowman toy")
print("stay warn and have a good time")

'''