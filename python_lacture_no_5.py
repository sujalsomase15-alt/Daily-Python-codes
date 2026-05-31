# loops in python
count = 1
while count <=5:
    print("hello",count)
    count+=1
    print(count)

i = 1
while i <=5:
    print("apnacollage",i)
    i += 1

# print number from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
print("loop ended")

# print number from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1
print("loop is ended")

# Let's practice
# 1 . print number from 1 to 100 or 100 to 1

i = 100
while i >= 1: # stoping condn
    print(i)
    i -= 1
print("loop is ended")

# 2 . print the multiplication table of a number n.

n = int(input("enter number:"))
i = 1
while i <= 10:
    print(n*i)
    i+=1

# 3. print the elements of the following list using a loop:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])            # traverse
    idx += 1

# 5. search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    if (nums[i] ==x):
        print("FOUND at idx", i)
    else:
        print("Finding..")
    i += 1

names = ("Alice", "Bob", "Charlie", "David", "Eve")

x = "Eve"
i = 0
while i < len(names):
    if(names[i] ==x):
        print("i found this name at idx", i)
    else:
        print("i finding this name..")
    i += 1

# Break and containue key word.

i = 0 
while i <= 5:
    if(i ==3):
        i += 1
        continue
    print(i)
    i += 1

# loops are used for sequential traversal. For traversing list, string, tuples etc.

str = "sujal_somase"
for cha in str:
    if(cha =='o'):
        print("o found")
        break
    print(cha)
else:
    print("END")

# lets practice

# 1. print the elements of the following list using a loop:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

# 2. search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49
idx = 0                # linear search

for el in nums:
    if(el == x):
        print("number found at inx", idx)
        break
    idx += 1

range()
for i in range(10): # range(stop)
    print(i)

for i in range(2,10): # range(start,stop)
    print(i)
    
for i in range(2,10,1): # range(start,stop,step)
    print(i)
    

for i in range(2, 100, 1): # even number sathi 2 and odd number sathi 1
    print(i)


# let's practice

# print number from 1 to 100

for i in range(1, 101, 1):
    print(i)

# print number from 100 to 1

for i in range(100, 0, -1):
    print(i)

# print the multiplication table of a number n.

n = int(input("enter number:"))

for i in range(1, 11):
    print(n * i)

# pass statement

for i in range(9):
    pass
   

# lets practice

# 1. WAP to find the sum of first n numbers.(using while)

n = int(input("enter first:")) # for loop

sum = 0
for i in range(1, n+1):
    sum += i

print("total sum = ", sum)


n = int(input("enter first:"))  # while loop 

sum = 0 
i = 1
while i <= n:                       
    sum += i
    i += 1
print("total sum = ", sum)

# WAP to find the factorial of first n numbers. (using for)

n = 5      # while loop
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial =",fact)