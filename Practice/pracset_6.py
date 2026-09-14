# # Write a program to find the greatest of four numbers entered by the user.
numbers = []
print("Enter four numbers:")

for i in range(4):
    a = int(input())
    numbers.append(a)

print("Greatest:", max(numbers))

# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

reqdtotal_marks = 120
subjectwise_passingmarks = 33
total = 0
marks = []

for i in range(3):
    mark = int(input(f"Enter marks in subject{i + 1}:"))
    marks.append(mark)
    total += mark
    if mark < subjectwise_passingmarks:
        print("You failed to achive subjectwise passing marks criterion.")
        break

if total >= reqdtotal_marks:
    print("You passed.")
else:
    print("You failed to achive required total marks.")

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

spam_comment = ["Make a lot of money", "buy now", "subscribe this", "click this"]

comment = input("Enter messege:").lower()

for spam in spam_comment:
    if spam in comment:
        print("Spam comment detected")
        break

# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter username:")
if len(username) < 10:
    print("Less than 10 character.")

# Write a program which finds out whether a given name is present in a list or not.

names = [
    "Rahul",
    "Amit",
    "Priya",
    "Sneha",
    "Arjun",
    "Riya",
    "Rohit",
    "Ananya",
    "Vikash",
    "Neha",
    "Sourav",
    "Pooja",
    "Karan",
    "Moumita",
    "Abhishek",
]
username = input("Enter username:").lower()

for name in names:
    if name.lower() == username:
        print("Name found!")
        break
else:
    print("Not found")

# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70  =>C
# 50 – 60 => D
# <50
# => F

marks = 98

if 100 >= marks > 90:
    print("Your grade: Ex")
elif 90 >= marks > 80:
    print("Your grade: A")
elif 80 >= marks > 70:
    print("Your grade: B")
elif 70 >= marks > 60:
    print("Your grade: C")
elif 60 >= marks > 50:
    print("Your grade: D")
else:
    print("Your grade: F")

# Write a program to find out whether a given post is talking about "Shibam" or not.
post = input("Enter your post: ").lower()

if "harry" in post:
    print("This post is talking about Shibam.")
else:
    print("This post is not talking about Shibam.")
