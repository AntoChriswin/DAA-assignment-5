def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        current_char = s[end]

        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1

        char_index_map[current_char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))  # Output: 1
print(length_of_longest_substring("pwwkew"))  # Output: 3
