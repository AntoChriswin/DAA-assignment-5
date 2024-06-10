def letterCombinations(digits):
    if not digits:
        return []

    # Create a mapping from digits to their corresponding letters
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def backtrack(combination, index):
        if len(combination) == len(digits):
            result.append(combination)
            return

        current_digit = digits[index]
        for letter in mapping[current_digit]:
            backtrack(combination + letter, index + 1)

    result = []
    backtrack('', 0)
    return result


# Example usage
print(letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))  # Output: []
print(letterCombinations("2"))  # Output: ["a","b","c"]
