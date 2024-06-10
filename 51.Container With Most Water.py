def maxArea(height):
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        # Calculate the area
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example usage
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(maxArea([1, 1]))  # Output: 1
