import random
from colorama import Fore

capitals = ['beijing', 'new delhi', 'washington dc', 'berlin', 'tokyo', 'brasilia', 'cairo', 'paris', 'moscow', 'mexico city']
countries = ['China', 'India', 'United States', 'Germany', 'Japan', 'Brazil', 'Egypt', 'France', 'Russia', 'Mexico']

print(Fore.MAGENTA + "THIS IS A CAPITAL GUESSING GAME. GUESS THE CAPITAL OF THE GIVEN COUNTRY. \n")

def game(c):
  randomNumber = random.randint(0,9)
  chosen_country = countries[randomNumber]
  chosen_capital = capitals[randomNumber]
  c = chosen_country
  def play_again(): #asking users if they want to play again
    play_again = input(Fore.BLUE + "Would you like to play again? (y/n) ").lower()
    while play_again != "y" and play_again != "n":
      play_again = input(Fore.BLUE + " ⚠️ Please enter a valid input. Would you like to play again? (y/n) ").lower() #accounting for bad user input
    if play_again == "y":
      print("\n")
      game(chosen_country)
    elif play_again == "n":
      quit() #ending program
  tries = 3
  print(Fore.GREEN + "You have " + str(tries) + " tries")
  user_input = input(Fore.BLUE + "Guess the capital of " + c + ": ").lower()
  while tries > 0 and tries != 0: 
    if user_input == chosen_capital:
      print("That is correct! \n")
      play_again()
    while user_input != chosen_capital:
      if tries < 1 or tries == 1:
        print(Fore.RED + "You ran out of tries! \n")
        play_again()
      print(Fore.RED + "That is incorrect! Please try again. \n")
      tries = tries - 1
      print(Fore.GREEN + "You have " + str(tries) + " tries left.")
      user_input = input(Fore.BLUE + "Guess the capital of " + c + ": ").lower()

      
game(countries[random.randint(0,9)])