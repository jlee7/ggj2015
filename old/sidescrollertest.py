import cocos
from cocos import actions
from cocos.director import director

import pyglet
from pyglet.window import key
from ninja import *




class NinjaMovementController(actions.Action):

    global keyboard

    def step(self,dt):

        if (keyboard[key.RIGHT]):
            self.target.x += 10

        if (keyboard[key.LEFT]):
            self.target.x -= 10

class Stage(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):

        super(Stage, self).__init__()

        label = cocos.text.Label("Ninja Game!",
                                 font_name="Courier",
                                 font_size=44,
                                 anchor_x="center",
                                 anchor_y="center")

        label.position = 320, 240

        self.add(label)

    def on_key_press(self, key, modifiers):

        #print key
        pass

class Background(cocos.layer.ColorLayer):

    def __init__(self):

        super(Background, self).__init__(34, 124, 5, 255)
        self._update_color()


def main():

    global keyboard

    director.init()

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    background_layer = Background()
    stage_layer = Stage()
    ninja_sprite = Ninja()
    ninja_sprite.do(NinjaMovementController())


    scene = cocos.scene.Scene()
    scene.add(background_layer, z=-1)
    scene.add(stage_layer, z=0)
    scene.add(ninja_sprite, z=1)

    director.run(scene)

main()
