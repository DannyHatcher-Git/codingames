''' ..........GIVEN..........
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print("SE")

'''
# ..........SOLUTION..........
# Note the diagram doesn't make much sense with the direction.
# The compass is misleading, as you start at top left you are 0,0
# and forward for the character is north which is negative y

target_x, target_y, start_tx, start_ty = [int(i) for i in input().split()]

# game loop
while 1:  # Every turn the loop starts again
    remaining_turns = int(input())  # This can't be removed

    direction_x = ""  # Storing the direction for this turn
    direction_y = ""  # Storing the direction for this turn

    # If the start is bigger the x needs to go down (West)
    if start_tx > target_x:
        direction_x = "W"  # Giving directions
        start_tx -= 1  # Updating position for the next round
    # If the start is smaller the x needs to go up (East)
    elif start_tx < target_x:
        direction_x = "E"  # Giving directions
        start_tx += 1  # Updating position for the next round

    # If the start is bigger the y needs to go down (South)
    if start_ty > target_y:
        direction_y = "N"  # Giving directions
        start_ty -= 1  # Updating position for the next round
    # If the start is bigger the y needs to go up (North)
    elif start_ty < target_y:
        direction_y = "S"  # Giving directions
        start_ty += 1  # Updating position for the next round

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction_y + direction_x)
