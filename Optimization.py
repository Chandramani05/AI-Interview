import numpy as np
from scipy.optimize import linprog

# Problem Definition:
# Details:
# Product A: Profit per unit = $30, Labor hours per unit = 5, Raw material per unit = 3 kg
# Product B: Profit per unit = $20, Labor hours per unit = 4, Raw material per unit = 2 kg
# Product C: Profit per unit = $50, Labor hours per unit = 6, Raw material per unit = 4 kg

# Constraints:
# 1. Labor hours: 5A + 4B + 6C <= 240
# 2. Raw materials: 3A + 2B + 4C <= 180
# 3. Non-negativity: A, B, C >= 0

# Objective:
# Maximize profit: Profit = 30A + 20B + 50C

# Coefficients for the objective function (negative because we want to maximize profit)
c = [-30, -20, -50]

A = [
    [5, 4, 6],  # Labor hours
    [3, 2, 4]   # Raw material
]
b = [240, 180] 

x_bounds = [(0, None), (0, None), (0, None)]  # Product A, B, C

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

optimal_quantities = result.x
total_profit = -result.fun

# Print optimal production quantities and profit
print(f"Optimal production quantities:")
print(f"Product A: {optimal_quantities[0]:.2f} units")
print(f"Product B: {optimal_quantities[1]:.2f} units")
print(f"Product C: {optimal_quantities[2]:.2f} units")
print(f"Total Profit: ${total_profit:.2f}")

# Simulate 10% increase in raw material (increase 180 kg by 10%)
new_b = [240, 180 * 1.1]  # Update raw material constraint

# Solve again with the new raw material constraint
result_with_increased_material = linprog(c, A_ub=A, b_ub=new_b, bounds=x_bounds, method='highs')

# Output the new results
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



#Output
"""
Comparison Table:
Product    Original Units  New Units       Profit Contribution ($)
A          0.00            0.00            0.00                
B          0.00            0.00            0.00                
C          40.00           40.00           0.00                
(image) chandramaniyadav@Chandramanis-MacBook-Pro Job Application % python Optimization.py   
Optimal production quantities:
Product A: 0.00 units
Product B: 0.00 units
Product C: 40.00 units
Total Profit: $2000.00

After increasing raw material by 10%:
Product A: 0.00 units
Product B: 0.00 units
Product C: 40.00 units
New Total Profit: $2000.00

Comparison Table:
Product    Original Units  New Units       Profit Contribution ($)
A          0.00            0.00            0.00                
B          0.00            0.00            0.00                
C          40.00           40.00           0.00                
"""
