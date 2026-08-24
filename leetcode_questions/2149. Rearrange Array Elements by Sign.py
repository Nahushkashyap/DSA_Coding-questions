class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_pointer = 0
        negative_pointer = 0
        length_of_array = len(nums)
        ans = [0] * length_of_array
        count = 0
        while count < length_of_array:
            if nums[positive_pointer] > 0:
                ans[count] = nums[positive_pointer]
                count += 1
                positive_pointer += 1
            else:
                while nums[positive_pointer] < 0:
                    positive_pointer += 1
                ans[count] = nums[positive_pointer]
                count += 1
                positive_pointer += 1
            if nums[negative_pointer] < 0:
                ans[count] = nums[negative_pointer]
                count += 1
                negative_pointer += 1
            else:
                while nums[negative_pointer] > 0:
                    negative_pointer += 1
                ans[count] = nums[negative_pointer]
                count += 1
                negative_pointer += 1
        return ans
