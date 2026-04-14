#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30402
#
# [238] 除了自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        suffix = [1] * (len(nums))
        t_1 = 1
        t_2 = 1
        for i in range(1, len(nums)):
            t_1 *= nums[i - 1]
            t_2 *= nums[-i]
            prefix[i] = t_1
            suffix[-i - 1] = t_2

        print(prefix)
        print(suffix)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
