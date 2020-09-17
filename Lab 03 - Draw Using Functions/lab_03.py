import arcade

arcade.open_window(900, 700, "Desert")

#Set background color
arcade.set_background_color(arcade.color.ARYLIDE_YELLOW)
arcade.start_render()

def draw_sky():
    """Draw the sky"""
    arcade.draw_lrtb_rectangle_filled(0, 900, 700, 400, arcade.color.AQUA)

def draw_sun():
    """Draw the sun"""
    arcade.draw_circle_filled(800, 600, 50, arcade.color.YELLOW_ORANGE)

def draw_halos():
    """Draw the Halos"""
    arcade.draw_circle_outline(800, 600, 75, arcade.color.PALE_GOLD)
    arcade.draw_circle_outline(800, 600, 100, arcade.color.PALE_GOLD)

def draw_cloud(x, y):
    """Draw clouds anywhere"""
    arcade.draw_ellipse_filled(200 + x, 500 + y, 200, 70, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(235 + x, 525 + y, 35, arcade.color.GRAY_BLUE)
    arcade.draw_ellipse_filled(190 + x, 540 + y, 75, 130, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(160 + x, 525 + y, 35, arcade.color.GRAY_BLUE)

def draw_cactus(x, y):
    """Draw cactus anywhere"""
    arcade.draw_lrtb_rectangle_filled(200 + x, 250 + x, 335 + y, 100 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(125 + x, 250 + x, 250 + y, 225 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(125 + x, 150 + x, 275 + y, 225 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(250 + x, 310 + x, 225 + y, 200 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(285 + x, 310 + x, 275 + y, 225 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(225 + x, 335 + y, 25, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(137.5 + x, 275 + y, 12.5, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(297.5 + x, 275 + y, 12.5, arcade.color.BANGLADESH_GREEN)

def draw_rock(x, y):
    """Draw rock anywhere"""
    arcade.draw_lrtb_rectangle_filled(100 + x, 150 + x, 50 + y, 45 + y, arcade.color.BLACK_OLIVE)
    arcade.draw_ellipse_filled(125 + x, 50 + y, 50, 10, arcade.color.BLACK_OLIVE)

def draw_oasis():
    """Draw the oasis"""
    arcade.draw_ellipse_filled(900, 0, 800, 400, arcade.color.BLUE_SAPPHIRE)

def draw_shore():
    """Draw the shore"""
    arcade.draw_ellipse_filled(900, 0, 900, 500, arcade.color.PALE_BROWN)


def main():

    draw_sky()
    draw_sun()
    draw_halos()
    draw_shore()
    draw_oasis()
    draw_cactus(100, 200)
    draw_cactus(0, 0)
    draw_cactus(300, 100)
    draw_cloud(50, 100)
    draw_cloud(350, 25)
    draw_cloud(-100, -10)
    draw_rock(0, 67)
    draw_rock(-40, 150)
    draw_rock(550, 300)
    draw_rock(600, 275)
    draw_rock(325, 100)

    arcade.finish_render()

    arcade.run()

main()

