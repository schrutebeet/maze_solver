from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        """
        Returns True if the square is a corner, False otherwise.
        Checks if the borders follow one of the following 
        patterns to check if it is a corner.
        """
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )
    
    @property
    def dead_end(self) -> bool:
        """
        Returns True if the square is a dead end, False otherwise.
        Checks if the bit count is equal to 3, which bit count-wise
        means it is sorrounded by three borders. See 
        ./viz helper/border_pattern_binary_table.png for a more
        detailed explanation.
        """
        return self.bit_count() == 3
    
    @property
    def intersection(self) -> bool:
        """
        Returns True if square is an intersection, False otherwise.
        Checks if the bit count is smaller to 2, which bit count-wise
        means it is an intersection. See 
        ./viz helper/border_pattern_binary_table.png for a more
        detailed explanation.
        """
        return self.bit_count() < 2
