def myAtoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    i = 0
    n = len(s)
    sign = 1
    result = 0

    # Step 1: Ignore leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Check for optional sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Step 3: Read digits and form the number
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # Step 4: Check for overflow and clamp if necessary
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        i += 1

    return sign * result


# Example usage
print(myAtoi("42"))  # Output: 42
print(myAtoi("   -42"))  # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987"))  # Output: 0
print(myAtoi("-91283472332"))  # Output: -2147483648 (clamped to INT_MIN)
