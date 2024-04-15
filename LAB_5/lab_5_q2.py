def maximumPeople(population, towns, clouds, ranges):
    n = len(towns)
    m = len(clouds)
    
    # Calculate the total population initially in sunny towns
    sunny_population = sum(population)
    
    # Initialize maximum sunny population
    max_sunny_population = sunny_population
    
    # Iterate through each cloud
    for i in range(m):
        cloud_population = 0
        
        # Calculate the range of towns covered by the current cloud
        left_boundary = clouds[i] - ranges[i]
        right_boundary = clouds[i] + ranges[i]
        
        # Simulate removal of the current cloud and calculate population left in darkness
        for j in range(n):
            if left_boundary <= towns[j] <= right_boundary:
                cloud_population += population[j]
        
        # Calculate the population in sunny towns after removing the current cloud
        sunny_population_after_removal = sunny_population - cloud_population
        
        # Update maximum sunny population
        max_sunny_population = max(max_sunny_population, sunny_population_after_removal)
    
    return max_sunny_population

# Read input
n = int(input())
population = list(map(int, input().split()))
towns = list(map(int, input().split()))
m = int(input())
clouds = list(map(int, input().split()))
ranges = list(map(int, input().split()))

# Output
print(maximumPeople(population, towns, clouds, ranges))
