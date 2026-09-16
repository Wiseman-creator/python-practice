#  Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number:"))
print("Multiplication table of ", num)
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print("Good morning!", name)

# Attempt problem 1 using while loop

num = int(input("Enter a number:"))
print("Multiplication table of ", num)
i = 1
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1

# Write a program to find whether a given number is prime or not

num = int(input("Enter a number:"))
if num < 2:
    print("It isn't a prime number")
else:
    sqrt_num = int(num**0.5)

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            print("It isn't a prime number")
            break
    else:
        print("It is a prime number")

# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a number:"))
i = 1
total = 0
exp = ""

while i <= num:
    total += i
    exp += str(i)
    if i < num:
        exp += " + "
    i += 1
print(exp, "=", total)

# Write a program to calculate the factorial of a given number using while loop

num = int(input("Enter a number:"))
i = 1
total = 1
exp = ""

while i <= num:
    total *= i
    exp += str(i)
    if i < num:
        exp += " X "
    i += 1
print(num, "!  =", total)

# Write a program to print the pyramid star pattern
n = 3

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2 * i - 1))

#  Write a program to print the following star pattern:
# *
# **
# ***      for n = 3

n = 3

for i in range(1, n + 1):
    print("* " * i)

# Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * *

n = 3
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Write a program to print multiplication table of n using for loops in reversed order

num = int(input("Enter a number:"))
print("Multiplication table of ", num)
for i in range(10, 0, -1):
    print(f"{num} X {i} = {num * i}")
