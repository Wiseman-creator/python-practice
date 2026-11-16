# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’

with open(r"Practice\poems.txt", "r") as poem:
   text = poem.read()

print(text)
if "twinkle" in text.lower():
   print("it contains the word ‘twinkle’")
else:
   print("it doesn't contain the word ‘twinkle’")

#  The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

import random

choice = ["stone", "paper", "scissor"]

def game():
    print("Enter your choice:")
    print(choice)

    user_input = input().lower()

    while user_input == "quit":
        return 0
    
    computer_input = random.choice(choice)
    score_count = 1

    if user_input == computer_input:
        print("It's a draw!")
        score_count += 0

    elif (
        (user_input == "stone" and computer_input == "scissor")
        or
    (user_input == "paper" and computer_input == "stone")
        or
        (user_input == "scissor" and computer_input == "paper")
    ):
        print("You win!")
        score_count += 1

    else:
        print("Computer wins!")
        score_count -= 1

    return score_count

score = game()

try:
    with open("Hi-score.txt",'r') as file:
        high_score = file.read()

    high_score = int(high_score) if high_score else 0
except FileNotFoundError:
    print("File does not exist!")
    high_score=0

if score > high_score:
    with open("Hi-score.txt","w") as file:
        file.write(str(score))

        print("New high score!",score)
else:
    print("High score", high_score)

    

