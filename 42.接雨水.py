#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30402
#
# [42] 接雨水
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom_h = height[stack.pop()]
                if not stack:
                    break
                distance = i - stack[-1] - 1
                H_S = min(h, height[stack[-1]]) - bottom_h

                ans += distance * H_S

            stack.append(i)

        return ans


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
