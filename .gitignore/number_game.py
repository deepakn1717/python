###Wanna play a game? In this project, we built a program that rolls a pair of dice and asks the user to guess a number.Based on the
user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win!
Otherwise, the computer wins.###

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("guess a number : "))
  return user_guess

def rool_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "maximum possible value is " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "invalid number, you must enter a number lessthan or equal to " + str(max_val)
    return
  else:
    print "Rolling..."
    sleep(2)
    print "first dice number is %d" % (first_roll)
    sleep(1)
    print "second dice number is %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    sleep(1)
    print "number diced is %d" % (total_roll)
    sleep(1)
    if user_guess > total_roll:
      print "you won !"
      return
    else:
      print "sorry, you lost"
      return
    
    
rool_dice(7)
