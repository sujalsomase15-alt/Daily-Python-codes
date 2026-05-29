# list and tuples 

# list in python

marks = [12.2, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

student = ["sujal", 99.4 , 18 , "kalamb"]
print(student[0])
student[0]= "arjun"
print(student)

marks = [ 56, 65, 56, 54, 55]
print(marks[-3:-1])

# list methods
list = [ 2, 3, 1, 2, 3]
list.pop(1)
print(list)

# tuples in python

tup = (1, 2 , 3, 4, 1)
print(tup.count(1))

movies = []
movie1 = input("enter your first favorite movie:")
movie2 = input("enter your second favorite movie:")
movie3 = input("enter your third favorite movie:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

family = [ ]

a = input("first membor name:")
b = input("second membor name:")
c = input("third membor name:")
d = input("fourth membor name:")

family.append(a)
family.append(b)
family.append(c)
family.append(d)

print(family)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.sort())
print(grade)



