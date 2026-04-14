#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30402
#
# [53] 最大子数组和
#


# ===================
#   窗口不是单调的，不用滑动窗口
# ===================

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        res = dp[0]

        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
            res = max(res, dp[i])

        return res


# @lc code=end


#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#
