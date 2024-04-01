import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [random.randint(1, 1000) for _ in range(10000)]
search_keys = [random.randint(1, 1000) for _ in range(5)]

linear_times = []
binary_times = []

for key in search_keys:
    start_time = time.time()
    linear_search(arr, key)
    linear_times.append(time.time() - start_time)

    start_time = time.time()
    binary_search(arr, key)
    binary_times.append(time.time() - start_time)

plt.plot(range(5), linear_times, label='Linear Search')
plt.plot(range(5), binary_times, label='Binary Search')
plt.xlabel('Search Number')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
