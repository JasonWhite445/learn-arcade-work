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
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_ellipse_filled( x, 35 + y, 200, 70, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(35 + x, 60 + y, 35, arcade.color.GRAY_BLUE)
    arcade.draw_ellipse_filled(-10 + x, 85 + y, 75, 130, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(-40 + x, 60 + y, 35, arcade.color.GRAY_BLUE)

def draw_cactus(x, y):
    """Draw cactus anywhere"""
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_lrtb_rectangle_filled(-25 + x, 25 + x, 235 + y, y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(-100 + x, 25 + x, 150 + y, 125 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(-100 + x, -75 + x, 175 + y, 125 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(25 + x, 85 + x, 125 + y, 100 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(60 + x, 85 + x, 175 + y, 125 + y, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(x, 235 + y, 25, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(-87.5 + x, 175 + y, 12.5, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(72.5 + x, 175 + y, 12.5, arcade.color.BANGLADESH_GREEN)

def draw_rock(x, y):
    """Draw rock anywhere"""
    arcade.draw_point(x, y, arcade.color.RED, 5)
    arcade.draw_lrtb_rectangle_filled(-25 + x, 25 + x, 5 + y,  y, arcade.color.BLACK_OLIVE)
    arcade.draw_ellipse_filled(x, 5 + y, 50, 10, arcade.color.BLACK_OLIVE)

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
    draw_cactus(275, 275)
    draw_cactus(200, 10)
    draw_cactus(500, 225)
    draw_cloud(550, 600)
    draw_cloud(350, 525)
    draw_cloud(100, 550)
    draw_rock(70, 167)
    draw_rock(80, 250)
    draw_rock(650, 300)
    draw_rock(700, 275)
    draw_rock(325, 100)

    arcade.finish_render()

    arcade.run()

main()

