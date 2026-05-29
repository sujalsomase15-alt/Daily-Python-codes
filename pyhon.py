# string and conditional statement

# Strings
# indexing
# slicing
# string function
# conditional statement

light = str(input("enter colour of light:"))

if(light =="green"):
    print("go")
elif(light =="red"):
    print("stop")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("code is end")

age = 18
if(age>=18):
    print("vote")
else:
    print("not vote")

marks = int(input("enter your marks:"))

if(marks >=90):
    grade = "A"
elif(marks >=80 and marks <90):
    grade = "B"
elif(marks >=70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("your grade is->",grade)

age = 12

if(age >= 18):
    if(age >=80):
        print("can't drive")
    else:
        print("can drive")
else:
    print("cannot drive")

num = int( input("enter number"))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a>=b and a >=c):
    print("first number is largest")
elif(b>=a and b >=c):
    print("second number is largest")
else:
    print("third number is largest")

x = int(input("enter number:"))

if(x % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if( a>=b and a>=c and a>=d):
    print("first number is largest")
elif(b>=c and b>=d):
    print("second number is largest")
elif(c>=d):
    print("third number is largest")
else:
    print("fourth number is largest")
