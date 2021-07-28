"""
File: bouncing_ball.py
Name: Debby Chang
-------------------------
To make a ball bouncing after the mouse-click.
The ball will only start bouncing after it bounces outside the window and gets back to the original position.
The bouncing can only start three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

# the Global variable I set
time = 0                                             # the time of ball finishing bouncing the whole turn
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce_the_ball)


def bounce_the_ball(mouse):
    """
    :param mouse: (mouseEvent) Everytime the mouse is clicked, the ball will bounce. And if the ball finishing bouncing,
                               it will return back to the start position waiting for the next click.
                               The bouncing will only start when it's at the original position.
    """
    global time
    vy = 0
    if ball.x == START_X and ball.y == START_Y:
        # ball only starts bouncing when it's at the original place, the clicking during the bouncing won't affect it.
        time += 1                                   # reassign the time to plus one after the ball starts bouncing
        while time <= 3 and ball.x <= window.width:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+ball.height >= window.height:  # when the ball hits the bottom of the window (ground)
                vy = -vy*REDUCE
            pause(DELAY)

        window.add(ball, START_X, START_Y)
        # the ball gets back to the original place after bouncing outside the window


if __name__ == "__main__":
    main()
