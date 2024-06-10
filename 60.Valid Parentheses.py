def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False

    return not stack


# Example usage
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
