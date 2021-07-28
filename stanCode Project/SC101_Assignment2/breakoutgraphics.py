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
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
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
                    self.bricks.color = self.bricks.fill_color = 'red'
                elif 1 < j <= 3:              # row 3 to row 4
                    self.bricks.color = self.bricks.fill_color = 'orange'
                elif 3 < j <= 5:              # row 5 to row 6
                    self.bricks.color = self.bricks.fill_color = 'yellow'
                elif 5 < j <= 7:              # row 7 to row 8
                    self.bricks.color = self.bricks.fill_color = 'green'
                elif 7 < j <= 9:              # row 9 to row 10
                    self.bricks.color = self.bricks.fill_color = 'blue'
                else:                         # row after row 10
                    self.bricks.color = self.bricks.fill_color = 'cornflowerblue'
                self.window.add(self.bricks)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:             # so there's half chance for the ball to bounce at the opposite direction
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        self.paddle_offset = paddle_offset

        # count the original brick number
        self.brick_number = brick_rows * brick_cols

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

    def set_dx(self, new_dx):
        """
        Setter: Assign the new __dx to the self.__dx
        :param new_dx: a new velocity of x-direction.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Setter: Assign the new __dx to the self.__dy
        :param new_dy: a new velocity of y-direction.
        """
        self.__dy = new_dy

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
        # the upper left side of the ball
        b_upleft = self.window.get_object_at(self.ball.x, self.ball.y)
        # the upper right side of the ball
        b_upright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        # the lower-left side of the ball
        b_lowerleft = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
        # the lower-right side of the ball
        b_lowerright = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

        # the upper left side of the ball hit the brick but not the paddle
        if b_upleft is not None and b_upleft is not self.paddle:
            self.window.remove(b_upleft)
            return True
        # the upper right side of the ball hit the brick but not the paddle
        elif b_upright is not None and b_upright is not self.paddle:
            self.window.remove(b_upright)
            return True
        # the lower left side of the ball hit the brick but not the paddle
        elif b_lowerleft is not None and b_lowerleft is not self.paddle:
            self.window.remove(b_lowerleft)
            return True
        # the lower right side of the ball hit the brick but not the paddle
        elif b_lowerright is not None and b_lowerright is not self.paddle:
            self.window.remove(b_lowerright)
            return True

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
        if b_upleft is not None and b_upleft is self.paddle:
            return True
        # the upper right side of the ball hit the paddle
        elif b_upright is not None and b_upright is self.paddle:
            return True
        # the lower left side of the ball hit the paddle
        elif b_lowerleft is not None and b_lowerleft is self.paddle:
            return True
        # the lower right side of the ball hit the paddle
        elif b_lowerright is not None and b_lowerright is self.paddle:
            return True
