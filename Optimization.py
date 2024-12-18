import numpy as np
from scipy.optimize import linprog

# Problem Definition:

# Product A: Profit per unit = $30, Labor hours per unit = 5, Raw material per unit = 3 kg
# Product B: Profit per unit = $20, Labor hours per unit = 4, Raw material per unit = 2 kg
# Product C: Profit per unit = $50, Labor hours per unit = 6, Raw material per unit = 4 kg

# Constraints:
# 1. Labor hours: 5A + 4B + 6C <= 240
# 2. Raw materials: 3A + 2B + 4C <= 180
# 3. Non-negativity: A, B, C >= 0

# Objective:
# Maximize profit: Profit = 30A + 20B + 50C


c = [-30, -20, -50]

# Coefficients for the inequality constraints (Labor Hours and Raw Material)
A = [
    [5, 4, 6],  # Labor hours
    [3, 2, 4]   # Raw material
]
b = [240, 180]  # Resource limits (Labor hours = 240, Raw material = 180)

x0_bounds = (0, None)  
x1_bounds = (0, None)  
x2_bounds = (0, None)  

result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

optimal_quantities = result.x
total_profit = -result.fun


print(f"Optimal production quantities:")
print(f"Product A: {optimal_quantities[0]:.2f} units")
print(f"Product B: {optimal_quantities[1]:.2f} units")
print(f"Product C: {optimal_quantities[2]:.2f} units")
print(f"Total Profit: ${total_profit:.2f}")

# Simulate 10% increase in raw material (increase 180 kg by 10%)
new_b = [240, 180 * 1.1] 

# Solve again with the new raw material constraint
result_with_increased_material = linprog(c, A_ub=A, b_ub=new_b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

new_optimal_quantities = result_with_increased_material.x
new_total_profit = -result_with_increased_material.fun

# Print new results
print("\nAfter increasing raw material by 10%:")
print(f"Product A: {new_optimal_quantities[0]:.2f} units")
print(f"Product B: {new_optimal_quantities[1]:.2f} units")
print(f"Product C: {new_optimal_quantities[2]:.2f} units")
print(f"New Total Profit: ${new_total_profit:.2f}")

# Comparison table
print("\nComparison Table:")
print(f"{'Product':<10} {'Original Units':<15} {'New Units':<15} {'Profit Contribution ($)'}")
products = ['A', 'B', 'C']
for i in range(3):
    print(f"{products[i]:<10} {optimal_quantities[i]:<15.2f} {new_optimal_quantities[i]:<15.2f} {((new_optimal_quantities[i] - optimal_quantities[i]) * [30, 20, 50][i]):<20.2f}")
