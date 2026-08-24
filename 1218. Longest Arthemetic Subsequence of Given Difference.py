# Question :- https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 0:
            return 0
        dp = {}
        ans = 1
        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
                ans = max(ans, dp[i])
                continue
            dp[i] = 1

        return ans
