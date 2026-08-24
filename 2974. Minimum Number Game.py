class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums.sort(reverse=True)
        for i in range(0, len(nums) - 1, 2):
            ans[i + 1] = nums.pop()
            ans[i] = nums.pop()
        return ans
