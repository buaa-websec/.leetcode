#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 设置一个新的指针，从头节点出发，慢指针速度为1，所以可以使用慢指针从相遇点出发
                new = head
                while new is not slow:
                    slow = slow.next
                    new = new.next
                return slow   
        
# @lc code=end

