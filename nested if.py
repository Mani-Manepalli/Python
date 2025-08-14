weather = input("Enter the weather (Sunny,Rainy) :")
if weather == "sunny":
    if input("Is it hot? (yes/no): ") == "yes":
     print("Wear a hat")
    else:
     print("Wear sunglasses")
elif weather == "rainy":
    if input("Is it cold? (yes/no): ") == "yes":
        print("Wear a raincoat")
    else:
        print("Take an umbrella")
else:
    print("Stay indoors")








