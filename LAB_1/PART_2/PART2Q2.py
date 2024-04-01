import heapq

def merge_sorted_lists(arrays):
    heap = []
    result = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    while heap:
        val, arr_idx, idx = heapq.heappop(heap)
        result.append(val)
        if idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, idx + 1))
    
    return result

# Example
m = 3
n = 4
arrays = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93],[32, 33]]
print(merge_sorted_lists(arrays))
