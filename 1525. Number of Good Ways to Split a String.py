from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        s_left = defaultdict(int)
        s_right = defaultdict(int)
        for i in s:
            s_right[i] += 1
        for i in range(len(s)):
            s_left[s[i]] += 1
            s_right[s[i]] -= 1
            if s_right[s[i]] <= 0:
                s_right.pop(s[i])
            if len(s_left) == len(s_right):
                ans += 1
        return ans
