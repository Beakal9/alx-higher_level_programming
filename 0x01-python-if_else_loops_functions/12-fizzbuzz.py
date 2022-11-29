#!/usr/bin/python3
# Author - Beakal Ketema
"""print the numbers from 1 to 100 separated by a space.
   For multiples of three, print Fizz instaed of the number
   For multiples of five, print Buzz instaed of the number.
   For multiples of three and five, print FizzBuzz instaed of the number
   """
   def fizzbuzz():
       for number in range(1, 101):
           if number % 3 == 0 and number % 5 == 0:
               print("FizzBuzz ", end="")
           elif number % 3 == 0:
               print("Fizz ", end="")
           elif number % 5 == 0:
               print("Buzz ", end="")
           else:
               print("{} ".format(number), end="")
