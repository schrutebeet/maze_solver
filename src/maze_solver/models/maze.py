from dataclasses import dataclass
from typing import Iterator
from functools import cached_property
from maze_solver.models.square import Square

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]
    # this method will help in iterating over the object Maze.
    # Needed in the next methods: 'width' and 'height'.
    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    # Caching is useful in this context because looping is a 
    # computationally-expensive operation. Here, caching the 
    # result of each iteration avoids having to compute again
    # in case of same input data.
    @cached_property
    def width(self):
        width_list = [square.column for square in self]
        return max(width_list) + 1
    
    @cached_property
    def height(self):
        height_list = [square.row for square in self]
        return max(height_list) + 1