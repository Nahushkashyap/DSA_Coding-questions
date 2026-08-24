from collections import defaultdict

# Question :- https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        stringDict1 = defaultdict(int)
        stringDict2 = defaultdict(int)
        diffCount = 0
        for i in range(len(s1)):
            stringDict1[s1[i]] += 1
            stringDict2[s2[i]] += 1
            if s1[i] != s2[i]:
                diffCount += 1
        if stringDict1 == stringDict2 and diffCount <= 2:
            return True
        return False
