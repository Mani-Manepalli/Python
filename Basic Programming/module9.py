

#eg 5:

def celesius(a):
    f = celesius*(9/5)+32
    k = 273+celesius
    print(f"Tempareture in Fahrenheit:{f}\nTemperature in Kelvin:{k}")

a = (30)
celesius(a)



'''
#eg 4:

def swap(a,b):
    b = a+b
    a = b-a
    b = b-a

    print(f"Value of A:{a}\nValue of B:{b}")

a = int(input())
b = int(input())
swap(a,b)



#eg 3:


def roots(a,b,c):
    root1 = 0
    root2 = 0
    d = (b**2-4*a*c)
    root1 = (-b + (d**(0.5)))/2*a
    root2 = (-b - (d**(0.5)))/2*a
    print(f"Roots:{root1},{root2}")

a = int(input("enter a value:"))
b = int(input("enter b value:"))
c = int(input("enter c value:"))

x = roots(a,b,c)
print(x)



#eg 2:

def area(r):
    b = 3.14*r**2
    return(b)
c = area(5)

print(c)


# eg 2:

radius = int(input("Give radius value:"))


def area(c):
    print(f"Area of Circle:{c}")

area(3.14*radius**2)



#eg 1:

a = int(input("Give A value:"))
b = int(input("Give B value:"))

def sum(a,b):
    print(a+b)

sum(a,b)


'''
