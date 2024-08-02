
import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
tib = turtle_module.Turtle()
tib.speed("fastest")
tib.penup()
tib.hideturtle()
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),
              (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251),
              (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8),
              (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161),
              (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161),
              (10, 97, 62), (5, 38, 33), (68, 219, 155)]
tib.setheading(225)
tib.forward(300)
tib.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tib.dot(20, random.choice(color_list))
    tib.forward(50)

    if dot_count % 10 == 0:
        tib.setheading(90)
        tib.forward(50)
        tib.setheading(180)
        tib.forward(500)
        tib.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()


# colorgram extract color from image
# colors = colorgram.extract('spot_paint.jpg', 30)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

#[(249, 228, 17), (213, 13, 9), (198, 12, 35),
# (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
# (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222),
# (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
# (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]