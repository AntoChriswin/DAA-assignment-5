def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Initialize the prefix as the first string in the array
    prefix = strs[0]

    # Iterate through the remaining strings in the array
    for string in strs[1:]:
        # Compare characters of the current string with the prefix
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        # Update the prefix to the common characters found so far
        prefix = prefix[:i]
        # If the prefix becomes empty, break the loop
        if not prefix:
            break

    return prefix


# Example usage
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
