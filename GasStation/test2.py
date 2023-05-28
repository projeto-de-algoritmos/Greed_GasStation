# Caso de Teste 2
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

import gasStation as gs

gas = [2,3,4]
cost = [3,4,3]

solution = gs.Solution() 
print(f"Gas: {gas}")
print(f"Cost: {cost}")
result = solution.canCompleteCircuit(gas, cost)
print(f"Solution: {result}")
