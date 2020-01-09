
from dataclasses import dataclass


@dataclass
class TileMeta:
    name: str = '???'

    # tile display
    tileset_name: str = 'kanto'
    tileset_ids: tuple = (0, 0, 0, 0)
    color: tuple = (255, 255, 255)

    # tile properties
    is_solid: bool = False
