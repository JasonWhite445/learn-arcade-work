import random
import arcade

SPRITE_NET_SCALE = 0.05
SPRITE_BUTTERFLY_SCALE = 0.01
BUTTERFLY_COUNT = 40
SPRITE_WASP_SCALE = 0.04
WASP_COUNT = 20

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Butterfly(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()

class Wasp(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)

    def update(self):
        self.center_x -= 1

        if self.left < 0:
            self.reset_pos()

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Butterfly Catch")

        self.net_list = None
        self.butterfly_list = None
        self.wasp_list = None

        self.net_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def setup(self):

        self.net_list = arcade.SpriteList()
        self.butterfly_list = arcade.SpriteList()
        self.wasp_list = arcade.SpriteList()

        self.score = 0

        self.net_sprite = arcade.Sprite("Net.png", SPRITE_NET_SCALE)
        self.net_sprite.center_x = 50
        self.net_sprite.center_y = 50
        self.net_list.append(self.net_sprite)



        for i in range(BUTTERFLY_COUNT):
                butterfly = Butterfly("BlueButterfly2.png", SPRITE_BUTTERFLY_SCALE)
                butterfly.center_x = random.randrange(SCREEN_WIDTH)
                butterfly.center_y = random.randrange(SCREEN_HEIGHT)
                self.butterfly_list.append(butterfly)


        for i in range(WASP_COUNT):
            wasp = Wasp("Wasp.png", SPRITE_WASP_SCALE)
            wasp.center_x = random.randrange(SCREEN_WIDTH)
            wasp.center_y = random.randrange(SCREEN_HEIGHT)
            self.wasp_list.append(wasp)

    def on_draw(self):

        arcade.start_render()
        self.net_list.draw()
        self.butterfly_list.draw()
        self.wasp_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.butterfly_list) == 0:
            output = f"Game Over!"
            arcade.draw_text(output, 100, 220, arcade.color.WHITE, 75)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.butterfly_list) > 0:
            self.net_sprite.center_x = x
            self.net_sprite.center_y = y

    def update(self, delta_time):

        self.butterfly_list.update()
        butterfly_hit_list = arcade.check_for_collision_with_list(self.net_sprite, self.butterfly_list)

        for butterfly in butterfly_hit_list:
            butterfly.reset_pos()
            butterfly.remove_from_sprite_lists()
            self.score += 1

        if len(self.butterfly_list) > 0:

            self.wasp_list.update()
            wasp_hit_list = arcade.check_for_collision_with_list(self.net_sprite, self.wasp_list)

            for wasp in wasp_hit_list:
                wasp.reset_pos()
                wasp.remove_from_sprite_lists()
                self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
