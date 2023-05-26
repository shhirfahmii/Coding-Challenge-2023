#!/usr/bin/env python 
#FahmiandAlip
import random

def main():
  """Start a music guessing game."""
  print("Guess the song!")

  song = [
      "Nafisa",
      "Aku masih disini",
      "Titian perjalanan",
      "Hentian ini",
      "Semangat yang hilang",
      "Aku dan sesuatu",
      "C.i.n.t.a",
      "Hijau bumi tuhan",
      "Hidup bersama",
      "Impian seroja"
        ]

  x = random.choice(song)
  guess = None 
  
  while x !=guess:

      guess = str(input("What XPDC song im think of ?: "))

      if x == guess:
          print("You guessed {}. Congratulations you got it right!".format(guess))
          break
      else:
          print("You guessed{}. Unfortunately you got the answer. Please try again!".format(guess))
  
main()