def candies(n, arr):
    # Initialize candies array with all 1's
    candy_counts = [1] * n
    
    # Traverse from left to right
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            candy_counts[i] = candy_counts[i-1] + 1
    
    # Traverse from right to left
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            candy_counts[i] = max(candy_counts[i], candy_counts[i+1] + 1)
    
    # Return the sum of candy counts
    return sum(candy_counts)

# Take input from the user
n = int(input())
arr = [int(input()) for _ in range(n)]

# Calculate and print the minimum number of candies Alice must buy
min_candies = candies(n, arr)
print(min_candies)
