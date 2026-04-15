#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30402
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            current = head
            next = head.next
            next_next = next.next
            next.next = current
            current.next = self.swapPairs(next_next)
            return next
        else:
            return head


# @lc code=end


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(pre, current):
            next = current.next
            if next:
                next_next = next.next
                pre.next = next
                next.next = current
                current.next = next_next

        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            swap(pre, pre.next)
            pre = pre.next.next

        return dummy.next


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
