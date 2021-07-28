"""
File: my_drawing.py
Name: Debby Chang
----------------------
To create a picture with GOval, GRect, GPolygon, GLine, adn GLabel
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Finally have the chance to know more about Class and object!
    So I create a minion that represents object in stanCode.
    Just want to say hi to this cute minion and hope I can get along well with him in SC101 lol.
    """
    window = GWindow(width=670, height=650, title='Minion Sticker')

    # the left hair
    hair_1 = GLine(275, 120, 290, 170)
    hair_1.color = 'black'
    window.add(hair_1)

    # the middle hair
    hair_2 = GLine(330, 100, 332, 170)
    hair_2.color = 'black'
    window.add(hair_2)

    # the right hair
    hair_3 = GLine(390, 120, 360, 170)
    hair_3.color = 'black'
    window.add(hair_3)

    # the head
    head = GOval(200, 200, x=230, y=150)
    head.filled = True
    head.fill_color = 'yellow'
    head.color = 'yellow'
    window.add(head)

    # the overalls
    pants = GOval(200, 200, x=230, y=320)
    pants.filled = True
    pants.fill_color = 'cornflowerblue'
    pants.color = 'cornflowerblue'
    window.add(pants)

    # the body
    body = GRect(200, 200, x=230, y=230)
    body.filled = True
    body.fill_color = 'yellow'
    body.color = 'yellow'
    window.add(body)

    # the pocket of the overalls
    pocket = GRect(120, 80, x=270, y=380)
    pocket.filled = True
    pocket.fill_color = 'cornflowerblue'
    pocket.color = 'cornflowerblue'
    window.add(pocket)

    # the left sling of the overalls
    l_sling = GPolygon()
    l_sling.add_vertex((230, 350))
    l_sling.add_vertex((270, 380))
    l_sling.add_vertex((270, 400))
    l_sling.add_vertex((230, 370))
    l_sling.filled = True
    l_sling.fill_color = 'cornflowerblue'
    l_sling.color = 'cornflowerblue'
    window.add(l_sling)

    # the right sling of the overalls
    r_sling = GPolygon()
    r_sling.add_vertex((390, 380))
    r_sling.add_vertex((430, 350))
    r_sling.add_vertex((430, 370))
    r_sling.add_vertex((390, 400))
    r_sling.filled = True
    r_sling.fill_color = 'cornflowerblue'
    r_sling.color = 'cornflowerblue'
    window.add(r_sling)

    # the left upper limb
    l_uphand = GPolygon()
    l_uphand.add_vertex((185, 390))
    l_uphand.add_vertex((230, 373))
    l_uphand.add_vertex((230, 388))
    l_uphand.add_vertex((185, 400))
    l_uphand.filled = True
    l_uphand.fill_color = 'yellow'
    l_uphand.color = 'yellow'
    window.add(l_uphand)

    # the left lower limb
    l_lowhand = GPolygon()
    l_lowhand.add_vertex((185, 390))
    l_lowhand.add_vertex((230, 425))
    l_lowhand.add_vertex((230, 440))
    l_lowhand.add_vertex((185, 400))
    l_lowhand.filled = True
    l_lowhand.fill_color = 'yellow'
    l_lowhand.color = 'yellow'
    window.add(l_lowhand)

    # the right upper limb
    r_uphand = GPolygon()
    r_uphand.add_vertex((430, 373))
    r_uphand.add_vertex((475, 390))
    r_uphand.add_vertex((475, 400))
    r_uphand.add_vertex((430, 388))
    r_uphand.filled = True
    r_uphand.fill_color = 'yellow'
    r_uphand.color = 'yellow'
    window.add(r_uphand)

    # the right lower limb
    r_lowhand = GPolygon()
    r_lowhand.add_vertex((430, 425))
    r_lowhand.add_vertex((475, 390))
    r_lowhand.add_vertex((475, 400))
    r_lowhand.add_vertex((430, 440))
    r_lowhand.filled = True
    r_lowhand.fill_color = 'yellow'
    r_lowhand.color = 'yellow'
    window.add(r_lowhand)

    # the left button on the overalls
    l_button = GOval(10, 10, x=270, y=385)
    l_button.filled = True
    window.add(l_button)

    # the right button on the overalls
    r_button = GOval(10, 10, x=380, y=385)
    r_button.filled = True
    window.add(r_button)

    # the left frame of the glasses
    l_frame = GRect(43, 25, x=230, y=240)
    l_frame.filled = True
    window.add(l_frame)

    # the right frame of the glasses
    r_frame = GRect(43, 25, x=387, y=240)
    r_frame.filled = True
    window.add(r_frame)

    # the glasses
    glasses = GOval(120, 120, x=270, y=190)
    glasses.filled = True
    glasses.fill_color = 'gray'
    glasses.color = 'gray'
    window.add(glasses)

    # the white eye
    white_eye = GOval(100, 100, x=280, y=200)
    white_eye.filled = True
    white_eye.fill_color = 'white'
    white_eye.color = 'white'
    window.add(white_eye)

    # the black eye
    black_eye = GOval(65, 65, x=300, y=220)
    black_eye.filled = True
    black_eye.fill_color = 'black'
    black_eye.color = 'black'
    window.add(black_eye)

    # the mouth
    mouth = GOval(100, 50, x=280, y=312)
    mouth.filled = True
    window.add(mouth)

    # the oval that covers the mouth to make the shape of mouse
    x_mouth = GOval(110, 35, x=280, y=311)
    x_mouth.color = 'yellow'
    x_mouth.filled = True
    x_mouth.fill_color = 'yellow'
    window.add(x_mouth)

    # the first left blush of the left blush
    l_blush1 = GLine(240, 300, 245, 315)
    l_blush1.color = 'deeppink'
    window.add(l_blush1)

    # the middle blush of the left blush
    l_blush2 = GLine(250, 300, 255, 315)
    l_blush2.color = 'deeppink'
    window.add(l_blush2)

    # the right blush of the left blush
    l_blush3 = GLine(260, 300, 265, 315)
    l_blush3.color = 'deeppink'
    window.add(l_blush3)

    # the first left blush of the right blush
    r_blush1 = GLine(395, 300, 400, 315)
    r_blush1.color = 'deeppink'
    window.add(r_blush1)

    # the middle blush of the right blush
    r_blush2 = GLine(405, 300, 410, 315)
    r_blush2.color = 'deeppink'
    window.add(r_blush2)

    # the right blush of the right blush
    r_blush3 = GLine(415, 300, 420, 315)
    r_blush3.color = 'deeppink'
    window.add(r_blush3)

    # the left leg
    l_leg = GPolygon()
    l_leg.add_vertex((275, 500))
    l_leg.add_vertex((315, 500))
    l_leg.add_vertex((310, 530))
    l_leg.add_vertex((280, 530))
    l_leg.color = "cornflowerblue"
    l_leg.filled = True
    l_leg.fill_color = "cornflowerblue"
    window.add(l_leg)

    # the right leg
    r_leg = GPolygon()
    r_leg.add_vertex((335, 500))
    r_leg.add_vertex((380, 500))
    r_leg.add_vertex((375, 530))
    r_leg.add_vertex((345, 530))
    r_leg.color = "cornflowerblue"
    r_leg.filled = True
    r_leg.fill_color = "cornflowerblue"
    window.add(r_leg)

    # the left shoe
    l_shoe = GRect(30, 20, x=280, y=530)
    l_shoe.filled = True
    l_shoe.fill_color = 'black'
    l_shoe.color = 'black'
    window.add(l_shoe)

    # the right shoe
    r_shoe = GRect(30, 20, x=345, y=530)
    r_shoe.filled = True
    r_shoe.fill_color = 'black'
    r_shoe.color = 'black'
    window.add(r_shoe)

    # the left foot
    l_feet = GOval(30, 20, x=264, y=530)
    l_feet.filled = True
    l_feet.fill_color = 'black'
    l_feet.color = 'black'
    window.add(l_feet)

    # the right foot
    r_feet = GOval(30, 20, x=360, y=530)
    r_feet.filled = True
    r_feet.fill_color = 'black'
    r_feet.color = 'black'
    window.add(r_feet)

    # the words show on the overalls
    stancode = GLabel('stanCode')
    stancode.color = 'white'
    stancode.font = '-20'
    window.add(stancode, 290, 420)

    # the greeting words!
    label = GLabel('Hi!')
    label.color = 'black'
    label.font = 'Dialog-50-bold-italic'
    window.add(label, 450, 220)


if __name__ == '__main__':
    main()
