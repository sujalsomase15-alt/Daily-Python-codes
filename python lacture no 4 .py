#dictionary and sets

#dictionary in python 

info = {
    "key" : "value",
    "name" : "apnacollage",
    "subjects" : ["python", "java", "C++"],
    "topics" : ("dictionary", "sets"),
    "learning" : "python",
    "age" : 18,
    "is_adult" : True
}

info["name"] = "sujal "
info["surname"] = "somase"
print(info)

student = {
    "name" : "sujal somase",
    "subjects" : {
        "phy" : 90,
        "chem" : 80,
        "math" : 70,
    }
}

student.update({"city" : "pune"})
print(student)

# set in python.
collection = {1, 2, 3, 4, "hellow", "welcome"}
print(collection)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add("hellow")
collection.clear()
print(len(collection))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))

dictionary = {
    "cat" : " a samll animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}
print(dictionary)

subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(len(subjects))


marks = {}

x = int(input("enter phy: "))
marks.update({"phy" : x})
x = int(input("enter math: "))
marks.update({"math" : x})
x = int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)

value = {
    ("float" , 9.0),
    ("int", 9)
}
print(value)