from itertools import product


class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    def __init__(self):
        self.board = {i + j: Cell('X') for i, j in product("ABCDEFGH", "87654321")}

        blacks = [i + j for i, j in product("BDFH", "86")]
        blacks.extend([i + j for i, j in product("ACEG", "7")])
        for i in blacks:
            self.board[i] = Cell('B')

        whites = [i + j for i, j in product("ACEG", "13")]
        whites.extend([i + j for i, j in product("BDFH", "2")])
        for i in whites:
            self.board[i] = Cell('W')

    def move(self, f, t):
        self.board[t] = self.board[f]
        self.board[f] = Cell('X')

    def get_cell(self, p):
        return self.board[p]


checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
