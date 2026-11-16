# Object Oriented Programming ---
# 1. Class & Object ---
# a class is a blueprint,
# while object is an individual instance created from that blueprint.
# When class is defined, a template(info) is defined.
# Memory is allocated only after the object instantiation.

# Objects of a given class can invoke the methods available to it without revealing the
# implementation details to the user.- Abstractions & Encapsulation!

# class Employee:
    # Methods and variables

# Class attributes:-
# An attribute that belongs to the class rather than a particular object.
class Employee:
    company = "Google" # specific to each class
    name = "hello"
    salary = "20k"
    def getsalary(self):
        print("Salary is not there.")
    @staticmethod
    # Someti,es we need a function that does not use the self-parameter.
    def greet():
        print("Hello user")

harry = Employee() # Object Instatiation
harry.name = "harry"
harry.salary = "30k"
Employee.company = "Youtube" # changing class attribute

# __init__() constructur 
# __init__() is a special method which is  first run as soon as the object is created.
# __init__() method is also known as constructur.
# It tkes self argument and can also take further arguments.

