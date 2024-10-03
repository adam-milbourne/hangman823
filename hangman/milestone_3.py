import milestone_2

def check_guess(guess):
    guess = guess.lower()
    if guess in milestone_2.word:
     print("good guess! " + guess + " is in the word")
    else:
     print("sorry, " + guess + " is not in the word")


def ask_for_input():  
 while True:
    guess = input("Guess a Letter: ")
    if len(guess) == 1 & guess.isalpha() == True:
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character")
 check_guess(guess)


ask_for_input()


