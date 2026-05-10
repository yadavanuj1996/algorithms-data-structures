class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode s[0..i] (i.e., s[0:i+1])
        # dp[i] = dp[i-1] + dp[i-2] where:
        #   dp[i-1]: valid if s[i] != '0' (current char decoded as single digit 1-9)
        #   dp[i-2]: valid if s[i-1:i+1] is a two-digit code between 10-26
        # One digit valid check: s[i] != '0'
        # Two digit valid check: 10 <= int(s[i-1:i+1]) <= 26
        n = len(s)
        dp = [0] * n

        dp[0] = 1 if s[0] != "0" else 0
        if n > 1:
            dp[1] = dp[0] if int(s[1]) != 0 else 0 # no of way to decode s[0..1] is no of ways to reach s[1] from s[0] + no of ways to take s[0] and s[1] combined
            dp[1] += 1 if int(s[0:2]) >= 10 and int(s[0:2]) <= 26 else 0

        for cur_index in range(2, n):
            prev_index = cur_index - 1
            prev_prev_index = cur_index - 2

            # 110 (11, 0 ) is not valid so we are checking cur index char should not be 0
            dp[cur_index] = dp[prev_index] if int(s[cur_index]) != 0 else 0
            # here combined prev char + cur char and if these 2 digits are valid then no of ways to reach to this (combined 2 digit code) is no of ways to reach 1 digit before the combined digit and same no
            # will be here as well if combined digit is valid as no of ways to reach combined digit from pre prev char will be same (as there is only one way from there to here)
            dp[cur_index] += dp[prev_prev_index] if int(s[prev_index: cur_index+1]) >= 10 and int(s[prev_index: cur_index+1]) <= 26 else 0


        return dp[n-1]
