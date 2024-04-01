def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], intervals[i][1]))
        else:
            merged.append(intervals[i])
    return merged

# Example
intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
print(merge_intervals(intervals))
