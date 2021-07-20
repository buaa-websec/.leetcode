#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if head is None or head.next is None:
        #     return head
        slow = None
        fast = head
        while fast:
            temp = fast
            fast =fast.next
            temp.next = slow
            slow = temp
        return slow
# @lc code=end

