# 1. Write a program to store seven fruits in a list entered by the user. 
# 2. Write a program to accept marks of 6 students and display them in a sorted manner. 
# 3. Check that a tuple type cannot be changed in python. 
# 4. Write a program to sum a list with 4 numbers. 
# 5. Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9)
fruits =[]
for i in range(7):
    fruit = input("Enter the name of fruit: ")
    fruits.append(fruit)
print("The list of fruits is:", fruits)
# another approach
fruitss =input("Enter 7 fruits seperated by commas: ").split(",")
print("The list of fruits is:", fruitss)
# problem 2
marks=[]
for i  in range(6):
    mark = int(input("Enter the marks of 6 students:"))
    marks.append(mark)
print("The sorted marks are:", sorted(marks))
# problem 3
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
# print(tuple1.append(6))
# makes an attribute error because tuples are immutable
# problem 4
list1 = [1784, 8246, 4563, 8474]
sum = sum(list1)
print("Sum of 4 digits:",sum)
# problem 5
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))