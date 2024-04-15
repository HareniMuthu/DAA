def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    knapsack = []

    for value, weight in items:
        if weight <= capacity:
            # Take the whole item if it fits
            knapsack.append((value, weight))
            total_value += value
            capacity -= weight
        else:
            # Take a fraction of the item if it doesn't fit completely
            fraction = capacity / weight
            knapsack.append((value * fraction, weight * fraction))
            total_value += value * fraction
            break

    return total_value, knapsack

# Test case
items = [(10, 2), (15, 5), (20, 4)]
capacity = 8
optimal_value, optimal_knapsack = fractional_knapsack(items, capacity)

print("Optimal value:", optimal_value)
print("Optimal knapsack contents:")
for value, weight in optimal_knapsack:
    print("Value:", value, " Weight:", weight)
