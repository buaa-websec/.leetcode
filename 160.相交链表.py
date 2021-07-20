#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 先遍历一个链表将链表的所有值都存到Hashset中，然后再遍历另一个链表，如果发现某个结点在Hashset中已经存在那我们直接返回该节点即可
        # 利用双指针，当某一指针遍历完链表之后，然后掉头去另一个链表的头部，继续遍历。因为速度相同所以他们第二次遍历的时候肯定会相遇
        a = headA
        b = headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
# @lc code=end

