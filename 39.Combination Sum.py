from typing import List


# Question :- https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sumVal = 0

        def backtracking(target, candidate, sumVal, candidateArr, indexVal, ans):
            if sumVal == target:
                ans.append(candidateArr[:])
                return
            if sumVal > target:
                return
            if indexVal >= len(candidate):
                return
            candidateArr.append(candidate[indexVal])
            backtracking(
                target,
                candidate,
                sumVal + candidate[indexVal],
                candidateArr,
                indexVal,
                ans,
            )
            candidateArr.pop()
            notpick = backtracking(
                target, candidate, sumVal, candidateArr, indexVal + 1, ans
            )

        backtracking(target, candidates, 0, [], 0, ans)
        return ans
