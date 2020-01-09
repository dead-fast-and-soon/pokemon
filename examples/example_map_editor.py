"""
A test game demonstrating a world map editor.
"""

from konkyo.game import Game
from konkyo.asset.tileset import TilesetAsset
from konkyo.camera import PixelCamera
from game.entities.editor import Editor
from game.entities.player import Player

WIDTH, HEIGHT = 160, 144

game = Game(width=WIDTH * 4, height=HEIGHT * 4)

scene = game.create_scene()
scene.use_camera(PixelCamera, zoom=4)

scene.spawn_entity(Editor)
scene.spawn_entity(Player)

game.start()
