import arcade

arcade.open_window(900, 700, "Desert")

#Set background color
arcade.set_background_color(arcade.color.ARYLIDE_YELLOW)

arcade.start_render()

# --- Draw the sky ---

#The sky
arcade.draw_lrtb_rectangle_filled(0, 900, 700, 400, arcade.color.AQUA)

#The sun
arcade.draw_circle_filled(800, 600, 50, arcade.color.YELLOW_ORANGE)

#The halos
arcade.draw_circle_outline(800, 600, 75, arcade.color.PALE_GOLD)
arcade.draw_circle_outline(800, 600, 100, arcade.color.PALE_GOLD)

#Cloud one
arcade.draw_ellipse_filled(200, 500, 200, 70, arcade.color.GRAY_BLUE)
arcade.draw_circle_filled(235, 525, 35, arcade.color.GRAY_BLUE)
arcade.draw_ellipse_filled(190, 540, 75, 130, arcade.color.GRAY_BLUE)
arcade.draw_circle_filled(160, 525, 35, arcade.color.GRAY_BLUE)

#Cloud two
arcade.draw_ellipse_filled(500, 600, 200, 70, arcade.color.GRAY_BLUE)
arcade.draw_circle_filled(535, 625, 35, arcade.color.GRAY_BLUE)
arcade.draw_ellipse_filled(490, 640, 75, 130, arcade.color.GRAY_BLUE)
arcade.draw_circle_filled(460, 625, 35, arcade.color.GRAY_BLUE)


#--- The plants and rocks ---

#Cactus one
arcade.draw_lrtb_rectangle_filled(200, 250, 335, 100, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(125, 250, 250, 225, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(125, 150, 275, 225, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(250, 310, 225, 200, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(285, 310, 275, 225, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(225, 335, 25, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(137.5, 275, 12.5, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(297.5, 275, 12.5, arcade.color.BANGLADESH_GREEN)

#Cactus two
arcade.draw_lrtb_rectangle_filled(500, 550, 435, 200, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(425, 550, 350, 325, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(425, 450, 375, 325, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(550, 610, 325, 300, arcade.color.BANGLADESH_GREEN)
arcade.draw_lrtb_rectangle_filled(585, 610, 375, 325, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(525, 435, 25, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(437.5, 375, 12.5, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(597.5, 375, 12.5, arcade.color.BANGLADESH_GREEN)

#Rock one
arcade.draw_lrtb_rectangle_filled(100, 150, 50, 45, arcade.color.BLACK_OLIVE)
arcade.draw_ellipse_filled(125, 50, 50, 10, arcade.color.BLACK_OLIVE)

#Rock two
arcade.draw_lrtb_rectangle_filled(400, 450, 100, 95, arcade.color.BLACK_OLIVE)
arcade.draw_ellipse_filled(425, 100, 50, 10, arcade.color.BLACK_OLIVE)

#Rock three
arcade.draw_lrtb_rectangle_filled(80, 130, 375, 370, arcade.color.BLACK_OLIVE)
arcade.draw_ellipse_filled(105, 375, 50, 10, arcade.color.BLACK_OLIVE)

#Rock four
arcade.draw_lrtb_rectangle_filled(700, 750, 305, 300, arcade.color.BLACK_OLIVE)
arcade.draw_ellipse_filled(725, 305, 50, 10, arcade.color.BLACK_OLIVE)

# --- Draw the Oasis ---

#The Shore
arcade.draw_ellipse_filled(900, 0, 900, 500, arcade.color.PALE_BROWN)

#The Oasis
arcade.draw_ellipse_filled(900, 0, 800, 400, arcade.color.BLUE_SAPPHIRE)


arcade.finish_render()

arcade.run()