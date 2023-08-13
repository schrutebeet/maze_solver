from dataclasses import dataclass
from typing import Iterator
from maze_solver.models.square import Square

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]
    # this method will help in iterating over the object Maze.
    # Needed in the next methods: 'width' and 'height'.
    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    @property
    def width(self):
        width_list = [square.column for square in self]
        return max(width_list) + 1
    
    @property
    def height(self):
        height_list = [square.row for square in self]
        return max(height_list) + 1