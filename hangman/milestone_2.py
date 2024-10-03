import random #imports random module

#VARIABLES
word_list = ["apple", "banana", "grapes", "strawberries", "pineapples"] #list of fruits to choose word from
print(word_list)#check list prints (TODO: make sure to remove this once debugging is over otherwise will show player the words list)

word = random.choice(word_list)#creates a variable called work from the list

print(word)#check it chooses a random word every time (TODO: make sure to remove this once debugging is over otherwise will show player the word)




#!!!!!!!!!RECREATED IN MILESTONE 2!!!!!!!!!!!!!!!
#def player_guess_letter():
#    guess = input("Guess a letter: ")
#    if len(guess) == 1 & guess.isalpha() == True:
#        print("Good guess!")  
#    else:
#     print("Oops! That is not a valid input")

#player_guess_letter()

