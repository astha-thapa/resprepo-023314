#8.	Write a program to implement the steepest ascent hill climbing for the 8-puzzle problem. Develop appropriate heuristic functions. 
import random
class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    value = self.board[i][j]
                    goal_row = (value - 1) // 3
                    goal_col = (value - 1) % 3
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance
    def get_neighbors(self):
        neighbors = []
        zero_pos = [(i, row.index(0)) for i, row in enumerate(self.board) if 0 in row][0]
        x, y = zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board))
        return neighbors
def steepest_ascent_hill_climbing(initial_board):
    current_state = PuzzleState(initial_board)
    while True:
        if current_state.board == current_state.goal:
            return current_state.board
        neighbors = current_state.get_neighbors()
        next_state = None
        min_heuristic = current_state.heuristic()
        for neighbor in neighbors:
            h = neighbor.heuristic()
            if h < min_heuristic:
                min_heuristic = h
                next_state = neighbor
        if next_state is None:
            return None  # No better neighbors found, local maximum reached
        current_state = next_state
# Example usage
initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = steepest_ascent_hill_climbing(initial_board)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")

# Output:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 0]