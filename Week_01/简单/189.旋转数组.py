#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 暴力（超时）
        # nums_size = len(nums)
        # k %= nums_size
        # for i in range(k):
        #     temp = nums[nums_size - 1]
        #     for j in range(nums_size - 2, -1, -1):
        #         nums[j+1] = nums[j]
        #     nums[0] = temp

        #2. 使用反转
        nums_size = len(nums)
        k %= nums_size
        # 切片是一种浅拷贝的方式，所以这里只能用自己定义的 reverse 方法
        # nums[:].reverse()
        # nums[0:k].reverse()
        # nums[k:nums_size].reverse()
        # 使用自定义 reverse
        self.reverse(nums, 0, nums_size - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nums_size - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# @lc code=end

