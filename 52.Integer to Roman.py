def intToRoman(num):
    # Create a mapping from integer values to Roman numeral symbols
    mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    result = ''

    # Iterate through the mapping
    for value, symbol in mapping.items():
        while num >= value:
            result += symbol
            num -= value

    return result


# Example usage
print(intToRoman(3))  # Output: "III"
print(intToRoman(58))  # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"
