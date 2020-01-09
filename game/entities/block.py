
from engine.components.shapes import Box2D
from engine.objects.component import BatchComponent
from engine.objects.entity import Entity
from structs.color import Color


class Block(BatchComponent):

    def on_spawn(self, color, size: tuple):
        color_1 = Color(255, 255, 0)
        color_2 = color.brightness(0.7)

        self.box_1: Box2D = self.create_component(Box2D, self.position,
                                                 size, color_1)
        self.box_2: Box2D = self.create_component(Box2D, self.position + (1, 1),
                                                 (size[0] - 2, size[1] - 2),
                                                 color_2)

    @property
    def color(self):
        return self.box_1.color

    @color.setter
    def color(self, color: Color):
        self.box_1.color = color
        self.box_2.color = color.brightness(0.7)


class BlockGrid(Entity):

    def on_spawn(self):

        self.i = 0
        self.j = 0
        self.ticks = 0

        self.n = 0  # number of blocks rendering

        self.create_component(Box2D, (0, 0))

    def addBlock(self, x, y):
        color = Color(0, 255, 150)
        darker = color.brightness(0.7)

        self.create_component(Box2D, (x, y), (32, 32), color)
        self.create_component(Box2D, (x + 2, y + 2), (28, 28), darker)

    def on_update(self, delta):
        i, j = self.i, self.j
        self.ticks += 1

        if self.ticks > 10 and self.n < 50:
            self.ticks -= 10

            self.addBlock(i * 32, j * 32)
            self.n += 1
            self.i += 1

            if self.i > 10:
                self.i = 0
                self.j += 1
