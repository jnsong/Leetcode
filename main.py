# class Solution:
#     def numDecodings(s):
#         # case 1 digit
#         # f(n) = (==0, +0) (!=0, +1) + f(n-1)
#         # case 2: 2 digits
#         # f(n) = (<=26 +1) (>26 +0; starting with 0 +0) + f(n-2)
#         n = len(s)
#         if n == 1:
#             if s[n] == '0':
#                 return 0
#             else:
#                 return 1
#         if n == 2:
#             if s[n]*10 + s[n-1] >26:
#                 return 0
#             elif s[n-1] == 0:
#                 return 0
#         return

class Solution:
    def numDecodings(s):
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

a = Solution.numDecodings("111111111111111111111111111111111111111111111")

print(a)