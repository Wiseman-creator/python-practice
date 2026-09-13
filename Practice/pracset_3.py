# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"{name}, Good afternoon")
#  Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''
import datetime
today = datetime.date.today()
print(f"Dear {name},\nYou are selected!\n{today}")
# Write a program to double spacing in a string
text = "I am felling nervous  today"
print(text.find("  ") != -1)
# Replace the double space from problem 3 with single spaces.
print(text.replace("  ","   "))
letter = "Dear Shibam,\n\tThis Python course is nice.\nThanks!"
print(letter)