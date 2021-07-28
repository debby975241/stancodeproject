"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Recursively print the sierpinski according to the order number in constants.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of the triangle has
	:param length: the length of the triangle
	:param upper_left_x: the x coordinate of the first triangle
	:param upper_left_y: the y coordinate of the first triangle
	:return: the sierpinski triangle
	"""
	if order == 0:		    # base case
		return
	else:
		# the first triangle
		# the left side of the triangle
		left_side = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		# the upper side of the triangle
		up_side = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		# the right side of the triangle
		right_side = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)

		window.add(left_side)
		window.add(up_side)
		window.add(right_side)

		# below are the order-1 triangles
		# the upper left order-1 triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# the upper right order-1 triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# the lower order-1 triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length*0.5*0.5, upper_left_y+length*0.866*0.5)


if __name__ == '__main__':
	main()
