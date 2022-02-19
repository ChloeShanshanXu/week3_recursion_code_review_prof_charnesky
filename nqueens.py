class NQueens:

    def __init__(self, number_of_queens=8):
        self._total_queens = number_of_queens
        self._current_number_of_queens=0
        self._board = []
        self._number_of_steps = 0
        self._number_of_solutions = 0
        for row in range (number_of_queens):
            self._board.append([])
            for column in range(number_of_queens):
                self._board[row].append(' ')
        self._solve()

    def __str__(self):
        return "\n".join(str(row) for row in self._board)+"\n"\
               + "Solution number:"+ str(self._number_of_solutions)+"\n"\
               + "Number of steps:" + str(self._number_of_steps)

    def _is_solved(self):
        return self._current_number_of_queens == self._total_queens

    def _solve(self):
        if self._is_solved():
            self._number_of_solutions += 1
            print(self)
        else:
            self._number_of_steps +=1
            print(self, "start step")
            for row_index in range(self. _total_queens):
                if not self._is_solved() and self._can_place_queen(row_index):
                    self._board[row_index][self._current_number_of_queens] = "Q"
                    self._current_number_of_queens +=1
                    self._solve()
                    if not self._is_solved():
                        self._current_number_of_queens -=1
                        self._board[row_index][self._current_number_of_queens] =" "
                        print(self, "cancel last step")


    def _is_row_open(self, row_index):
        return "Q" not in self._board[row_index]

    def _is_up_dia_open(self, row_index):
        current_column_index = self._current_number_of_queens -1
        current_row_index = row_index -1
        while current_row_index >=0 and current_column_index >=0:
            if self._board[current_row_index][current_column_index]=="Q":
                return False
            current_column_index -= 1
            current_row_index -= 1
        return True

    def _is_dn_dia_open(self, row_index):
        current_column_index = self._current_number_of_queens -1
        current_row_index = row_index + 1  #questions
        while current_row_index < self._total_queens and current_column_index >=0:
            if self._board[current_row_index][current_column_index]=="Q":
                return False
            current_column_index -= 1
            current_row_index += 1
        return True

    def _can_place_queen(self, row_index):
        return self._is_row_open(row_index) and\
            self._is_up_dia_open(row_index) and\
            self._is_dn_dia_open(row_index)

if __name__ =="__main__":
    queens = NQueens(4)