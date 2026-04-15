#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30402
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry, num = divmod(sum, 10)
            tail.next = ListNode(val=num)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            carry, num = divmod(sum, 10)
            tail.next = ListNode(val=num)
            tail = tail.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            carry, num = divmod(sum, 10)
            tail.next = ListNode(val=num)
            tail = tail.next
            l2 = l2.next
        if carry:
            tail.next = ListNode(val=carry)
            tail = tail.next

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
