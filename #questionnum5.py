#questionnum5
def calculate_heuristic(current_state, goal_state):
    """
    Calculates the global heuristic e(p) for the Blocks World problem.
    e(p) = (Sum of points for correct support) - (Sum of points for wrong support)
    """
    score = 0
# i = current height/index (0 is the bottom/table)
    # block = the name of the block (e.g., 'A')
    for i, block in enumerate(current_state):
        if i < len(goal_state) and current_state[:i+1] == goal_state[:i+1]:

            score += (i + 1)
        else:
            score -= (i + 1)

    return score   # ← MUST be inside the function


# Test
initial = ['A', 'D', 'C', 'B']
goal = ['D', 'C', 'B', 'A']

h_value = calculate_heuristic(initial, goal)
print (f"Initial State: {initial}")
print(f"Goal State:    {goal}")
print("Heuristic Value:", h_value)


#output:
# Initial State: ['A', 'D', 'C', 'B']
# Goal State:    ['D', 'C', 'B', 'A']
#Heuristic Value: -10