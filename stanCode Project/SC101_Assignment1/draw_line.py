"""
File: draw_line.py
Name: Debby Chang
-------------------------
To create line with every two clicks.
The first click makes a circle with the click as the center of the circle.
The second click makes a line from the center of the circle to the position of the second mouse-click.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 10                             # This constant controls the size of the circle

# Global variable
window = GWindow()

# The Global variable I set
num_click = 0                         # the number of the click
circle = GOval(SIZE, SIZE)
circle_x = 0                          # the x coordinate of the circle
circle_y = 0                          # the y coordinate of the circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global num_click, circle, circle_x, circle_y
    circle.filled = False
    num_click += 1                    # reassign the number of the click after every mouse-clicking

    if num_click % 2 != 0:            # the odd click
        circle_x = mouse.x - SIZE//2  # reassign the x coordinate of the circle after the odd click
        circle_y = mouse.y - SIZE//2  # reassign the y coordinate of the circle after the odd click
        window.add(circle, circle_x, circle_y)

    else:                             # the even click
        line = GLine(circle_x+SIZE//2, circle_y+SIZE//2, mouse.x, mouse.y)
        # draw the line from the center of the circle to the mouse click
        window.add(line)
        window.remove(circle)


if __name__ == "__main__":
    main()
