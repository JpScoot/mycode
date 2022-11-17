#!/bin/env python3

#Save a user's input to the variable char_name from the following question:
char_name = input("which character do you want to know about? (Starlord, Mystique, Hulki)\n>").capitalize()

#Save a user's input to the variable char_stat from the following question:
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n>").lower()

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
# good! you are printing out the answer that the user is looking for!
answer= marvelchars[char_name][char_stat]

# for the final stretch, you're going to want to use that for a print that does the following:
print(f"{char_name}'s {char_stat} is: {answer}")





