class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r, value in enumerate(nums):
            if value != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        #return nums
