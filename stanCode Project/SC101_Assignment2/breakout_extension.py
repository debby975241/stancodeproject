"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The breakout game will start after the player clicks the mouse.
The ball will bounce back everytime it hits the wall or anything else except the bottom of the window.
When the ball hits the brick, that brick will be removed from the window.
The player can get points by hitting and removing the bricks.
The ball will bounce faster when hitting certain numbers of the bricks.
If the ball hits the bottom of the window, it will lose one life.
The game will end when losing all the lives the player has or when there's no brick remain.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 1000 / 120                          # 120 frames per second
NUM_LIVES = 3			                         # Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_dx()                       # get the x speed of the ball from the class breakoutgraphics
    dy = graphics.get_dy()                       # get the y speed of the ball from the class breakoutgraphics
    graphics.lives_num = NUM_LIVES               # reassign the lives_num according to the constant
    graphics.draw_lives_heart()                  # draw the lives the player would have
    graphics.introduction()
    pause(3000)
    graphics.remove_introduction()
    graphics.click_to_start()
    pause(1000)
    graphics.remove_click_to_start()
    # The animation loop here
    while True:
        if graphics.start:                       # when the mouse is clicked
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)

            # when the ball hit the brick
            if graphics.ball_hit_brick():
                graphics.score_num += 1          # get one point everytime hitting the brick
                graphics.score.text = "Score: " + str(graphics.score_num)
                graphics.remove_brick()          # remove the brick that the ball hit
                dy = -dy                         # the ball bounce at the opposite direction (y coordinate)
                graphics.brick_number -= 1       # the remaining brick number

                if graphics.score_num > (graphics.brick_rows*graphics.brick_cols)/4:
                    # to speed after hitting 1/4 of the bricks
                    dx += 0.3
                    dy += 0.2

                if graphics.brick_number == 0:   # if there's no brick remain
                    graphics.winning_the_game()  # tell the player he or she win the game
                    break                        # end the game

            # when the ball hit the paddle
            if graphics.ball_hit_paddle():
                dy = -dy

            # when the ball hit the left or right side of the window
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                dx = -dx

            # when the ball hit the ground(the bottom of the window
            if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                graphics.lives_num -= 1
                graphics.remove_lives_heart()

                if graphics.lives_num > 0:      # when there are still lives remain
                    graphics.reset_ball()
                    graphics.start = False
                else:                           # when there's no life remain
                    graphics.losing_the_game()
                    break                       # end the game

            # when the ball hit the top of the window
            elif graphics.ball.y <= 0:
                dy = -dy
        pause(FRAME_RATE)





    # Add animation loop here!


if __name__ == '__main__':
    main()
