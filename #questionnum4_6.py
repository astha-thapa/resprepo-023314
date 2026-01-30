#questionnum4_6
class ManGoatLionCabbageProblem:
    def __init__(self, initial_state, goal_state):
        # State is a tuple of four elements: (man, goat, lion, cabbage)
        # Each element is either 'L' (left bank) or 'R' (right bank)
        self.initial_state = initial_state
        self.goal_state = goal_state
    def goalTest(self, state):
        return state == self.goal_state
    def successor(self, state):
        successors = []
        man, goat, lion, cabbage = state

        # 1. Man moves alone
        new_man_pos = 'R' if man == 'L' else 'L'
        alone_state = list(state)
        alone_state[0] = new_man_pos
        if self.is_valid(tuple(alone_state)):
            successors.append(tuple(alone_state))

        # 2. Man moves with one item
        items = [('goat', 1), ('lion', 2), ('cabbage', 3)]
        for item_name, idx in items:
            # CRITICAL CHECK: Man must be on the same side as the item
            if state[idx] == man:
                new_state = list(state)
                new_state[0] = new_man_pos   # Man moves
                new_state[idx] = new_man_pos # Item moves with him
                
                new_state_tuple = tuple(new_state)
                if self.is_valid(new_state_tuple):
                    successors.append(new_state_tuple)

        return successors
    def is_valid(self, state):
        man, goat, lion, cabbage = state
        # Goat and lion alone
        if goat == lion and man != goat:
            return False
        # Goat and cabbage alone
        if goat == cabbage and man != goat:
            return False
        return True
    def bfs(self):
        from collections import deque

        queue = deque([(self.initial_state, [])])
        visited = set()

        while queue:
            current_state, path = queue.popleft()

            if self.goalTest(current_state):
                return path + [current_state]

            if current_state in visited:
                continue

            visited.add(current_state)

            for next_state in self.successor(current_state):
                if next_state not in visited:
                    queue.append((next_state, path + [current_state]))

        return None
    def generate_path(self, solution_path):
        if solution_path is None:
            return "No solution found"
        return "\n".join(str(state) for state in solution_path)
# Example usage
if __name__ == "__main__":
    initial = ('L', 'L', 'L', 'L')  # All on the left bank
    goal = ('R', 'R', 'R', 'R')     # All on the right bank

    problem = ManGoatLionCabbageProblem(initial, goal)
    solution = problem.bfs()
    print(problem.generate_path(solution))
# Output:
# ('L', 'L', 'L', 'L')
# ('R', 'R', 'L', 'L')
# ('L', 'R', 'L', 'L')
# ('R', 'R', 'R', 'L')
# ('L', 'L', 'R', 'L')
# ('R', 'L', 'R', 'R')
# ('L', 'L', 'R', 'R')
# ('R', 'R', 'R', 'R')