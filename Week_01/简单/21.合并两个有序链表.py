#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 迭代
        # prehead = ListNode(-1)
        # pre = prehead
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         pre.next = l1
        #         l1 = l1.next
        #     else:
        #         pre.next = l2
        #         l2 = l2.next
        #     pre = pre.next
        # pre.next = l1 if l1 is not None else l2
        # return prehead.next

        # 2. 递归
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# @lc code=end

