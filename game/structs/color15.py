
from structs.color import Color


class Color15:
    """
    A 15-bit color.
    """

    def __init__(self, r: int, g: int, b: int):

        assert (0 <= r <= 31
                and 0 <= g <= 31
                and 0 <= b <= 31), 'RGB values must be between 0 - 31'

        self.r, self.g, self.b = (r, g, b)

    def to_24(self) -> Color:
        """
        Convert this color to a 24-bit color.

        Returns:
            Color: a 24-bit color.
        """
        return Color((self.r / 31) * 255,
                     (self.g / 31) * 255,
                     (self.b / 31) * 255)


class palette:

