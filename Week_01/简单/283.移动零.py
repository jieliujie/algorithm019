#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
# 双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        slow = 0
        for i in range(nums_size):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
            

# @lc code=end

