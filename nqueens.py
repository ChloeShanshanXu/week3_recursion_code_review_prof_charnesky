class NQueens:

    def __init__(self, number_of_queens=8):
        self._total_queens = number_of_queens
        self._current_number_of_queens=0
        self._board = []
        self._number_of_step = 0
        self._number_of_solutions = 0
        for row in range (number_of_queens):
            self._board.append([])
            for column in range(number_of_queens):
                self._board[row].append(' ')
        self.solve()

    def __str__(self):
        return "\n".join(str(row) for row in self._board)+"\n"\
               + "Solution number:"+ str(self._number_of_solutions)+"\n"\
               + "Number of steps:" + str(self._number_of_step)