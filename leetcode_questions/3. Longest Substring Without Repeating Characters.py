# Question :- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        subStrSet = {}
        i = 0
        subStrCount = 0
        while i < len(s):
            if s[i] not in subStrSet:
                subStrSet[s[i]] = i
                subStrCount += 1
                i += 1
            else:
                i = subStrSet[s[i]] + 1
                subStrSet = {}
                ans = max(ans, subStrCount)
                subStrCount = 0
        ans = max(ans, subStrCount)
        return ans
