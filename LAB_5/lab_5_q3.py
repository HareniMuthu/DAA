def pylons(k, arr):
    n = len(arr)
    plants_count = 0
    last_plant = -1
    
    i = 0
    while i < n:
        # Find the furthest possible location for the current power plant
        plant_loc = min(i + k - 1, n - 1)
        
        # Check if the current power plant location is suitable
        while plant_loc > last_plant:
            if arr[plant_loc] == 1:
                break
            plant_loc -= 1
        
        # If no suitable location found within the distribution range, return -1
        if plant_loc == last_plant:
            return -1
        
        # Place a power plant and update counters
        plants_count += 1
        last_plant = plant_loc + k - 1
        i = last_plant + 1
    
    return plants_count

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(pylons(k, arr))
