import random
from random  import randint

x=randint(1,100)

print("Welcome to the guessing game!")
print("Guess a number between 1 and 100")
print("you have 10 tries")
print("Good luck!")
print("")
print("")

y = 0
for i in range(1, 11):
  print("guess number", i)
  y= int(input("pick a number from 1 to 100: "))
  print("")
  if y == x:
    print("YOU WIN!")
    print("")
    break
  elif y > x:
    print("lower")
    print("")
  elif y < x:
    print("higher")
    print("")

if y != x:
  print("YOU LOSE!")
  print("the number was", x)

print("The End")
