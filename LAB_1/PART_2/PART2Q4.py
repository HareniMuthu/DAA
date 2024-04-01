def max_activities(activities):
    # Sort activities based on finishing time
    activities.sort(key=lambda x: x[1])
    
    # Initialize variables
    count = 1
    end_time = activities[0][1]
    selected_activities = [activities[0]]
    
    # Iterate through activities and select each if its starting time is after the end time of the previous activity
    for i in range(1, len(activities)):
        if activities[i][0] >= end_time:
            count += 1
            end_time = activities[i][1]
            selected_activities.append(activities[i])
    
    return selected_activities

# Example
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = max_activities(activities)
print(selected_activities)
