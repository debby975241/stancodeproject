"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The breakout game will start after the player clicks the mouse.
The ball will bounce back everytime it hit the wall or anything else except the bottom of the window.
When the ball hits the brick, that brick will be removed from the window.
If the ball hits the bottom of the window, it will lose one life.
The game will end when losing all the lives the player has or when there's no brick remain.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120                         # 120 frames per second
NUM_LIVES = 3			                        # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        if graphics.start:                      # when the mouse is clicked
            # pause(FRAME_RATE)
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())

            # when the ball hit the brick
            if graphics.ball_hit_brick():
                graphics.set_dy(-graphics.get_dy())   # the ball bounce at the opposite direction (y coordinate)
                graphics.brick_number -= 1            # the remaining brick number
                if graphics.brick_number == 0:        # if there's no brick remain
                    graphics.reset_ball()             # the ball go to its original position
                    break                             # end the game

            # when the ball hit the paddle
            if graphics.ball_hit_paddle():
                if graphics.get_dy() > 0:
                    graphics.set_dy(-graphics.get_dy())

            # when the ball hit the left or right side of the window
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get_dx())

            # when the ball hit the ground(the bottom of the window
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                if lives > 0:                        # when there are still lives remain
                    graphics.reset_ball()
                    graphics.start = False
                else:                                # when there's no life remain
                    break                            # end the game

            # when the ball hit the top of the window
            elif graphics.ball.y <= 0:
                graphics.set_dy(-graphics.get_dy())
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
