def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort the intervals based on the start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False  # Overlapping intervals found

    return True  # No overlapping intervals found

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)
