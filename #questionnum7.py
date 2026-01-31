#7.	Solve the 8 puzzle problems using A* algorithm in Python.
import heapq
class PuzzleState:
    def __init__(self, board, moves=0, parent=None):
        self.board = board
        self.moves = moves
        self.parent = parent
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())
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
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors
def a_star(initial_board):
    initial_state = PuzzleState(initial_board)
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.board == current_state.goal:
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]
        closed_set.add(tuple(map(tuple, current_state.board)))
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.board)) in closed_set:
                continue
            heapq.heappush(open_set, neighbor)
    return None
# Example usage
initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = a_star(initial_board)
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
    
    #output:
    #[1,2,3]
    #[4,0,6]
    #[7,5,8]    
    #[1,2,3]
    #[4,5,6]
    #[7,0,8] 
    #[1,2,3]
    #[4,5,6]
    #[7,8,0] 