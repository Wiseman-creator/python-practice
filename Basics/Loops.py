# # loop = repeat a block of code multiple times
# # for loop

# for i in range(5):
#     print(i)

# # range(start, stop, step)
# for i in range(21, 11, -1):
#     print(i)

# # loop through strings,lists,dict
# names = ["arjun", "pushpendu", "Debanshu", "Sumana"]
# for name in names:
#     print(name)

# student = {"name": "Rahul", "age": 20, "marks": 96}

# # for key,value in student.items():
# #     print(f"{key} : {value}")

# # while loop - repeats as lang as the condition is true
# i = 1

# while i <= 5:
#     print(i)
#     i += 1

# for i in range(1, 11):
#     if i == 5:
#         continue  # continue - skip the current iteration and go to the next one
#     print(i)

# for i in range(1, 11):
#     if i == 5:
#         break  # break - completely stops the loop
#     print(i)

# # pass  # do nothing for now in a loop

# for i in range(3):
#     for j in range(3):
#         print(i, j)

# # for else
# numbers = [3, 34, 56, 63, 55]

# for num in numbers:
#     if num == 55:
#         print("found")
#         break
# else:
#     print("not found")

# total = 0
# count = 0

# for num in numbers:
#     total += num
# print(total)
# print(sum(numbers))

# for num in numbers:
#     count += 1
# print(count)
# print(len(numbers))

# # pattern printing

# for i in range(5):
#     print("*", end=" ")

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     print("* " * i)

# for i in range(5):
#     print(i + 1, end=" ")
# print()

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# print()

# for i in range(1, 6):
#     for j in range(i):
#         print(j + 1, end=" ")
#     print()
# print()

# for i in range(1, 6):
#     print("  " * (5 - i) + "* " * i)

# for i in range(1, 6):
#     print(" " * (5 - i) + "* " * i)

# num = 1

# for i in range(5):
#     for j in range(i + 1):
#         print(num, end=" ")
#         num += 1
#     print()
"""--------------------------------------------------"""

# number manupulation
# reverse a number
input = 123456

reverse = 0

while input > 0:
    digit = input % 10
    reverse = reverse * 10 + digit
    input = input // 10

print(reverse)

# palindrome number
# 1331 --> 1331
num = 1331
original = num  # because num becomes 0 after the loop.
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

# armstrong number -- An Armstrong number is a number where the sum of each digit raised to the number of digits equals the original number.
#  153, 370, 371, 407

num = 407

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit**digits
    num //= 10
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Perfect Number - A perfect number is a number whose proper divisors add up to the number itself.
# 6, 28
num = 27

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("Perfect number")
else:
    print("Not a perfect number")
