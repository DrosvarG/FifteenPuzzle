from enum import Enum

class Coord():
    def __init__(self, x:int = 0, y:int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

class Move(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Tile():
    def __init__(self, number:int = None):
        self.value = number

class Board():
    class InvalidMove(Exception):
        pass

    def __init__(self, size:int):
        self.__size = size
        self.__tiles = [[Tile((x*size + y)+1) for y in range(size)] for x in range(size)]
        self.__tiles[size-1][size-1] = Tile()
        self.__empty_tile_coords=Coord(size-1, size-1)

    def __swapElements(self, pos1:Coord, pos2:Coord):
        self.__tiles[pos1.x][pos1.y], self.__tiles[pos2.x][pos2.y] = self.__tiles[pos2.x][pos2.y], self.__tiles[pos1.x][pos1.y]

    def move_tile(self, move:Move):
        match move:
            case Move.UP:
                new_empty_tile_coords = self.__empty_tile_coords + Coord(1, 0)
            case Move.DOWN:
                new_empty_tile_coords = self.__empty_tile_coords + Coord(-1, 0)
            case Move.LEFT:
                new_empty_tile_coords = self.__empty_tile_coords + Coord(0, 1)
            case Move.RIGHT:
                new_empty_tile_coords = self.__empty_tile_coords + Coord(0, -1) 
            case _:
                raise Board.InvalidMove("Invalid move: Unknown move")

        if 0 <= new_empty_tile_coords.x < self.__size and 0 <= new_empty_tile_coords.y < self.__size:
            self.__swapElements(self.__empty_tile_coords, new_empty_tile_coords)
            self.__empty_tile_coords = new_empty_tile_coords
        else:
            raise Board.InvalidMove("Invalid move: OOB forbidden")

    def print_board(self):
        for x in range(self.__size):
            for y in range(self.__size):
                if self.__tiles[x][y].value is None:
                    print("  ", end='')
                else:
                    print(f"{self.__tiles[x][y].value} ", end='')
            print("")

