#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30402
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        def reverse(pre, current):
            current.next = pre

        dummy = ListNode(next=head)
        current = head
        pre = dummy
        while current is not None:
            next = current.next
            reverse(pre, current)
            pre = current
            current = next
        head.next = None
        return pre


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
