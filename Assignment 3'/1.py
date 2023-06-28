def threeSumClosest(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return target  # If the sum is equal to target, return the target

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum

# Example usage
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)
