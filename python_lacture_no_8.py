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