# dictionary is a collection of key-value pairs
student = {
    "name" : "Alice",
    "age" : 20,
    "marks" : 95
}
# PROPERTIES OF PYTHON DICTIONARIES 
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys. 
# dictionary methods
# clear() - removes all the items from the dictionary
student.clear()
print(student)
# copy() - make a copy of the dictionary
new_student = student.copy()
new_student["marks"] = 90
# print(new_student)
subject = ["math", "physics", "Computer"]
# fromkeys() - creates a new dictionary using a sequence of keys.
result = dict.fromkeys(subject,0)
print(result)
print(student.get("grade","Not available"))
print(student.keys())
print(student.values())
print(student.items())
for key,value in student.items():
    print(key,value)
student.pop("age")
print(student)
student.popitem()
print(student)
# setdefault() - gets the value of a key,if not found then it creates the key with a default value.
result = student.setdefault("grade", "O")
result = student.setdefault("marks", 0)
print(result)
print(student)
student.update({
    "age":21,
    "garde":"AA",
    "marks":96
})
print(student)
student.update(age=21,graduate=None,marks=90)
print(student)
print(len(student))


# A set is a collection of elements that:

# contains unique values
# is unordered
# is mutable (you can add/remove elements)
# does not support indexing like lists
num = {10,20,30,20,30}
set1 = {"Apple", "Banana", "Coconut"}
print(type(num))
print(len(num))
print(num)
x = {}
print(type(x)) # this is an empty dictionary
x1 = set()
print(type(x1))
'''1. add()
2. clear()
3. copy()
4. difference()
5. difference_update()
6. discard()
7. intersection()
8. intersection_update()
9. isdisjoint()
10. issubset()
11. issuperset()
12. pop()
13. remove()
14. symmetric_difference()
15. symmetric_difference_update()
16. union()
17. update()'''

num.add(20) # can add only one element at a time
num.update({20,90,85}) # can add multiple element at a time

num.remove(20) # remove a specified element, if not found gives keyerror
num.discard(85) # the only diff is that it does not give an error like remove
num.pop() # remove an arbitrary element 
num.clear() # remove everything
print(num)

set1 = {1,3,5}
set2 = {2,4,6}
set3 = {1,2,3,4,6,8,10}

print(set1.union(set2))
print(set1 | set2) # | set union operator
print(set2.intersection(set3))
print(set3 & set2) # & set intersection operator
print(set3 - set2) # difference 
print(set3 ^ set2) # symmetric difference
print(set1.isdisjoint(set2))
print(set3.issubset(set2))
print(set3.issuperset(set2))
