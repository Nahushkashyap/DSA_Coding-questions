# Question:- https://leetcode.com/problems/rotated-digits/
class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotatedDict = {
            "0": "0",
            "1": "1",
            "8": "8",
            "2": "5",
            "5": "2",
            "6": "9",
            "9": "6",
        }

        def canBeRotated(num, rotatedDict):
            numStr = str(num)
            rotatedStr = ""
            for i in numStr:
                if i not in rotatedDict:
                    return False
                rotatedStr += rotatedDict[i]
            return rotatedStr != numStr

        count = 0
        for i in range(1, n + 1):
            if canBeRotated(i, rotatedDict):
                count += 1
        return count
