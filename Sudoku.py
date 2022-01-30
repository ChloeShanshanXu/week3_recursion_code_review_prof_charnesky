class SudokuSolver:

    def __init__(self, board):
        self.board = board
        self.row_index = 0
        self.column_index = 0

    def __str__(self):
        result = ""
        for row in self.board:
            result += str(row) + "\n"
        return result
