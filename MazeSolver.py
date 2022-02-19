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
                    self._solve(row_index, col_index)

    def shortest_path(self):
        try:
            return self._steps_per_solution[min(self._steps_per_solution.keys())]
        except ValueError as e:
            return "No Solution Found"

    def solve(self, row_index, col_index):
        if self._maze[row_index][col_index] == "E"
            self._steps_per_solution[self._current_steps] = str(self)
            return
        if self._maze[row_index][col_index] != 's':
            self._maze[row_index][col_index] = "X"
        self._current_steps += 1