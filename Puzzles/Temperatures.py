'''..........GIVEN..........
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(n)
'''

# ..........SOLUTION..........
import sys

closest = sys.maxsize  # a variable to compare and store (biggest size number)
# the number of temperatures to analyse (this is the first input )
n = int(input())
if n == 0:  # Check if there are no temperatues
    print(0)  # If True print 0
else:  # If there are temperatures
    for i in input().split():  # This is the second input. Loop through the list (a string of numbers)
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if abs(t) < abs(closest):  # Look if t is smaller than current smallest (not sign specific)
            closest = t  # If True make the new smallest t
        elif abs(t) == abs(closest):  # If the numbers are the same
            # Look if the origional number temp is bigger (looking for positive)
            if t > closest:
                closest = t  # If true then make the positive the closest
    print(closest)
