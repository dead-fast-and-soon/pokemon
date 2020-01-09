
from konkyo.objects.entity import Entity
from konkyo.asset.tileset import TilesetAsset
from konkyo.asset.managers.tileset import TilesetManager
from game.structs.tilemeta import TileMeta
from konkyo.objects.component import BatchComponent
from konkyo.components.sprite import Sprite


class TileSprite(BatchComponent):

    def on_spawn(self, tileset: TilesetAsset, meta: TileMeta, offsets=None):

        pos = self.position
        offsets = offsets or ((0, 8), (8, 8), (0, 0), (8, 0))

        assert len(meta.tileset_ids) == len(offsets)

        self._sprites = []

        for i, offset in enumerate(offsets):
            id = tile.tileset_ids[i]
            if id < 0:
                id = id % len(tile.tileset_ids)
            self._sprites.append(
                self.create_component(Sprite, pos + offset, tileset[id],
                                      color=tile.color)
            )


class TileSpriteFactory:

    def __init__(self, parent: Entity, manager: TilesetManager):
        self._parent: Entity = parent
        self._manager = manager

    def create_tile(self, tile: TileMeta, pos: tuple):
        self._manager.load(tile.tileset_name, 8)
        tileset = self._manager.get(tile.tileset_name)
        return self._parent.create_component(TileSprite, pos, tileset, tile)
