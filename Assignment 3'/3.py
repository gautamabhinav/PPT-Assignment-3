def nextPermutation(nums):
    # Find the first pair of consecutive elements where nums[i] < nums[i+1]
    idx1 = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            idx1 = i
            break

    if idx1 == -1:
        nums.reverse()  # Array is in descending order, reverse it
        return

    # Find the first element greater than nums[idx1] starting from the right end
    idx2 = -1
    for i in range(len(nums) - 1, idx1, -1):
        if nums[i] > nums[idx1]:
            idx2 = i
            break

    # Swap elements at indices idx1 and idx2
    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    # Reverse the subarray starting from idx1+1 to the end
    left = idx1 + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)
