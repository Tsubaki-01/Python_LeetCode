#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30402
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        hash_table = {}

        def dfs(node):
            if not node:
                return None
            if node in hash_table:
                return hash_table[node]
            copy_node = Node(node.val)
            hash_table[node] = copy_node
            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)
            return copy_node

        return dfs(head)


# @lc code=end


#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#
