from collections import deque

class WaterJug:
    def __init__(self, jug4=4, jug3=0, goal=(2, 0)):
        self.initial_state = (jug4, jug3)
        self.goal_state = goal

    def goalTest(self, state):
        return state == self.goal_state

    def successor(self, state):
        """
        Generate all possible next states based on water jug rules:
        1. Fill jug4 or jug3
        2. Empty jug4 or jug3
        3. Pour water from one jug to the other
        """
        jug4, jug3 = state
        successors = []

        # 1. Fill Jug4 or Jug3
        successors.append((4, jug3))  
        successors.append((jug4, 3))  

        # 2. Empty Jug4 or Jug3
        successors.append((0, jug3))  
        successors.append((jug4, 0))  

        # 3. Pour Jug4 -> Jug3
        pour_to_jug3 = min(jug4, 3 - jug3)
        successors.append((jug4 - pour_to_jug3, jug3 + pour_to_jug3))

        # 4. Pour Jug3 -> Jug4
        pour_to_jug4 = min(jug3, 4 - jug4)
        successors.append((jug4 + pour_to_jug4, jug3 - pour_to_jug4))

        # Remove duplicates and same state
        successors = list(set(s for s in successors if s != state))
        return successors

    def generate_path(self, parent_map, state):
        path = []
        while state is not None:
            path.append(state)
            state = parent_map.get(state)
        return path[::-1]

    def bfs(self):
        queue = deque()
        queue.append(self.initial_state)
        closed = set()
        parent_map = {self.initial_state: None}

        while queue:
            state = queue.popleft()
            if self.goalTest(state):
                return self.generate_path(parent_map, state)

            closed.add(state)
            for child in self.successor(state):
                if child not in closed and child not in queue:
                    queue.append(child)
                    parent_map[child] = state

        return None

    def dfs(self):
        stack = []
        stack.append(self.initial_state)
        closed = set()
        parent_map = {self.initial_state: None}

        while stack:
            state = stack.pop()
            if self.goalTest(state):
                return self.generate_path(parent_map, state)

            closed.add(state)
            for child in self.successor(state):
                if child not in closed and child not in stack:
                    stack.append(child)
                    parent_map[child] = state

        return None

if __name__ == "__main__":
    jug_problem = WaterJug()

    print("BFS Solution Path:")
    bfs_path = jug_problem.bfs()
    if bfs_path:
        for step in bfs_path:
            print(step)
    else:
        print("No solution found.")

    print("\nDFS Solution Path:")
    dfs_path = jug_problem.dfs()
    if dfs_path:
        for step in dfs_path:
            print(step)
    else:
        print("No solution found.")
