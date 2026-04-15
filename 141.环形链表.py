#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30402
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        fast = head
        slow = head
        while fast is not None and slow is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            if fast == slow:
                return True

        return False


# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#
