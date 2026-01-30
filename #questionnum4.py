#questionnum4

class CityMapProblem:
    def __init__(self, initial_state, goal_state, city_map):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.city_map = city_map

    def goalTest(self, current_state):
        return current_state == self.goal_state

    def successor(self, state):
        return self.city_map.get(state, [])

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

            for successor in self.successor(current_state):
                if successor not in visited:
                    queue.append((successor, path + [current_state]))

        return None

    def generate_path(self, solution_path):
        if solution_path is None:
            return "No solution found"
        return " -> ".join(solution_path)


# Example usage
if __name__ == "__main__":
    city_map = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    problem = CityMapProblem('A', 'F', city_map)
    solution = problem.bfs()
    print("Path from A to F:", problem.generate_path(solution))
 
# Output:
# Path from A to F: A -> C -> F