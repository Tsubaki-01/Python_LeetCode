#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30402
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        dp = []
        dp.append(0)
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp.append(max(dp[i - 1], prices[i] - min_price))
        return dp[-1]


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
