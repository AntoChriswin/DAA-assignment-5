def romanToInt(s):
    # Create a mapping from Roman numeral symbols to integer values
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string
    for char in s:
        value = mapping[char]
        # If the current value is less than the value of the next character, subtract it
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total


# Example usage
print(romanToInt("III"))  # Output: 3
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
