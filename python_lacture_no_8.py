# part 1
#OOP in python 

#class & object in python

# creating class or creating object
class Student:
    name ="karan"       #this is a class 
 
s1 = Student()          #this is a object
print(s1.name)

# __init__function
class Student:
    def __init__(self,fullname):      #__init__ this is a function
        self.name = fullname

s1 = Student("karan")
print(s1.name)


#e.g
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan",97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)


#class and instance attributes
class Student:
    collage_name = "ABC collage"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan",97)
print(s1.name)
print(s1.collage_name)   

# methods

class Student:
    def __init__(self,fullname):
        self.name = fullname

    def hello(self):
        print("hello",self.name)

s1 = Student("karan")
s1.hello()

#e.g
class Student:
    collage_name = "ABC collage"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,",self.name)
    
    def get_marks(Self):
        return Self.marks
    
s1 = Student("karan",97)
s1.welcome()
print(s1.get_marks())

# let's practices

# 1.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(slef):
        sum = 0
        for val in slef.marks:
            sum += val
        print("hi",slef.name,"your avg score is:",sum/3)

s1 = Student("tony stark",[99,98,97])
s1.get_avg()

s1.name = "iron man"
s1.get_avg()

#static method 

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():                    #static method
        print("hello")

    def get_avg(slef):
        sum = 0
        for val in slef.marks:
            sum += val
        print("hi",slef.name,"your avg score is:",sum/3)

s1 = Student("tony stark",[99,98,97])
s1.get_avg()

s1.name = "iron man"
s1.get_avg()
s1.hello()

# IMPORTANT 

# Abstraction

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True              # this is a part of unneccessary
        self.acc = True
        print("car started..")          

car1 = car()
car1.start()

#Encapsulation
# wrapping data and function into a single unite(object)

#let's practice

# 1. 
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was creadit")
        print("total balance=", self.get_balance())

    def get_balance(self):
        return self.balance
acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)


# part 2

#del keyword

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("shradha")
print(s1.name)
del s1.name
print(s1.name)

#private (like) attribute & method

class Person:
    __name = "anonymous"

    def __hello():                      # private thing write like this '__' this symbol
        print("hello person")

p1 = Person()
print(p1.hello())

# inheritance  or 1.single inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())

# 2. multi-level inheritance

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("disel")
car1.start()

# multiple inheritance 

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


#super method

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("prius","electric")
print(car1.type)

# class method

# NOT:-  static method can't access or modify 
# class state & generally for utility

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("rahual kumar")
print(p1.name)
print(Person.name)

# property

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percantage(self):
        return str((self.phy + self.chem + self.math)/3) +"%"
    
stu1 = Student(98,97,99)
print(stu1.percantage)

stu1.phy = 86
print(stu1.percantage)

# polymorphism: operator overloadhing

# 1. addition

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

# let's practice

#1. 
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7)* self.radius ** 2
    
    def perimeter(self):
        return 2*(22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#2.
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        super().__init__("Engineer","IT","7500")
        
engg1 = Engineer("elong musk",40)
engg1.showDetails()

#3. 
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips",20)
odr2 = Order("tea",15)
print(odr1 > odr2)
