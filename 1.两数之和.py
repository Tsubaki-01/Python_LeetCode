#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30402
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic: dict[int, int] = {}
        for i, num in enumerate(nums):
            if target - num in dic.keys():
                return [dic[target - num], i]
            dic[num] = i


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
