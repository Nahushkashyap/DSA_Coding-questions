# Question:- https://leetcode.com/problems/max-consecutive-ones-iii

from collections import deque


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = k
        i = 0
        j = 0
        flip_indices = deque()
        while i < len(nums):
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 0:
                if k > 0:
                    flip_indices.append(i)
                    i += 1
                    k -= 1
                    continue

                ans = max(ans, i - j)
                if len(flip_indices) > 0:
                    j = flip_indices[0] + 1
                    k += 1
                    flip_indices.popleft()
                    continue
                i += 1
                j = i

        ans = max(ans, i - j)
        return ans
