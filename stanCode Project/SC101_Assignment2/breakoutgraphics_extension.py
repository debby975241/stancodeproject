"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Including all the class, objects, methods and attributes that the breakout game needs.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'darkgrey'
        self.paddle.color = 'darkgray'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'darkgray'
        self.ball.color = 'darkgray'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Initialize our mouse listeners
        onmousemoved(self.paddle_moving)
        onmouseclicked(self.start_playing)
        self.start = False                    # Control the opening of the mouseclicked event

        # Draw bricks
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height, x=0+(brick_width*i)+(brick_spacing*i),
                                    y=brick_offset+(brick_height+brick_spacing)*j)
                self.bricks.filled = True
                if j <= 1:                    # row 1 to row 2
                    self.bricks.color = self.bricks.fill_color = 'pink'
                elif 1 < j <= 3:              # row 3 to row 4
                    self.bricks.color = self.bricks.fill_color = 'cornflowerblue'
                elif 3 < j <= 5:              # row 5 to row 6
                    self.bricks.color = self.bricks.fill_color = 'lightcoral'
                elif 5 < j <= 7:              # row 7 to row 8
                    self.bricks.color = self.bricks.fill_color = 'mediumpurple'
                elif 7 < j <= 9:              # row 9 to row 10
                    self.bricks.color = self.bricks.fill_color = 'royalblue'
                else:                         # row after row 10
                    self.bricks.color = self.bricks.fill_color = 'cornflowerblue'
                self.window.add(self.bricks)

        # Draw the scoreboard
        self.score = GLabel('Score: 0')
        self.score.font = '-25'
        self.score_num = 0
        self.window.add(self.score, x=0, y=window_height)

        # Draw the number of the live remaining
        self.lives_num = 3

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:             # so there's half chance for the ball to bounce at the opposite direction
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        self.paddle_offset = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # count the original brick number
        self.brick_number = self.brick_rows * self.brick_cols

    def get_dx(self):
        """
        To get the current x speed of the ball
        :return: the x speed of the ball
        """
        return self.__dx

    def get_dy(self):
        """
        To get the current y speed of the ball
        :return: the y speed of the ball
        """
        return self.__dy

    def start_playing(self, mouse):
        """
        (mouseEvent) click the mouse to let the ball start bouncing
        """
        self.start = True

    def reset_ball(self):
        """
        To let the ball appear at the original starting position
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def paddle_moving(self, mouse):
        """
        (mouseEvent) The center of the paddle will follow the mouse
        """
        # when the paddle is in the window
        if 0 + self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width / 2

        # when the paddle is about to leave the left side of the window
        elif mouse.x < 0 + self.paddle.width/2:
            self.paddle.x = 0

        # when the paddle is about to leave the right side of the window
        elif mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width

        # the paddle's y coordinate will always be at the same as below
        self.paddle.y = self.window.height - self.paddle_offset

    def ball_hit_brick(self):
        """
        :return: if any of the four corner of the ball hit the brick
        """
        if self.ball.y < self.window.height-self.paddle_offset:
            # the upper left side of the ball
            b_upleft = self.window.get_object_at(self.ball.x, self.ball.y)
            # the upper right side of the ball
            b_upright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
            # the lower-left side of the ball
            b_lowerleft = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
            # the lower-right side of the ball
            b_lowerright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

            # the upper left side of the ball hit the brick but not the paddle
            upleft_hit = b_upleft is not None and b_upleft is not self.paddle and b_upleft is not self.score
            # the upper right side of the ball hit the brick but not the paddle
            upright_hit = b_upright is not None and b_upright is not self.paddle and b_upright is not self.score
            # the lower left side of the ball hit the brick but not the paddle
            lowerleft_hit = b_lowerleft is not None and b_lowerleft is not self.paddle and b_lowerleft is not self.score
            # the lower right side of the ball hit the brick but not the paddle
            lowerright_hit = b_lowerright is not None and b_lowerright is not self.paddle \
                             and b_lowerright is not self.score
            return upleft_hit or upright_hit or lowerleft_hit or lowerright_hit

    def ball_hit_paddle(self):
        """
        :return: if any of the four corner of the ball hit the paddle
        """
        # the upper left side of the ball
        b_upleft = self.window.get_object_at(self.ball.x, self.ball.y)
        # the upper right side of the ball
        b_upright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        # the lower-left side of the ball
        b_lowerleft = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
        # the lower-right side of the ball
        b_lowerright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

        # the upper left side of the ball hit the paddle
        upleft_hit = b_upleft is not None and b_upleft is self.paddle
        # the upper right side of the ball hit the paddle
        upright_hit = b_upright is not None and b_upright is self.paddle
        # the lower left side of the ball hit the paddle
        lowerleft_hit = b_lowerleft is not None and b_lowerleft is self.paddle
        # the lower right side of the ball hit the paddle
        lowerright_hit = b_lowerright is not None and b_lowerright is self.paddle
        return upleft_hit or upright_hit or lowerleft_hit or lowerright_hit

    def remove_brick(self):
        """
        remove the brick when the ball hit the brick but not the paddle
        """
        b_upleft = self.window.get_object_at(self.ball.x, self.ball.y)
        b_upright = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        b_lowerleft = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        b_lowerright = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)
        if b_upleft is not None and b_upleft is not self.paddle:
            self.window.remove(b_upleft)
        elif b_upright is not None and b_upright is not self.paddle:
            self.window.remove(b_upright)
        elif b_lowerleft is not None and b_lowerleft is not self.paddle:
            self.window.remove(b_lowerleft)
        elif b_lowerright is not None and b_lowerright is not self.paddle:
            self.window.remove(b_lowerright)

    def winning_the_game(self):
        """
        When winning the game, add 'You Win!!' on the window.
        """
        win = GLabel('You Win!!!')
        win.font = '-50'
        self.window.add(win, x=self.window.width/2 - 115, y=self.window.height/2)

    def losing_the_game(self):
        """
        When winning the game, add 'You Lose :(' on the window.
        """
        lose = GLabel('You Lose :(')
        lose.font = '-70'
        self.window.add(lose, x=self.window.width/2 - 160, y=self.window.height/2 + 50)

    def draw_lives_heart(self):
        """
        Drawing balls that indicate the lives the player still has.
        """
        for i in range(self.lives_num):
            heart = GOval(20, 20, x=self.window.width - 25 * (i + 1), y=self.window.height - 25)
            heart.color = 'pink'
            heart.filled = True
            heart.fill_color = 'pink'
            self.window.add(heart)

    def remove_lives_heart(self):
        """
        Remove the live ball one at a time when losing one life.
        """
        heart_remove = self.window.get_object_at(x=self.window.width-24*(self.lives_num+1), y=self.window.height - 12.5)
        self.window.remove(heart_remove)

    def introduction(self):
        """
        Welcome the player by saying Welcome to stanCode Breakout Game!! on the window.
        """
        self.welcome1 = GLabel('Welcome to stanCode')
        self.welcome2 = GLabel('Breakout Game!!')
        self.welcome1.font = '-35'
        self.welcome2.font = '-35'
        self.window.add(self.welcome1, x=self.window.width/2 - 160, y=self.window.height/2 + 50)
        self.window.add(self.welcome2, x=self.window.width/2 - 160, y=self.window.height/2 + 100)

    def remove_introduction(self):
        """
        Remove the introduction words.
        """
        self.window.remove(self.welcome1)
        self.window.remove(self.welcome2)

    def click_to_start(self):
        """
        Tell the player to click by saying "Click to Start :)" on the window.
        """
        self.click_to_start = GLabel('Click to Start :)')
        self.click_to_start.font = '-35'
        self.window.add(self.click_to_start, x=(self.window.width) / 2 - 100, y=(self.window.height) / 2 + 100)

    def remove_click_to_start(self):
        """
        Remove the instruction of 'click to start :)'.
        """
        self.window.remove(self.click_to_start)
