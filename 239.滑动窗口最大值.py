#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30402
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque  # 这里加


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return [max(nums)]

        l = deque()  # 这里改！

        def insert(l: deque, n: int):
            while l and l[-1] < n:
                l.pop()
            l.append(n)

        def pop(l: deque, n: int):
            if l[0] == n:
                l.popleft()  # 这里也改，O(1)

        # 初始化第一个窗口
        for i in range(k):
            insert(l, nums[i])

        res = [l[0]]

        # 滑动窗口
        for i in range(1, len(nums) - k + 1):
            pop(l, nums[i - 1])
            insert(l, nums[i + k - 1])
            res.append(l[0])

        return res


# @lc code=end


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
