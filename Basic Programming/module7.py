

'''
#eg 6:

c = int(input())

f = c*(9/5)+32

k = 273+c

print(f"Temperature in Fahrenheit:{f}F\nTemperature in kelvin:{k}K")



#eg 5:

year = int(input())

leap = 0
if year%100==0 and year%400!=0:
    leap = False
elif year%4==0:
    leap = True

else:
    leap = False

print(leap)
 

#eg 4 :

x = input()

a,b,c = x.split(",")

num1 = int(a)
num2 = int(b)
num3 = int(c)

if num1>num2:
    if num1>num3:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num3} ")

elif num2>num3:
    if num2>num1:
        print(f"The largest number is {num2} ")

    else:
        print(f"The largest number is {num1} ")

elif num3>num1:
    if num3>num2:
        print(f"The largest number is {num3} ")
    else:
        print(f"The largest number is {num2} ")
else:
    print("Given numbers are equal.")



#eg 3 pallindrome:

s = input("Give string :")

revese = s[::-1]

if revese == s:
    print("It\"s a pallindrome.")

else :
    print("It\"s not a pallindrome.")



#eg 2:

a = int(input())
b = int(input())
c = int(input())

total = a+b+c
average = total/3
percentage = (total/300)*100
grade = 0
if percentage>90:
    grade = "A+"
elif percentage>80 and percentage<=90:
    grade = "A"
elif percentage>70 and percentage<=80:
    grade = "B"
elif percentage>60:
    grade = "C"
else :
    grade = "pass"

print(f"Total = {total}\n Average = {average}\n Grade = {grade}")

    
#eg 1:

s = input()
s = s.lower()
a = s.count("a")
e = s.count("e")
i = s.count("i")
o = s.count("o")
u = s.count("u")

print(f"Vowels are :{a+e+i+o+u}")

'''