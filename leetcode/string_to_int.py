# https://leetcode.com/problems/string-to-integer-atoi/
# Input: s = "4193 with words"
# Output: 4193
class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading and trailing whitespaces
        s = s.strip()

        # Check if the string is empty
        if not s:
            return 0

        # Initialize variables
        sign, result, i = 1, 0, 0

        # Check if the first character is a sign (+/-)
        if s[0] in ['+', '-']:
            sign = 1 if s[0] == '+' else -1
            i = 1

        # Iterate over the remaining characters
        for j in range(i, len(s)):
            # Check if the character is a digit
            if not s[j].isdigit():
                break
            result = result * 10 + int(s[j])

        # Apply the sign and clamp the result
        result *= sign
        result = max(min(result, 2**31-1), -2**31)

        return result
