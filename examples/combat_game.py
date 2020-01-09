"""
A test of the block-based combat game idea.
"""

import math
import pyglet
import pyglet.window.key as key

from typing import cast

from konkyo.components.text import Text
from konkyo.components.console import Console
from konkyo.components.shapes import Box2D
from konkyo.objects.component import BatchComponent
from konkyo.objects.entity import Entity
from konkyo.camera import PixelCamera
from konkyo.game import Game
from konkyo.scene import Scene

from game.entities.block import Block

from konkyo.structs.vector import Vector
from structs.color import Color

BLOCK_SIZE = 8  # in pixels

SELECT_AREA = 5  # select phase area
SELECT_POS_L = Vector(-85, 0)
SELECT_POS_R = Vector(85, 0)


class BackgroundComponent(BatchComponent):

    def on_spawn(self, size: tuple):

        color_1 = Color(20, 20, 20)
        color_2 = Color(40, 40, 40)

        ctr = Vector(
            (BLOCK_SIZE * size[0]) // -2,
            (BLOCK_SIZE * size[1]) // -2
        )

        color = color_1

        for i in range(0, size[0]):  # x-range
            for j in range(0, size[1]):  # y-range

                pos = (ctr + Vector(i * BLOCK_SIZE, j * BLOCK_SIZE)
                       + self.position)

                self.create_component(
                    Box2D, pos,
                    (BLOCK_SIZE, BLOCK_SIZE), tuple(color)
                )

                color = color_2 if color is color_1 else color_1


class Cursor(Entity):

    def on_spawn(self):

        self.color_select = Color(64, 163, 239)  # sky-blueish

        self.origin = SELECT_POS_L
        self.boxes = {}

        for y in reversed(range(-2, 3)):
            for x in range(-2, 3):

                pos = (self.origin + self.position
                       + Vector(x * BLOCK_SIZE, y * BLOCK_SIZE))

                self.boxes[(x, y)] = self.create_component(
                    Block, pos,
                    size=(BLOCK_SIZE, BLOCK_SIZE),
                    color=Color(10, 10, 10)
                )

        self.grid_pos = Vector(0, 0)
        self.selected_coords = [self.grid_pos]

        self.dir_x = 0
        self.dir_y = 0

        # grid coordinates of block
        self.stun_ticks = 0

        self.update_blocks()

    def update_blocks(self):
        """Update block position based on block_pos"""

        for pos, box in self.boxes.items():
            box.pos = self.origin + Vector(
                (pos[0] - (1 / 2)) * BLOCK_SIZE,
                (pos[1] - (1 / 2)) * BLOCK_SIZE
            )

            if self.grid_pos == pos:
                box.color = self.color_select
            elif any(x == pos for x in self.selected_coords):
                box.color = Color(5, 255, 255)
            else:
                box.color = Color(10, 10, 10)

    def on_update(self, delta: float):

        # print(f'{self.dir_x}, {self.dir_y}')
        global console

        if self.dir_x == 0 and self.dir_y == 0:
            self.grid_pos = Vector(0, 0)
            self.selected_coords = [Vector(0, 0)]
            self.update_blocks()
        elif self.stun_ticks == 0:
            self.grid_pos += (self.dir_x, self.dir_y)

            if self.grid_pos.x > 2:
                self.grid_pos.x = 2
            if self.grid_pos.y > 2:
                self.grid_pos.y = 2
            if self.grid_pos.x < -2:
                self.grid_pos.x = -2
            if self.grid_pos.y < -2:
                self.grid_pos.y = -2

            self.stun_ticks = 4
            if not any(x == self.grid_pos for x in self.selected_coords):
                self.selected_coords.append(self.grid_pos)

            self.update_blocks()

        if self.stun_ticks > 0:
            self.stun_ticks -= 1

        console.line(0, 'pos: ' + str(tuple(self.grid_pos)))
        console.line(1, 'dir: ' + str((self.dir_x, self.dir_y)))
        console.line(2, 'select: ' + str(self.selected_coords))
        console.line(3, 'stun: ' + str(self.stun_ticks))

    def on_key_press(self, k: int, mod):
        print(k)
        if k is key.UP:
            if self.dir_y == -1:
                self.dir_y = 0
            else:
                self.dir_y = 1

        elif k is key.DOWN:
            if self.dir_y == 1:
                self.dir_y = 0
            else:
                self.dir_y = -1

        elif k is key.RIGHT:
            if self.dir_x == -1:
                self.dir_x = 0
            else:
                self.dir_x = 1

        elif k is key.LEFT:
            if self.dir_x == 1:
                self.dir_x = 0
            else:
                self.dir_x = -1

    def on_key_release(self, k: int, mod):
        if k is key.UP:
            if self.dir_y == 1:
                self.dir_y = 0
            else:
                self.dir_y = -1

        elif k is key.DOWN:
            if self.dir_y == -1:
                self.dir_y = 0
            else:
                self.dir_y = 1

        elif k is key.RIGHT:
            if self.dir_x == 1:
                self.dir_x = 0
            else:
                self.dir_x = -1

        elif k is key.LEFT:
            if self.dir_x == -1:
                self.dir_x = 0
            else:
                self.dir_x = 1

    def on_position_change(self):
        # shift block position to be center on entity position
        # self.block.pos = self.pos - Vector(BLOCK_SIZE // 2, BLOCK_SIZE // 2)
        pass


class CombatScene(Scene):

    def on_load(self):

        self.spawn_component(BackgroundComponent, (0, 0), (15, 9))
        self.spawn_component(BackgroundComponent, SELECT_POS_L, (5, 5))
        self.spawn_entity(Cursor, (0, 0))

    def on_update(self, delta: float):

        pass


# configure game window
game = Game(width=1280, height=720)

# spawn entities
scene = game.load_scene(CombatScene)
# scene = game.createScene()

# create new camera
scene.use_camera(PixelCamera, zoom=4)

console = game.console
# game.log("test")

# def updateCamera(delta: float):
#     global ticks
#     camera.focus = Vector(
#         math.sin(ticks * 0.1) * 100,
#         math.cos(ticks * 0.1) * 100
#     )
#     ticks += 1

# start game
print('starting game')
game.start()
