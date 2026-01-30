#questionnum4_2
class MissionariesCannibalsProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state  # (3, 3, 'left')
        self.goal_state = goal_state          # (0, 0, 'right')

    def goalTest(self, current_state):
        return current_state == self.goal_state

    def successor(self, state):
        successors = []
        M_left, C_left, boat = state
        M_right = 3 - M_left
        C_right = 3 - C_left

        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

        for M_move, C_move in moves:
            if boat == 'left':
                new_M_left = M_left - M_move
                new_C_left = C_left - C_move
                new_boat = 'right'
            else:
                new_M_left = M_left + M_move
                new_C_left = C_left + C_move
                new_boat = 'left'

            new_M_right = 3 - new_M_left
            new_C_right = 3 - new_C_left

            if (0 <= new_M_left <= 3 and 0 <= new_C_left <= 3 and
                (new_M_left == 0 or new_M_left >= new_C_left) and
                (new_M_right == 0 or new_M_right >= new_C_right)):
                successors.append((new_M_left, new_C_left, new_boat))

        return successors
    def bfs(self):
        from collections import deque

        initial_state = self.initial_state
        goal_state = self.goal_state

        queue = deque([(initial_state, [])])
        visited = set()

        while queue:
            current_state, path = queue.popleft()

            if self.goalTest(current_state):
                return path + [current_state]

            if current_state in visited:
                continue

            visited.add(current_state)

            for successor in self.successor(current_state):
                if successor not in visited:
                    queue.append((successor, path + [current_state]))

        return None
    def generate_path(self, solution_path):
        if solution_path is None:
            return "No solution found"
        return " -> ".join([f"({m},{c},{b})" for m, c, b in solution_path]) 
# Example usage
if __name__ == "__main__":
    problem = MissionariesCannibalsProblem((3, 3, 'left'), (0, 0, 'right'))
    solution = problem.bfs()
    print("Path from (3,3,left) to (0,0,right):", problem.generate_path(solution))  