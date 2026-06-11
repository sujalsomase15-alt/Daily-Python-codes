#file i/o
# f = open("demo.txt","r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()

#writing to a file

# f = open("demo.txt","a")
# f.write(" \ni want to learn javascript tp,orrow.123")
# f.close()

# f = open("sample.txt","a")
# f.close()


# f = open("demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# f = open("demo.txt","w+")
# print(f.read())
# f.write("abc")
# f.close()

#with syntax

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# import os
# os.remove("sample.txt")

#lets practice

# 1. 

# with open("practice.txt","w") as f:
#     f.write("hi every one\nwe are learning file I/O\n")
#     f.write("using java\nI like programming in java")

# 2. 
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


# 3. 

# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):             #method 1
#         print("found")
#     else:
#         print("no found")

# def cheak_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):          #method 2
#             print("found")
#         else:
#             print("no found")

# cheak_for_word()


# 4.

# def check_for_line():
#     word = "learnings"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1

# print(check_for_line())
       
# 5.
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)