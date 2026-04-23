#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30402
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key=0, value=0, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy

    def get(self, key: int) -> int:
        node = self.get_node(key)
        if node:
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.dummy.pre.key]
                self.remove_node(self.dummy.pre)
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.push_to_front(new_node)

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def push_to_front(self, node):
        node.next = self.dummy.next
        node.pre = self.dummy
        self.dummy.next.pre = node
        self.dummy.next = node

    def get_node(self, key):
        if key in self.cache.keys():
            node = self.cache[key]
            self.remove_node(node)
            self.push_to_front(node)
            return node
        else:
            return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


#
# @lcpr case=start
# ["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]\n
# @lcpr case=end

#
