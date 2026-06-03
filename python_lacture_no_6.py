#function and recursion

def calc_sum(a,b):
    return a + b

sum = calc_sum(1,2)
print(sum)

sum = calc_sum(22,99)
print(sum)

def print_hello():
    print("hello")

i = 1
while i <= 5:
    print(print_hello())
    i += 1

def calc_avg(a, b, c):
    sum = a + b+ c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(98, 97, 95)

def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5,10)

calc_sum(10,10)

#types in pyhton

print("apnacollage",end=" ")
print("sujal somase")

#default parameters

def cal_prod(a,b=2): # this is called defauld parameters
    print(a * b)
    return(a * b)

cal_prod(3)

#lets practice

1. 

cities = ["delhi", "kalamb", "latur", "dharashiv", "mumbai", "nashik"]
movies = ["KGF", "salar", "spiderman","avanger"]

def print_len(list):
    print(len(list))
    return len

print_len(cities)
print_len(movies)

2.

cities = ["delhi", "kalamb", "latur", "dharashiv", "mumbai", "nashik"]
movies = ["KGF", "salar", "spiderman","avanger"]

def print_list(list):
    for item in list:               #function defination 
        print(item,end=" ")

print_list(cities)   # function call
print()

3.

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(5)

4.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD=", inr_val,"INR")

converter(100)

def function(n):
    if(n % 2 == 0):
        print("even")
    else:
        print("odd")
    return(function)

function(2)

#recursion

def show(n):
    if(n == 0):
        return
    print(n)                # all function is call recursion
    show(n - 1)

show(5)

#returns n! (factorial)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n - 1) * n

print(fact(2))

#let's practice

1.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)

2. 

def print_list(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx + 1)

fruit = ["mango","litchi","apple","banana"]
print_list(fruit)
    