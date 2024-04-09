from fifteenPuzzle import board

print("hello world!")
game_board = board.Board(5)

game_board.print_board()
try:
    game_board.move_tile(board.Move.DOWN)
except board.Board.InvalidMove as error:
    print(error)

game_board.print_board()