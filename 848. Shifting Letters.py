# Question :- https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        shiftVal = 0
        for i in range(1, len(s) + 1):
            startingNum = ord(s[-i]) - 96
            shiftVal += shifts[-i]
            sumVal = shiftVal + startingNum
            sumVal %= 26
            if sumVal == 0:
                sumVal = 26
            s[-i] = chr(sumVal + 96)
        return "".join(s)
