# Code review From Prof. Charnesky at:
# https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Project1-MazeSolver/main.py

class MazeSolver:

    def __init__(self, maze):
        self._maze = maze
        self._current_steps = 0
        self._steps_per_solution = {}
        for row_index in range(len(self._maze)):
            for col_index in range(len(self._maze[row_index])):
                if self._maze[row_index][col_index] == "S":
                    self.solve(row_index, col_index)

    def shortest_path(self):
        try:
            return self._steps_per_solution[min(self._steps_per_solution.keys())]
        except ValueError as e:
            return "No Solution Found"

    def solve(self, row_index, col_index):

        if self._maze[row_index][col_index] == "E":
            # print(self)
            self._steps_per_solution[self._current_steps] = str(self)
            return

        if self._maze[row_index][col_index] != 's':
            self._maze[row_index][col_index] = "X"
        self._current_steps += 1

        self._try_move(row_index - 1, col_index)
        self._try_move(row_index + 1, col_index)
        self._try_move(row_index, col_index - 1)
        self._try_move(row_index, col_index + 1)

        if self._maze[row_index][col_index] != 'S':
            self._maze[row_index][col_index] = ' '
            self._current_steps -= 1

    def _try_move(self, row_index, col_index):
        if self._can_move_to(row_index, col_index):
            self.solve(row_index, col_index)

    def _can_move_to(self, row_index, col_index):
        return 0<= row_index < len(self._maze) and 0<= col_index <len(self._maze[row_index]) and \
               (self._maze[row_index][col_index] == ' ' or self._maze[row_index][col_index] == 'E')

    def __str__(self):
        result = ''
        for row in self._maze:
            result += str(row) + '\n'
        result += f'{self._current_steps} steps\n'
        return result

if __name__ == '__main__':
    maze = [
        ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        ['W', 'W', ' ', 'W', ' ', ' ', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' '],
        [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        [' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' '],
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E']
    ]
    solve = MazeSolver(maze)
    print (solve.shortest_path())