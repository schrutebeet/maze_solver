from dataclasses import dataclass
from maze_solver.models.border import Border
from maze_solver.models.role import Role

# the dataclass decoratoe is used to simplify the class.
# It automatically generates the __init__ method.
# It can be used along with type annotations and default values.
@dataclass(frozen=True)
class Square:
    # These is an example of a type annotation 
    index: int
    row: int
    column: int
    border: Border
    # These is an example of a type annotation and a default value
    role: Role = Role.NONE
