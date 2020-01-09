
import math

from konkyo.game import Game
from konkyo.asset.tileset import TilesetAsset
from konkyo.objects.entity import Entity
from konkyo.components.shapes import Box2D
from konkyo.components.sprite import SpriteText
from konkyo.camera import PixelCamera
from konkyo.structs.vector import Vector


class ExampleEntity(Entity):

    def on_spawn(self, text: str, speed: float):

        tileset = TilesetAsset('assets/font.png', tile_height=8, tile_width=8)

        sprite = self.create_component(SpriteText, (0, 8),
                                       tileset, text)
        box = self.create_component(Box2D, (0, 0),
                                    size=(8, 8), color=(0, 0, 255))
        sprite.parent = self.root_component
        box.parent = self.root_component

        self.time: float = 0
        self.speed = speed

    @Entity.limit_rate(60)
    def on_update(self, delta: float):
        self.position = Vector((math.cos(self.time * self.speed) * 10,
                                math.sin(self.time * self.speed) * 10))
        self.time += delta

    def on_key_press(self, symbol, modifier):
        print(symbol)


game = Game(width=1280, height=720)

scene = game.create_scene()
scene.use_camera(PixelCamera, zoom=4.0)
scene.spawn_entity(ExampleEntity, (0, 0), 'hello there', 2)
# scene.spawn_entity(ExampleEntity, (10, -5), 'what', 3)

game.start()
