#### Steps to writing a program - a good approach
# Follow along in the comments to see how I might work through this if it were part of my practical.

## NOTICE tools.py IS IN THE SAME LOCATION AS YOUR PRACTICE FILES

"""
We'll be using the third example from our review class (see lecture notes for sample output):

Directions:
Write a function that takes a string and prints a ‘word centipede’ using that string. 
You’ll want to have your function call the dasher3 function from your tools file!
(Full credit only if you use tools.py correctly!)

"""

### STEP 1 - PART A - MAKE AN OUTLINE, USE COMMENTS TO MARK OUT SECTIONS
## Hm, it says write a FUNCTION that takes a STRING and then PRINTS stuff (instead of returning something).
## I also know that I need to import tools.py, write a function, and a main, in that order

# IMPORTS
from tools import *  # make note of the three ways to import a module
 

# FUNCTIONS
# word_centipede()
# notice that my arguments and names are descriptive
# notice that I'm printing out the argument (phrase) that I'm passing to test that my function is set up properly
def word_centipede(word):

	print(word)

# MAIN BODY OF PROGRAM
#main
entry = input("Please enter a phrase: ")
word_centipede(entry)

"""
OUTPUT:
>>> Please enter a phrase: message
message
"""
## YES! Our function is working.. now to figure out what the heck we do next.
## In Step 1, I set up the sections for my program, and handled what my INPUT will be (from the user), 
## what will do my PROCESSING (my function in this case), and my OUTPUT (printing).

## Basic plan. I'm either writing this down on paper or in comments.
"""
Get a phrase from the user
Call a function giving it that phrase
Loop through character by character
	Make each character doubled with a space between
	Print it out with dashes on either side
"""

## More specfic plan. This is the algoritm from class.
# Notice that now we've added in some of the details like doing a global import for tools
# And that the structure is not top to bottom, but based on where the sections of my program will live
# Plus indenting for when I want to group code together
"""
Import the tools file using a global import

Define a function that takes a string
    Walk through the string character by character
        Make a ‘segment’ out of each character doubled
        Print whatever dasher3 gives you on each segment

In the main section of your code,
Get a phrase from the user
Call your function on that phrase
"""

# The basic plan is probably enough to get started.. but practice writing out what is called "pseudocode" to think through the logic.

