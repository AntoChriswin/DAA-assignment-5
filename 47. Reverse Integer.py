def reverse(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    result = 0
    negative = x < 0
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow before actually appending the digit
        if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return 0

        result = result * 10 + digit

    if negative:
        result = -result

    return result if INT_MIN <= result <= INT_MAX else 0


# Example usage
print(reverse(123))  # Output: 321
print(reverse(-123))  # Output: -321
print(reverse(120))  # Output: 21
print(reverse(1534236469))  # Output: 0 (since it will overflow)

