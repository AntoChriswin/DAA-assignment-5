def threeSumClosest(nums, target):
    nums.sort()  # Sort the array
    n = len(nums)
    closest_sum = float('inf')

    # Iterate through the array
    for i in range(n):
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            # Update the closest sum
            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return closest_sum

    return closest_sum


# Example usage
print(threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(threeSumClosest([0, 0, 0], 1))  # Output: 0

