#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(800, 600, "Smiley Face Example")
arcade.set_background_color(open_color.white)
# Start the render process. This must be done before any drawing commands.
arcade.start_render()

face_x,face_y = (600,600)

# Draw the smiley face:
# (x,y,radius,color)
arcade.draw_circle_filled(300, 300, 200, open_color.yellow_3)
# (x,y,radius,color,border_thickness)
arcade.draw_circle_outline(300 + 0, 300 + 0, 200, open_color.black, 4)

#(x,y,width,height,color)
arcade.draw_ellipse_filled(370 + 0, 350 + 0, 50, 100, open_color.black)
arcade.draw_ellipse_filled(230 + 0, 350 + 0, 50, 100, open_color.black)
arcade.draw_circle_filled(380 + 0, 370 + 0, 5, open_color.gray_2)
arcade.draw_circle_filled(240 + 0, 370 + 0, 5, open_color.gray_2)

#(x,y,width,height,color,start_degrees,end_degrees,border_thickness)
arcade.draw_arc_outline(300 + 0, 280 + 0, 120, 100, open_color.black, 190, 350, 5)



# Finish the render
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()
