from enum import Enum
from dataclasses import dataclass


class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


@dataclass
class Rect:
    x: int
    y: int
    width: int
    height: int

    def to_pygame(self):
        return [self.x, self.y, self.width, self.height]





@dataclass
class Color:
    r: int
    g: int
    b: int

    def to_pygame(self):
        return self.r, self.g, self.b


