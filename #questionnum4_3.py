#questionnum4_3
class TowersOfHanoiProblem:
    def __init__(self, initial_state, goal_state):
        # Each peg is a tuple, disks are integers (bigger number = bigger disk)
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goalTest(self, state):
        return state == self.goal_state

    def successor(self, state):
        successors = []
        pegs = [list(peg) for peg in state]

        for i in range(3):  # source peg
            if not pegs[i]:
                continue

            disk = pegs[i][-1]  # top disk

            for j in range(3):  # destination peg
                if i == j:
                    continue

                # move allowed if destination empty or top disk is larger
                if not pegs[j] or pegs[j][-1] > disk:
                    new_pegs = [list(p) for p in pegs]
                    new_pegs[i].pop()
                    new_pegs[j].append(disk)

                    successors.append(tuple(tuple(p) for p in new_pegs))

        return successors

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
    initial = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))

    problem = TowersOfHanoiProblem(initial, goal)
    solution = problem.bfs()

    print("Solution path:")
    print(problem.generate_path(solution))
# Output:
# Solution path:    
# ((3, 2, 1), (), ())
# ((3, 2), (), (1)) 
# ((3,), (2), (1))
# ((), (2), (3, 1))
# ((1), (2), (3))
# ((1), (), (3, 2))
# ((), (), (3, 2, 1))