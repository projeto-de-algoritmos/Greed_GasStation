# Caso de Teste 1
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

import containerWithMostWater as cm

height = [1,8,6,2,5,4,8,3,7]

solution = cm.Solution()
print(f"Heights: {height}")
result = solution.maxArea(height)
print(f"Solution {result}")