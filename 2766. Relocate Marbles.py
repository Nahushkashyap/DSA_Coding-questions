# Question :- https://leetcode.com/problems/relocate-marbles/
class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        nums = set(nums)
        for i in range(len(moveFrom)):
            moveToPosition = moveTo[i]
            moveFromPosition = moveFrom[i]
            if moveToPosition == moveFromPosition:
                continue
            nums.add(moveToPosition)
            nums.remove(moveFromPosition)
        nums = list(nums)
        nums.sort()
        return nums
