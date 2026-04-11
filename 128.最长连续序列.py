#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30402
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        tmp = []
        longest = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            tmp.append(num)
        for num in tmp:
            len = 1
            while num + 1 in num_set:
                len += 1
                num += 1
            longest = max(longest, len)
        return longest


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#
