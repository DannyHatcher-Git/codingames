'''..........GIVEN..........

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print("4")
'''
# .......... SOLUTION..........

while True:
    max = 0  # Max height of a mountain
    imax = 0  # The location in the list of the max height
    for i in range(8):  # Check through the list from 0-7
        # The input is made an integer and is the mountain_h
        mountain_h = int(input())
        if mountain_h > max:  # is the mountain height bigger than the current stored max
            max = mountain_h  # If true a new max is saved
            imax = i  # If true the location of the new height is stored
print(imax)  # The integer of location of the mountain in the list
