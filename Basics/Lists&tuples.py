# python lists are containers to store a set of values of any data type.
# list indexing
l1 = [7,9,"Shibam", 3.5, True]
print(l1[0]) 
print(type(l1[0]))
# slicing
# list[start : stop : step]
#   list reverse slicing
print(l1[::-1])
# list manipulation methods 
#  appeend() - add one item at the end of the list
l1.append(10)
# expand() - add multiple items 
l1.extend([50,607,89])
# insert()- add item at a specific position on the list 
l1.insert(2, "Python")
# removing
# remove() - remove a specific item 
# pop() - remove the item by index
# clear() - remove everrything
# index() - find a position of the value 
# count() - count the number of occurences of a value
# sort() - sort the list in ascending order
# reverse() - reverse the list
# copy() - copy the list to another list

# tuples
#  a tuple is an immutable data type in python.
t1= (7,9,"Shibam", 3.5, True)
# count() - count the number of occurences of a value
print(t1.count(7))
# index() - find a position of the value
print(t1.index("Shibam"))
t2 = (50,607,89)
# concatenation
print(t1+t2)
student = ("Shibam", 20, "Mathematics")
name, age, subject = student
print(f"Name: {name}, Age: {age}, Subject: {subject}")
# tuple unpacking
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)