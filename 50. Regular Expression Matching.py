def isMatch(s, p):
    m, n = len(s), len(p)

    # DP table initialization
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Initialize dp[0][j] for patterns like a*, a*b*, a*b*c* etc.
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)
            else:
                dp[i][j] = dp[i - 1][j - 1] if p[j - 1] == '.' or p[j - 1] == s[i - 1] else False

    return dp[m][n]


# Example usage
print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b"))  # Output: True
print(isMatch("mississippi", "mis*is*p*."))  # Output: False
