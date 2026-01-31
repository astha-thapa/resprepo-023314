# 9.	WAP to demonstrate the effect of temperature on the probability of choosing an inferior node by selecting an appropriate temperature schedule.
from typing_extensions import Final
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0
    else:
        return math.exp((current_cost - new_cost) / temperature)
def simulated_annealing(initial_solution, cost_function, neighbor_function, initial_temp, cooling_rate, min_temp):
    current_solution = initial_solution
    current_cost = cost_function(current_solution)
    temperature = initial_temp
    costs = [current_cost]
    while temperature > min_temp:
        new_solution = neighbor_function(current_solution)
        new_cost = cost_function(new_solution)
        ap = acceptance_probability(current_cost, new_cost, temperature)
        if ap > random.random():
            current_solution = new_solution
            current_cost = new_cost
        costs.append(current_cost)
        temperature *= cooling_rate
    return current_solution, current_cost, costs
def cost_function(solution):
    return sum(x**2 for x in solution)
def neighbor_function(solution):
    neighbor = solution[:]
    index = random.randint(0, len(solution) - 1)
    neighbor[index] += random.uniform(-1, 1)
    return neighbor
initial_solution = [random.uniform(-10, 10) for _ in range(5)]
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1
final_solution, final_cost, costs = simulated_annealing(initial_solution, cost_function, neighbor_function, initial_temp, cooling_rate, min_temp)
plt.plot(costs)
plt.title('Simulated Annealing Cost Over Time')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()
print("Initial Solution:", initial_solution)
print("Final Solution:", final_solution)
print("Final Cost:", final_cost)
# Analyzing the effect of temperature on the probability of choosing an inferior node
temperatures = [1000, 500, 100, 50, 10, 1]
probabilities = []
for temp in temperatures:
    ap = acceptance_probability(10, 15, temp)
    probabilities.append(ap)
df = pd.DataFrame({'Temperature': temperatures, 'Acceptance Probability': probabilities})
sns.lineplot(data=df, x='Temperature', y='Acceptance Probability', marker='o')
plt.title('Effect of Temperature on Acceptance Probability of Inferior Node')
plt.xlabel('Temperature')
plt.ylabel('Acceptance Probability')
plt.xscale('log')
plt.show()

#output:
# Initial Solution: [3.863132885673341, 2.179754963798235, -7.725057786477894, 3.76069251637122, 8.553711588235522]
# Final Solution: [2.5062606767176634, -1.347640378437071, -9.71508967304682, 0.2867143504039038, 8.590269992631882]
# Final Cost: 176.35538818963556