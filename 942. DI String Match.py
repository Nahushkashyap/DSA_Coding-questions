class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        max_value = len(s)
        min_value = 0
        ans = [0] * (max_value + 1)
        for i in range(len(s)):
            if s[i] == "I":
                ans[i] = min_value
                min_value += 1
            else:
                ans[i] = max_value
                max_value -= 1
        if s[-1] == "D":
            ans[-1] = min_value
        else:
            ans[-1] = max_value
        return ans
