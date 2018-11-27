"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Michael Johnson.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

window.tracer(200)

bohdan = rg.SimpleTurtle()
bohdan.pen = rg.Pen('yellow', 5)
bohdan.speed = 8
bohdan.forward(10)

for k in range(250):
    bohdan.draw_circle(k+20)
    bohdan.left(10)
    bohdan.forward(10)

michael = rg.SimpleTurtle()
michael.pen = rg.Pen('red', 4)
michael.speed = 15

size = 200

for k in range(250):
    michael.draw_square(size)
    michael.pen_up()
    michael.forward(20)
    michael.right(45)

    michael.pen_down()
    size = size - 5

window.close_on_mouse_click()









