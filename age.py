age = int(input("Enter your age: "))

if (age < 0):
    print("Invalid input")
elif (age < 18):
    print("you are a legal minor")
else:
    print("you are a legal adult")