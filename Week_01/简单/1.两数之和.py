#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# # 暴力
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if nums is None:
#             return []
#         nums_size = len(nums)
#         for i in range(nums_size - 1):
#             for j in range(i + 1, nums_size):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

# 哈希
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        hashtable = {}
        for i, n in enumerate(nums):
            other_num = target - nums[i]
            if other_num in hashtable:
                return [hashtable[other_num], i]
            hashtable[n] = i
        return []


# @lc code=end
