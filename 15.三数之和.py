#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30402
#
# [15] 三数之和
#

# @lc code=start
# 双指针
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        if sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []
        results = set()

        for i, num in enumerate(sorted_nums):
            target = 0 - num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if sorted_nums[left] + sorted_nums[right] == target:
                    results.add((num, sorted_nums[left], sorted_nums[right]))
                    left += 1
                    right -= 1
                if sorted_nums[left] + sorted_nums[right] > target:
                    right -= 1
                if sorted_nums[left] + sorted_nums[right] < target:
                    left += 1

        return list(results)


# @lc code=end


# 双指针++
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        if sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []

        results = set()
        for i, num in enumerate(sorted_nums):
            target = 0 - num
            num_set = set()
            for t in sorted_nums[i + 1 :]:
                if target - t in num_set:
                    results.add((num, t, target - t))
                num_set.add(t)

        return list(results)


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
