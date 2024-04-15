def maximize_sum(arr):
    # Sort the array
    arr.sort()

    # Initialize the sum
    max_sum = 0

    # Calculate the sum of products
    for i in range(len(arr)):
        max_sum += arr[i] * i

    return max_sum

# Test case
arr = [2, 5, 3, 4, 0]
maximized_sum = maximize_sum(arr)
print("Maximum sum:", maximized_sum)
