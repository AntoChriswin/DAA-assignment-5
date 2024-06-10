def two_sum(nums, target):
    # Initialize a dictionary to store value and its index
    num_to_index = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # If found, return the indices
            return [num_to_index[complement], i]

        # Otherwise, add the current number and its index to the dictionary
        num_to_index[num] = i


# Example usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
print(two_sum([3, 3], 6))  # Output: [0, 1]
