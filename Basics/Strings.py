# string is a sequence of characters enclosed in quotes.
# string slicing:
name = "alchemist"
text ="lorem"
pr_header = "python programming"
print(name[0]) # prints first character
print(len(name))
print(name[0:7])
# string slicing with skip value
print(name[0:7:2])
# string functions 
# changingig case
print(name.upper()) #converts to uppercase
print(name.lower()) # converts to lowercase
print(name.capitalize()) # converts first character to uppercase
print(pr_header.title()) # converts first character of each word to uppercase
# str.swapcase() - converts uppercase to lowercase and vice versa
# str.casefold() - converts string to lowercase for caseless matching
# finding & searching
print(name.find("ch"))
print(text.find("rem")) #find the position of the substring;if niot fopund then it returns -1
print(name.rfind("ch")) #finds the last occurrence of the substring from the right
print(pr_header.index("ing")) #finds the position of the substring; if not found then it raises ValueError
print(pr_header.count("m")) #counts the number of occurrences of the substring
print(text.startswith("lo"))
print(name.endswith("em)"))

# checking alphanumeric, alphabetic, digit, whitespace
username1 = "alphanumeric 593   "
'''str.isalpha() - checks if all characters in the string are alphabetic
str.isdigit() - checks if all characters in the string are digits
str.isdecimal() - checks if all characters in the string are decimal characters
str.isalnum() - checks if all characters in the string are alphanumeric
str.isnumeric(), isspace() , islower(), isupper(), istitle(), 
isidentifier()	valid Python identifier
isascii()	all characters are ASCII
isprintable()	all characters are printable
'''
# removing whitespace
print(username1.strip()) #removes leading and trailing whitespace
# str.lsrtrip() #removes leading whitespace
# str.rstrip() #removes trailing whitespace
# there are also str.removeprefix() and str.removesuffix() methods to remove prefix and suffix from a string.

# replacing
print(pr_header.replace("python", "Java")) #replaces substring with another substring
# spiltting strings
text = "apple,banana,cherry,mango,lichi,grapes,orange"
fruits = text.split(",") 
#splits the string into a list of substrings based on the delimiter
print(fruits)
# there are also str.splitlines() and str.partition() methods to split strings based on line breaks and partition a string into three parts based on a separator.
print(pr_header.partition("programming")) #splits the string into three parts based on the separator
# joining strings
print(",".join(fruits))
# aligning strings
print(name.center(60))
# ljust() - left align, rjust() - right align, zfill() -add zeros to the left
# encoding and decoding
print(name.encode())
print(type(name.encode()))

# f strings - formatted string literals
print(f"I am an {name} and i am learning {pr_header}")
#uses
pi = 3.14159
print(f"pi = {pi:.2f}")
marks = 89.58954545
print(f"Your percentage is {marks:.2f}%")
score = 0.875
print(f"Score: {score:.2%}")
amount =10000
print(f"Amount: ${amount:,}") # adds comma as thousand separator

# escape sequences
'''newline (\n) - moves the cursor to the next line
tab (\t) - adds a horizontal tab space
backslash (\\) - adds a backslash character
single quote (\') - adds a single quote character
double quote (\") - adds a double quote character
carriage return (\r) - moves the cursor to the beginning of the line
backspace (\b) - moves the cursor one position back
form feed (\f) - adds a form feed character
vertical tab (\v) - adds a vertical tab character
alert (\a) - triggers an alert sound'''