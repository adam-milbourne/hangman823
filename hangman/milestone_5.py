import random

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
             print("")
             print("good guess! " + guess + " is in the word")
             for idx, c in enumerate(word):
                if c == guess:
                   word_guessed[idx] = c
             num_letters = num_letters -  1    
        else:
           self.num_lives = self.num_lives - 1
           print("")
           print("Sorry ", guess,  " is not in the word.")
           print("")
           print("You have ", self.num_lives,  " lives left.")
        
           
                   


    def ask_for_input(self):
       #while True:
        print("")
        print(word_guessed)
        print(" ")
        print('guesses: ', list_of_guesses)
        print("")
        print("number of letters left: ", num_letters)   
        print("")

        guess = input("Guess a Letter: ")
        if len(guess) != 1 or guess.isalpha() == False:
           print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in list_of_guesses:
           print("You already tried that letter!")
        else: 
           list_of_guesses.append(guess)
           self.check_guess(guess)
          

def play_game(word_list):
   num_lives = 5
   game = Hangman(word_list, 5)
   while True:
    if game.num_lives == 0:
     print("YOU LOST")
     break
    elif num_letters > 0:
     game.ask_for_input()
    else:
     print(word_guessed)
     print("Congratulations! You won the game!")
     break

    
play_game(word_list)
   


