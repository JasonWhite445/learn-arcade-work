import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Gem Knight!"

NUMBER_OF_GEMS = 25

VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.avatar_list = None
        self.avatar_sprite = None
        self.gem_list = None
        self.box_list = None
        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0

        self.gem_sound = arcade.load_sound("open_001.ogg")

    def setup(self):

        self.avatar_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        self.avatar_sprite = arcade.Sprite("Avatar.png", 0.1)
        self.avatar_sprite.center_x = 64
        self.avatar_sprite.center_y = 270
        self.avatar_list.append(self.avatar_sprite)

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                if random.randrange(5) > 0:
                    box = arcade.Sprite("box.png", 0.125)
                    box.center_x = x
                    box.center_y = y
                    self.box_list.append(box)

        for x in range(0, 1850, 64):
            box = arcade.Sprite("wall.png", 0.125)
            box.center_x = x
            box.center_y = 1050
            self.box_list.append(box)

        for x in range(0, 1850, 64):
            box = arcade.Sprite("wall.png", 0.125)
            box.center_x = x
            box.center_y = -25
            self.box_list.append(box)

        for y in range(-25, 1050, 64):
            box = arcade.Sprite("wall.png", 0.125)
            box.center_x = 0
            box.center_y = y
            self.box_list.append(box)

        for y in range(-25, 1050, 64):
            box = arcade.Sprite("wall.png", 0.125)
            box.center_x = 1850
            box.center_y = y
            self.box_list.append(box)

        for i in range(NUMBER_OF_GEMS):

            gem = arcade.Sprite("gem.png")
            gem_placed_successfully = False

            while not gem_placed_successfully:

                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)
                box_hit_list = arcade.check_for_collision_with_list(gem, self.box_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(box_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True

            self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.avatar_sprite, self.box_list)

        arcade.set_background_color(arcade.color.BLACK)

        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):

        arcade.start_render()

        self.box_list.draw()
        self.gem_list.draw()
        self.avatar_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.avatar_sprite.change_y = MOVEMENT_SPEED
            print("hi")
        elif key == arcade.key.DOWN:
            self.avatar_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.avatar_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.avatar_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

         if key == arcade.key.UP or key == arcade.key.DOWN:
             self.avatar_sprite.change_y = 0
         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
             self.avatar_sprite.change_x = 0

    def update(self, delta_time):

        self.gem_list.update()
        gem_hit_list = arcade.check_for_collision_with_list(self.avatar_sprite, self.gem_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

        self.physics_engine.update()
        changed = False

        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.avatar_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.avatar_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.avatar_sprite.right > right_boundary:
            self.view_left += self.avatar_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.avatar_sprite.top > top_boundary:
            self.view_bottom += self.avatar_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.avatar_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.avatar_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()




