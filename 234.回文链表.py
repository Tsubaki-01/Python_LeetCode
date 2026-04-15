#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30402
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        current = head
        len = 0
        while current is not None:
            len += 1
            current = current.next

        dummy = ListNode(next=head)
        current = head
        pre = dummy

        for i in range(len // 2):
            next = current.next
            current.next = pre
            pre = current
            current = next
        head.next = None

        if len % 2 == 1:
            current = current.next

        while current is not None:
            if current.val != pre.val:
                return False
            current = current.next
            pre = pre.next

        return True


# @lc code=end


#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#
