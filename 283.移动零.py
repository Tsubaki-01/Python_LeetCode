#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30402
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
            right += 1


# @lc code=end


#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
