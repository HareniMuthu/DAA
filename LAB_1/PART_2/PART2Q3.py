import heapq

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

# Example
arr = [1, 23, 12, 9, 30, 2, 50, 99,44 ,78 ,33 ,36 ,91 ,22 ,29]
k = 3
print(find_k_largest(arr, k))
