#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30402
#
# [41] 缺失的第一个正数
#

# @lc code=start


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > len(nums) or nums[i] < 0:
                continue
            while (0 < nums[i] <= len(nums)) and (nums[nums[i] - 1] != nums[i]):
                help = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = help

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


# @lc code=end


#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#
