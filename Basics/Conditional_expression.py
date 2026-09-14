#  a codition is something that can be evaluated as either true or false
# comparison operators are > , < , >= , <= , == , !=
# = means assignment where == means comparison
# == → equality comparison
# is → identity comparison
# there is if ,if-else, if - elif - else

age = int(input("Enter your age:"))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior citizen")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

num = int(input("Enter a number:"))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negetive")

# logical operator -- and , or , not

age = int(input("Enter your age:"))
if age >= 18 and age <= 60:  # and means both codition must satify
    print("Eligible")
else:
    print("Not Eligible")

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

attandance = 80
fees_paid = True

if attandance >= 75 and fees_paid == True:
    print("Allowed for exam")
else:
    print("Not Allowed")

# chained comparison
if 18 <= age <= 60:
    print("Allowed")
else:
    print("Not allowed")

# Nested if statements

card_valid = True
pin_correct = True
balance = 5000
amount = 1000

if card_valid:
    if pin_correct:
        if amount <= balance:
            print("Transaction successful")
        else:
            print("Insufficient balance")
    else:
        print("Incorrect PIN")
else:
    print("Invalid card")

# Truthy and falsy values
numbers = [1, 2, 3]

if numbers:
    print("The list has elements")

name = input("Enter your name: ").strip(" ")

if name != "":
    print("Hello", name)
else:
    print("You didn't enter a name")

# Membership condition are in , not in , is , is not
numbers = [10, 20, 30, 40]

if 20 in numbers:
    print("20 is present")

if 50 not in numbers:
    print("50 is not present")

student = {"name": "Shibam", "age": 20}

print("name" in student)  # True
print("Shibam" in student)  # False
