#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!

print("My favorite character is: " + heroes[1] + "!")


# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.

nums= [1, -5, 56, 987, 0]

user_input = input("user, select a random number from 1 to 100\n>")

print(user_input)



# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!


max_number = max(nums)

print(max_number)
