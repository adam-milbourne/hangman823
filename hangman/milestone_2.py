import random #imports random module

#VARIABLES
word_list = ["Apple", "Banana", "Grapes", "Strawberries", "Pineapples"] #list of fruits to choose word from
print(word_list)#check list prints

word = random.choice(word_list)#creates a variable called work from the list

print(word)#check it chooses a random word every time


def player_guess_letter():
    guess = input("Guess a letter: ")
    if len(guess) == 1 & guess.isalpha() == True:
        print("Good guess!")  
    else:
     print("Oops! That is not a valid input")

player_guess_letter()

