from enum import auto
from maze_solver.models.border import Border
from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.models.maze import Maze

def main():
    maze = Maze((Square(index=0, row=0, column=0, border=Border.LEFT | Border.TOP),
                 Square(index=1, row=1, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=2, row=2, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=3, row=3, column=0, border=Border.LEFT | Border.RIGHT),
                 Square(index=4, row=4, column=0, border=Border.LEFT | Border.RIGHT | Border.BOTTOM, role=Role.ENTRANCE),
                 Square(index=5, row=0, column=1, border=Border.TOP | Border.RIGHT),
                 Square(index=6, row=1, column=1, border=Border.LEFT | Border.RIGHT),
                 Square(index=7, row=2, column=1, border=Border.LEFT),
                 Square(index=8, row=3, column=1, border=Border.LEFT | Border.RIGHT),
                 Square(index=9, row=4, column=1, border=Border.LEFT | Border.RIGHT | Border.BOTTOM),
                 Square(index=10, row=0, column=2, border=Border.LEFT | Border.RIGHT | Border.TOP),
                 Square(index=11, row=1, column=2, border=Border.LEFT | Border.BOTTOM),
                 Square(index=12, row=2, column=2, border=Border.TOP),
                 Square(index=13, row=3, column=2, border=Border.LEFT | Border.RIGHT),
                 Square(index=14, row=4, column=2, border=Border.LEFT | Border.BOTTOM),
                 Square(index=15, row=0, column=3, border=Border.LEFT | Border.RIGHT | Border.TOP),
                 Square(index=16, row=1, column=3, border=Border.RIGHT),
                 Square(index=17, row=2, column=3, border=Border.RIGHT | Border.BOTTOM),
                 Square(index=18, row=3, column=3, border=Border.LEFT | Border.TOP | Border.BOTTOM),
                 Square(index=19, row=4, column=3, border=Border.LEFT | Border.RIGHT | Border.TOP, role=Role.EXIT),
                 Square(index=20, row=0, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=21, row=1, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=22, row=2, column=4, border=Border.LEFT | Border.RIGHT),
                 Square(index=23, row=3, column=4, border=Border.RIGHT),
                 Square(index=24, row=4, column=4, border=Border.BOTTOM | Border.RIGHT),))
    
    print(maze.squares[1].index)

if __name__=='__main__':
    main()
