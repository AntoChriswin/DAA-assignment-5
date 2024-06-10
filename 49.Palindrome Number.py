def is_palindrome(x):
    # Special cases:
    # When x is negative, it cannot be a palindrome
    # When x ends with 0, it cannot be a palindrome unless x is 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10


# Example usage
print(is_palindrome(121))  # Output: true
print(is_palindrome(-121))  # Output: false
print(is_palindrome(10))  # Output: false
print(is_palindrome(12321))  # Output: true
