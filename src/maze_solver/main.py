from enum import auto
from maze_solver.models.border import Border
from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.models.maze import Maze

def main():
    maze = Maze((Square(index=auto(), row=0, column=0, border=Border.LEFT | Border.TOP),
                 Square(index=auto(), row=1, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=2, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=3, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=4, column=0, border=Border.LEFT | Border.RIGHT | Border.BOTTOM, role=Role.ENTRANCE),
                 Square(index=auto(), row=0, column=1, border=Border.TOP | Border.RIGHT),
                 Square(index=auto(), row=1, column=1, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=2, column=1, border=Border.LEFT),
                 Square(index=auto(), row=3, column=1, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=4, column=1, border=Border.LEFT | Border.RIGHT | Border.BOTTOM),
                 Square(index=auto(), row=0, column=2, border=Border.LEFT | Border.RIGHT | Border.TOP),
                 Square(index=auto(), row=1, column=2, border=Border.LEFT | Border.BOTTOM),
                 Square(index=auto(), row=2, column=2, border=Border.TOP),
                 Square(index=auto(), row=3, column=2, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=4, column=2, border=Border.LEFT | Border.BOTTOM),
                 Square(index=auto(), row=0, column=3, border=Border.LEFT | Border.RIGHT | Border.TOP),
                 Square(index=auto(), row=1, column=3, border=Border.RIGHT),
                 Square(index=auto(), row=2, column=3, border=Border.RIGHT | Border.BOTTOM),
                 Square(index=auto(), row=3, column=3, border=Border.LEFT | Border.TOP | Border.BOTTOM),
                 Square(index=auto(), row=4, column=3, border=Border.LEFT | Border.RIGHT | Border.TOP, role=Role.EXIT),
                 Square(index=auto(), row=0, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=1, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=2, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=auto(), row=3, column=4, border=Border.RIGHT),
                 Square(index=auto(), row=4, column=4, border=Border.BOTTOM | Border.RIGHT),))
    
    print(maze.width)

if __name__=='__main__':
    main()
