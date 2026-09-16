# loop = repeat a block of code multiple times
# for loop

for i in range(5):
    print(i)

# range(start, stop, step)
for i in range(21, 11, -1):
    print(i)

# loop through strings,lists,dict
names = ["arjun", "pushpendu", "Debanshu", "Sumana"]
for name in names:
    print(name)

student = {"name": "Rahul", "age": 20, "marks": 96}

# for key,value in student.items():
#     print(f"{key} : {value}")

# while loop - repeats as lang as the condition is true
i = 1

while i <= 5:
    print(i)
i += 1

for i in range(1, 11):
    if i == 5:
        continue  # continue - skip the current iteration and go to the next one
    print(i)

for i in range(1, 11):
    if i == 5:
        break  # break - completely stops the loop
    print(i)

# pass  # do nothing for now in a loop

for i in range(3):
    for j in range(3):
        print(i, j)

# for else
numbers = [3, 34, 56, 63, 55]

for num in numbers:
    if num == 55:
        print("found")
        break
    else:
        print("not found")

total = 0
count = 0

for num in numbers:
    total += num
print(total)
print(sum(numbers))

for num in numbers:
    count += 1
print(count)
print(len(numbers))

# pattern printing

for i in range(5):
    print("*", end=" ")

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(5, 0, -1):
    print("* " * i)

for i in range(5):
    print(i + 1, end=" ")
print()

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
print()

for i in range(1, 6):
    for j in range(i):
        print(j + 1, end=" ")
    print()
print()

for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

num = 1

for i in range(5):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()
