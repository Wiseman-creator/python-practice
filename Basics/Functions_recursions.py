# a function is a group of statements performing a specific task
# we use it because it is a reuseable block of code
# syntax
# def func1(parameter): ---> defenition of function
#   print("Hello") ---> function body
# func1() ---> function call
# there are two types of function in python like user defined function and built in functions.
# recursion is a function which calls itself
# eg --> factorial


def addz(a, b):
    print(a + b)


result = addz(10, 20)
print(result)  # output will be 30 None


def addition(a, b):
    return a + b


result = addition(10, 20)
print(result)  # gives the program back the result


def student_info(name, age=18):
    print("Name:", name)
    print("Age:", age)


student_info("Shibam", 20)


def calculate_bill(price, quantity):
    return price * quantity


print(calculate_bill(50, 10))

# Multiple parameters


def calculate_average(a, b, c):
    return (a + b + c) / 3


print(calculate_average(21, 19, 20))


#  default parameters
def calculate_bill1(amount, delivery_charge=40):
    return amount + delivery_charge


print(calculate_bill1(500))
print(calculate_bill1(500, 0))

# keyword arguments


def create_account(name, age, city, phone, email):
    print("Account created!")
    print(name, age, city, phone, email)


create_account(name="Shibam", age=20, phone="6329843904", city=None, email=None)

# x1 = 23
# # def calculate():
#     x = 10            # local variable
#     print(x1)         # global variable
# calculate()

# print(x)   # Error

#  *args --> allows a function to accept many positional arguments.


def total_expenses(*expenses):  # stores as a tuple
    return sum(expenses)


print(total_expenses(500, 200, 100, 50, 20, 10))

# **wargs ---> allows to accept multiple keyword arguments


def create_profile(**details):
    for key, value in details.items():
        print(key, ":", value)


create_profile(name="Shibam", age=20, subject="Mathematics")

# /  → before it = positional-only
#  → after it = keyword-only

# function calling in another function


def square(num):
    return num * num


def calc():
    result = square(5)
    return result + 10


print(calc())


def process_student(name, marks):

    def is_valid_marks(marks):
        return 0 <= marks <= 100

    if is_valid_marks(marks):
        print(name, "has valid marks")
    else:
        print("Invalid marks")


process_student("Shibam", 85)

#  Recursion ---> a function calling itself


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(10)


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# lambda function --->used when we need a small function without wanting to formally define it with def
# lambda arguments: expression

addd = lambda a, b: a + b
print(addd(12, 78))

students = [("Rahul", 75), ("Shibam", 90), ("Arjun", 82)]

students.sort(key=lambda student: student[1], reverse=True)
print(students)

# map() ---> a function to every item in an iterable
# filter() --->selects only the items that satisfy a condition.
# reduce() ---> repeatedly combines values to produce one final result.

marks = [70, 80, 90, 60]

# updated_marks = map(lambda x: x + 5, marks) , the warning we are getting because of map is In modern Python, a generator expression is often clearer for this simple transformation.
updated_marks = (x + 5 for x in marks)
passed = filter(lambda mark: mark >= 75, marks)

print(list(updated_marks))
print(list(passed))


# [ ]  → list comprehension → stores all results
# ( )  → generator expression → produces results when needed

number_list = [1, 2, 3, 4, 5, 6]

even_num = filter(lambda x: x % 2 == 0, number_list)

print(list(even_num))


# in python functions objects.
# 1. It can be stored in a varible
def greet():
    print("Hello")


messege = greet  # no paretheses

messege()


# 2. pass a function to another function
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(operation, a, b):
    return operation(a, b)


print(calculate(add, 10, 5))
print(calculate(multiply, 10, 5))

# closures ---> A closure is when an inner function remembers variables from the outer function.


def create_discount(rate):
    def discount(price):
        return price - price * rate

    return discount


student_discount = create_discount(0.10)

print(student_discount(500))

# decorator adds/modifies behavior of a function without changing the original function.


def log_fuction(func):
    def wrapper():
        print("Function start")
        func()
        print("Function start")

    return wrapper


@log_fuction
def logged_greet():
    print("Hello")


logged_greet()

# generator produces values one at a time, instead of creating everything at once.


def numbers():
    # for i in range(5):
    #     yield i
    yield from range(5)


for num in numbers():
    print(num)

# yield turns a function into a generator and pauses the function.


def count():
    yield 1
    yield 2
    yield 3


for x in count():
    print(x)

# Type hints tell you what type of data a function expects and returns.


def add3(a: float, b: int) -> float:
    return a + b


x5 = add3(34.4, 44)
print(x5)

# A docstring documents what a function does.


def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


print(calculate_area.__doc__)
