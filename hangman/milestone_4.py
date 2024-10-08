import random
import sys
word_list = ["apple", "banana", "grapes", "strawberries", "pineapples"]
word = random.choice(word_list)
word_guessed = ["_"]*len(word)
num_letters = len(list(set(word)))
list_of_guesses = []


class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
       

    
    def check_guess(self, guess):
        global num_letters
        guess = guess.lower()
        if guess in word:
             print("good guess! " + guess + " is in the word")
             for idx, c in enumerate(word):
                if c == guess:
                   word_guessed[idx] = c
             num_letters = num_letters -  1    
        else:
           self.num_lives = self.num_lives - 1
           print("Sorry ", guess,  " is not in the word.")
           print("You have ", self.num_lives,  " lives left.")
           
                   


    def ask_for_input(self):
       while True:
        print(word_guessed)
        print(" ")
        print('guesses: ')
        print(list_of_guesses)
        print("number of letters left: ")
        print(num_letters)
        
        

        guess = input("Guess a Letter: ")
        if len(guess) != 1 or guess.isalpha() == False:
           print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in list_of_guesses:
           print("You already tried that letter!")
        else: 
           list_of_guesses.append(guess)
           self.check_guess(guess)
          

my_hangman = Hangman(word_list, 5)
my_hangman.ask_for_input()
