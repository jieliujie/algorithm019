#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1. 双指针（快慢指针）
        nums_size = len(nums)
        slow, fast = 0, 1
        while fast < nums_size:
            if nums[slow] != nums[fast]:
                slow += 1
                # 不等的时候要将后面不等的数字移到前面来
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
        return slow + 1
# @lc code=end

