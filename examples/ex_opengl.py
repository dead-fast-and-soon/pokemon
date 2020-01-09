"""
A test game demonstrating a world map editor.
"""

from engine.game import Game
from engine.asset.tileset import TilesetAsset
from engine.asset.image import ImageAsset
from engine.components.sprite import Sprite
from engine.camera import PixelCamera
from game.entities.editor import Editor

WIDTH, HEIGHT = 160, 144

game = Game(width=WIDTH * 4, height=HEIGHT * 4)

scene = game.create_scene()
scene.use_camera(PixelCamera, zoom=4)

image = ImageAsset('assets/font.png')

sprite = scene.spawn_component(Sprite, (0, 0), image)
sprite.set_scale_x(1)

game.start()
