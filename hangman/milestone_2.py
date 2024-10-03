import random

word_list = ["Apple", "Banana", "Grapes", "Strawberries", "Pineapples"]
print(word_list)

word = random.choice(word_list)

print(word)


guess = input("Guess a letter: ")
if len(guess) == 1 & guess.isalpha() == True:
    print("Good guess!")  
else:
    print("Oops! That is not a valid input")

