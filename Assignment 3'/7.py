def findMissingRanges(nums, lower, upper):
    missingRanges = []
    start = lower

    for num in nums:
        if num > start:
            missingRanges.append(getRange(start, num - 1))
        start = num + 1

    if start <= upper:
        missingRanges.append(getRange(start, upper))

    return missingRanges

def getRange(start, end):
    if start == end:
        return str(start) + "->" + str(end)
    else:
        return str(start) + "->" + str(end)

# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
