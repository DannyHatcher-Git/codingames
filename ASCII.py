'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
'''
# ..........SOLUTION ..........
w = int(input())  # width
h = int(input())  # height
t = input().lower()  # text needed lower to make comparison consistent

# find first character
for i in range(h):  # going through heigh 0-5 (rows)
    row = input()  # font input
    for char in t:
        if not char.isalpha():
            offset = 26*w
        else:
            # find ASCII order of first letter and take number away from a then multiply by width
            offset = (ord(char)-ord("a"))*w
        # row (number: number). First offset is the first part of the font taken, then add width. end="" (print everything in one line)
        print(row[offset:offset+w], end="")
    print("")
