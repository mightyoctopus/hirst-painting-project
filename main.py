from turtle import Turtle, Screen
from rgb_color_extractor import RgbColorExtractor

# get_rgb = RgbColorExtractor()
# result = get_rgb.extract_rgb_properties("hirst-painting.jpg", 30)
# print(result)

# # the result holds the RGB color sets.
# # So it can be used like color_list = result down below.
color_list = [ (232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

t = Turtle()
screen = Screen()
screen.colormode(255)

dot_size = 15
gap = 30
dots_per_row = 10


def draw_row(start_index):
    for i in range(dots_per_row):
        color = color_list[(start_index + i) % len(color_list)]
        t.dot(dot_size, color)
        t.penup()
        t.forward(gap)

def move_to_next_row():
    t.left(90)
    t.forward(gap)
    t.left(90)
    t.forward(300)
    t.left(180)

for index in range(0, dots_per_row * 10, dots_per_row):
    draw_row(index)
    move_to_next_row()
    print("INDEX: ", index)


screen.exitonclick()



"""
So that's going to be 10 along this side and 10 along this side.
Each of your dots should be around 20 in size and spaced apart by around 50
"""





