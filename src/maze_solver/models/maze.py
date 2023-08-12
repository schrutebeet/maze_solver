from dataclasses import dataclass
from maze_solver.models.square import Square

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    def width(self):
        return max(square.column for square in self) + 1
    
    def height(self):
        return max(square.row for square in self) + 1