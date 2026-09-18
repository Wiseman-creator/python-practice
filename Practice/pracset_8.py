# Write a program using functions to find greatest of three numbers


def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x = greatest(12, 10, 16)
print(x)

#  Write a python program using function to convert Celsius to Fahrenheit


def Celcius_to_fahrenheit(celsius: float) -> float:
    Fahrenheit = (celsius * 9 / 5) + 32
    return Fahrenheit


c1 = Celcius_to_fahrenheit(97.6)
print(c1)

# How do you prevent a python print() function to print a new line at the end.
# addind end=" "

# Write a recursive function to calculate the sum of first n natural numbers.


def summation(n):
    if n == 1:
        return 1
    else:
        return n + summation(n - 1)


sum = summation(10)
print(sum)

# Write a python function to print first n lines of the following pattern:
# ***
# **
# * - for n = 3


def star_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)


star_pattern(3)

# Write a python function which converts inches to cms.


def inch_to_cm(inches):
    cm = inches * 2.54
    return cm


y = inch_to_cm(5)
print(y)

# Write a python function to remove a given word from a list ad strip it at the same time.


def remove_word(words, word):
    result = []

    for item in words:
        item = item.replace(word, "").strip()
        result.append(item)

    return result


words = ["  Harry  ", "Rohan", "  Harry", "Ankit  "]

print(remove_word(words, "Harry"))
