#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30402
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head

        for _ in range(k):
            if tmp is None:
                return head
            tmp = tmp.next

        dummy = ListNode(0, head)
        pre = dummy
        current = head
        while current != tmp:
            next = current.next
            current.next = pre
            pre = current
            current = next
        head.next = self.reverseKGroup(current, k)

        return pre


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
