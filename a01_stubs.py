######################################################################
# Author: Ben Maynard
# Username: maynardb
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
birfday = input("What year were you born on? ")

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if birfday == 1976 or birfday == 1988 or birfday == 2000:
    print("Have you seen Mulan? well you're a dragon just like mushu.")


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend = input("What's your friends birth year?")

# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
if friend == 1979 or friend == 1991 or friend == 2003:
    print("You're the GOAT")

######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
