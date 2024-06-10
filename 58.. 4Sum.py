def fourSum(nums, target):
    nums.sort()  # Sort the array
    n = len(nums)
    result = []

    # Iterate through the array
    for i in range(n):
        # Skip duplicates for nums[i]
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Update target_3 for current nums[i]
        target_3 = target - nums[i]

        for j in range(i + 1, n - 2):
            # Skip duplicates for nums[j]
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Initialize two pointers
            left, right = j + 1, n - 1

            while left < right:
                total = nums[j] + nums[right]

                if total == target_3 - nums[left]:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for nums[left] and nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target_3 - nums[left]:
                    left += 1
                else:
                    right -= 1

    return result


# Example usage
print(fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(fourSum([2, 2, 2, 2, 2], 8))  # Output: [[2, 2, 2, 2]]
