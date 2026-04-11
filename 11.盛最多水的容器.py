#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30402
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def square(a: int, b: int) -> int:
            return abs(a - b) * min(height[a], height[b])

        left = 0
        right = len(height) - 1
        S = square(left, right)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            S = max(S, square(left, right))

        return S


# @lc code=end


#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
