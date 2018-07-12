"""This is a game where you roll a pair of dice and the user guesses what the sum of the two are."""
from random import randint
from time import sleep

print("**Dice Game Started**")

def get_user_guess():
  guess = int(raw_input("Guess a number or type \"0\" to end game: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The max value is: %d") % (max_val)
  print("The min value is: 2")
  guess = get_user_guess()
  if guess > max_val or guess < 1:
    return ("Your guess is invalid. Too high/low.")
  elif guess == 0:
    return ("Closing Game")
  else:
    print("Rolling...")
    sleep(2)
    print("First roll is: %d") % (first_roll)
    sleep(1)
    print("Rolling...")
    sleep(1)
    print("Second roll is: %d") % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("Result...is: %d") % (total_roll)
    sleep(1)
    if guess == total_roll:
      print("You won! Congratulations, you beat a computer!!!")
      sleep(2)
    else:
      print("I'm sorry, but the computer beat you...")
      sleep(2)
  print("Restarting Game...")
  sleep(3)
  roll_dice(6)
  
roll_dice(6)
