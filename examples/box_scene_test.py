"""
A graphics test using multiple boxes in order to test performance.
"""

import math

from engine.components.shapes import Box2D
from engine.objects.entity import Entity
from engine.utils import autoargs
from engine.camera import PixelCamera
from engine.game import Game
from engine.scene import Scene

from structs.color import Color


class BoxTest(Entity):
    """
    An example entity.
    """
    @Entity.autoargs
    def __init__(self):
        self.ticks = 0  # accumulate total ticks
        self.boxes = []

        for i in range(0, 1500):
            if i < 750:
                # blue to cyan
                color = (0, int(255 * (i / 750)), 255)
            else:
                # cyan to green
                color = (0, 255, int(255 * (1 - ((i - 750) / 750))))

            box = self.create_component(
                Box2D, ((i - 750) * 0.8, 0),
                size=(10, 10), color=color, name='box {}'.format(i)
            )

            self.boxes.append(box)

    @Entity.limit_rate(20)
    def on_update(self, delta: float):
        for i in range(len(self.boxes)):
            box = self.boxes[i]
            box.position = (
                box.position.x, math.sin(self.ticks * 0.01 + (i * 0.1))
                * math.cos(self.ticks * 0.01 + (i * 0.01)) * 200
            )

        self.ticks += delta * 50


class ExampleScene(Scene):

    def on_load(self):

        self.spawn_entity(BoxTest)


# configure game window
game = Game(width=1280, height=720)

# spawn entities
scene = game.load_scene(ExampleScene)

# start game
game.start()
