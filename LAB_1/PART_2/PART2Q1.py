import time
import random
import matplotlib.pyplot as plt
import heapq

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for num in arr:
        idx = num // 1000
        buckets[idx].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

# Generate 1000 random numbers between 1 and 10000
numbers = [random.randint(1, 10000) for _ in range(1000)]

# Bubble Sort
start_time = time.time()
bubble_sort(numbers.copy())
bubble_sort_time = time.time() - start_time

# Selection Sort
start_time = time.time()
selection_sort(numbers.copy())
selection_sort_time = time.time() - start_time

# Insertion Sort
start_time = time.time()
insertion_sort(numbers.copy())
insertion_sort_time = time.time() - start_time

# Merge Sort
start_time = time.time()
merge_sort(numbers.copy())
merge_sort_time = time.time() - start_time

# Quick Sort
start_time = time.time()
quick_sort(numbers.copy())
quick_sort_time = time.time() - start_time

# Heap Sort
start_time = time.time()
heap_sort(numbers.copy())
heap_sort_time = time.time() - start_time

# Bucket Sort
start_time = time.time()
bucket_sort(numbers.copy())
bucket_sort_time = time.time() - start_time

# Radix Sort
start_time = time.time()
radix_sort(numbers.copy())
radix_sort_time = time.time() - start_time

# Plotting
labels = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Bucket Sort', 'Radix Sort']
times = [bubble_sort_time, selection_sort_time, insertion_sort_time, merge_sort_time, quick_sort_time, heap_sort_time, bucket_sort_time, radix_sort_time]

plt.bar(labels, times)
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (s)')
plt.title('Comparison of Sorting Algorithms')
plt.xticks(rotation=45)
plt.show()
