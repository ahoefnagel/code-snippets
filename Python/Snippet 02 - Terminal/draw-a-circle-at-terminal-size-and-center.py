# Our imports, OS, for cleaning the window, shutil for the shell utils
import shutil
import os
# Get the width and height of the terminal screen
columns, rows = shutil.get_terminal_size()

# Create an empty string that will draw to the screen
s = ""

for y in range(rows):
    for x in range(columns-1):
        # Check if the power of the half of the offset of x plus the half of the offset of y is less than the radius we want
        # This is acchieved with the Pythagorean Theorem
        if (columns//2-x)**2 + (rows//2-y)**2 < (rows//2)**2:
            s += '*'
        else:
            s += ' '
    # Draw a new line
    s += '\n'

# Clear the screen and draw the circle
os.system('cls' if os.name == 'nt' else 'clear')
print(s)
