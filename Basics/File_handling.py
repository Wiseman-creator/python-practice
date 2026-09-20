# file handling ---> using python to create, read, write, modify, and mage files stored in computer.

# file = open("students.txt") # open a file

# syntax ---> open("filename","mode")

# r - read, w - write, a - append, x - create

# If the file already contains data, "w" replaces the existing content

# readline() -- reads one line at a time

file = open(r"Basics\students.txt", "r",newline="\n")

print(file.readline())
print(file.readline()) # returns one string

print(file.readlines()) # read all the lines and returns them as a list

file.close()

students = ["Rahul\n", "Priya\n", "Amit\n"]

file = open("Basics/students.txt", "w")

file.write("Rohan\n")
file.write("Priya\n")

file.writelines(students)

file.close()

with open("Basics/students.txt", "r") as file:
    data = file.read()
    print(data)

# using a for loop to read a line
# why? -- if  i have 1 gb logfile, then if i do file.read() it tries to load everythinh into memory.
# but using for it can be done one by one

with open("Basics/students.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() ---> removes whitespace and unwanted \n from entering in working data.
print("\n")

with open("Basics/students.txt", "r") as file:

    print(file.tell()) # tell() ---> tells the current position of the file pointer.

    print(file.read(5))

    print(file.tell())

    print(file.read(5))

    file.seek(0) # seek() ---. moves the file pointer to a specefic position

    print(file.tell())

try:
    with open("marks.txt","r") as file:
        print(file.read())
except FileNotFoundError: # file does not exist
    print("File not found!")

try:
    with open("important.txt","r") as file:
        print(file.read())
except PermissionError: # the file exists but Python doesn't have permission to access it
    print("You don't have permission to access this file.")