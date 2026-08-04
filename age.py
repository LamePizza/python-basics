#fibonacci series with loop
n = int(input("Enter no. of fibonacci values needed: "))
a = 0
b = 1
print(a)
print(b)

for i in range (2, n):
    c = a + b 
    a = b
    b = c
    print(c," ")

#age checker using if-else
age = int(input("Enter your age: "))

if (age < 0):
    print("Invalid input")
elif (age < 18):
    print("you are a legal minor")
else:
    print("you are a legal adult")