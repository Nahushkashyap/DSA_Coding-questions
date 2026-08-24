from collections import deque


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_even = []
        nums_odd = []
        target_even = []
        target_odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
            if target[i] % 2 == 0:
                target_even.append(target[i])
            else:
                target_odd.append(target[i])
        nums_even.sort()
        nums_odd.sort()
        target_even.sort()
        target_odd.sort()
        number_difference = 0
        for i in range(len(nums_odd)):
            number_difference += abs(nums_odd[i] - target_odd[i])
        for i in range(len(target_even)):
            number_difference += abs(target_even[i] - nums_even[i])
        return int(number_difference / 4)
