# Brenden Lawlor
# 09/18/21
# Chapter 5 Assignment

# Turtle Graphics

# This program lets the user pick a size and color preset and then draws a chess board based off
# their selections.

import turtle

# Board size needs to be large enough to see and be divisible by 8
board_size_choices = ['200', '400', '800']

print("\nThis program will draw a Chess/Checker board to"
      " the size and colors you decide.")

print("You will be able to pick from 3 sizes and 4 color schemes.")

# Loop until user selects a valid board size
board_size = 1
while board_size not in board_size_choices:
    print("\nSize choices: "
          f"{board_size_choices[0]}, {board_size_choices[1]}, {board_size_choices[2]}")
    board_size = input("\nPlease enter a board size: ")
    if board_size not in board_size_choices:
        print("You did not enter a valid board size. Please try again.")

# Sets the appropiate x and y sizes of the board. In hindsight this program probably could have been
# completed with just one of these 2 variables, but this works as well.
if board_size == '200':
    y_size = 200
    x_size = 200
elif board_size == '400':
    y_size = 400
    x_size = 400
elif board_size == '800':
    y_size = 800
    x_size = 800

# These are the color presets availabe in this program. For some reason the 'brown' color from turtle
# actually looks red, so I had to change this to reflect that.
color_presets = [
    'Black and White',
    'Tan and White',
    'Red and Tan',
    'Gray and White'
]

# Since user just enters a number 1 - 4, I needed a way to check if they entered a valid number.
# This list was the solution I came up with.
one_thru_four = ['1', '2', '3', '4']

# Loop until user selects a valid number corresponding to a color scheme
color_scheme = ''
while color_scheme not in one_thru_four:
    print(f"\nColor Schemes:\n\t1 = {color_presets[0]} \n\t2 = {color_presets[1]}"
          f"\n\t3 = {color_presets[2]} \n\t4 = {color_presets[3]}")
    color_scheme = input(
        "\nPlease pick a choice from the color presets above: ")
    if color_scheme not in one_thru_four:
        print("You did not enter a valid number. Please try again.")

# Sets the color of the light and dark squares based off of the users choice
if color_scheme == '1':
    dark_color = 'black'
    light_color = 'white'
elif color_scheme == '2':
    dark_color = 'tan'
    light_color = 'white'
elif color_scheme == '3':
    dark_color = 'brown'
    light_color = 'tan'
elif color_scheme == '4':
    dark_color = 'gray'
    light_color = 'white'

# Prompt user to look at the new pop up window that they probably didn't notice opening up
print("\nPlease see Python Turtle Graphic application.")

# Now for the fun part. Actually drawing the chess board. This turned out to be much more
# difficult than I was expecting. The main issue I was having was filling in the color for
# every other square. The only way I could think to do it was to fill the whole board with the
# light color in the very beginning, and then fill in each individual dark square.
my_pen = turtle.Pen()
my_pen.up()
# moving the turtle to the position that will allow the board to be centered
my_pen.goto(-x_size / 2, -y_size / 2)
my_pen.down()
my_pen.color(dark_color)  # Making sure there is an outline

my_pen.fillcolor(light_color)
my_pen.begin_fill()

# Draws a square based on selected board size
for outer_square in range(4):
    my_pen.forward(y_size)
    my_pen.left(90)
my_pen.end_fill()

my_pen.color(dark_color)

# Draws the squares for the odd rows. The only way I could make out to do this
# was to use 2 nested for loops. One to control the location of each row, one to control
# the location of each individual square in each individual row, and one to control the actual
# drawing of the square. As the x or y coordinate updates at the end of each loop,
# I am able to use them later to determine where to ultimately move the Turtle.
for y_coordinate in range(-x_size, y_size, int(y_size / 2)):
    for x_coordinate in range(-x_size, y_size, int(y_size / 2)):
        my_pen.begin_fill()
        my_pen.up()
        # No clue why I needed to divide these by 2, just know that it made it work lol
        my_pen.goto(x_coordinate / 2, y_coordinate / 2)
        my_pen.down()

        # After the position of the square has been determined, this actually draws the squares
        for dark_square in range(4):
            my_pen.forward(y_size / 8)
            my_pen.left(90)

        my_pen.end_fill()

# Does the same as above, but moves the inital starting point of each row to the right one square
# and operates only on the even rows
for y_coordinate in range(int(-(3 * x_size) / 4), y_size, int(y_size / 2)):
    for x_coordinate in range(int(-(3 * x_size) / 4), y_size, int(y_size / 2)):
        my_pen.begin_fill()
        my_pen.up()
        my_pen.goto(x_coordinate / 2, y_coordinate / 2)
        my_pen.down()

        for dark_square in range(4):
            my_pen.forward(y_size / 8)
            my_pen.left(90)
        my_pen.end_fill()

# Hides the turtle once finished and waits the user to close the window
my_pen.ht()
turtle.exitonclick()
