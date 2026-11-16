# 1. Write a program to create a dictionary of English words with values as their bengali
# translation. Provide user with an option to look it up!
words = {
    "Ability": "সক্ষমতা",
    "Accept": "গ্রহণ করা",
    "Achieve": "অর্জন করা",
    "Advice": "পরামর্শ",
    "Answer": "উত্তর",
    "Arrange": "সাজানো / ব্যবস্থা করা",
    "Avoid": "এড়িয়ে চলা",
    "Begin": "শুরু করা",
    "Believe": "বিশ্বাস করা",
}
print(words.keys())
word = input("Search a word fom here:")
print(words.get(word))

# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
num_set = set()
print("Enter eight numbers:")
for i in range(8):
    num = int(input())
    num_set.add(num)
print("Unique numbers are:", num_set)


# Can we have a set with 18 (int) and '18' (str) as a value in it?
# yes, it is possible
set1 = {18, "18"}
print(set1)

# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
# length of s after these operations?
# the length of set will 3, cause int,float,string

s = {}
# What is the type of 's'?
# it is a dictionary type, to make it an empty set it will be like
s = set()

#  Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
fav_lang = {}
for i in range(4):
    name = input("Enter name:")
    lang = input("Enter favourite language: ")
    fav_lang[name] = lang
print(fav_lang)

# If the names of 2 friends are same; what will happen to the program in problem 6
# If two names are the same, a Python dictionary cannot keep both as separate keys. The later value replaces the earlier value.

# If languages of two friends are same; what will happen to the program in problem 6?
# nothing happens

# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# Set elements must be hashable. Lists are mutable → lists cannot be elements of a set.
