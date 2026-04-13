#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30402
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s: list[int] = [0]
        prefix: dict[int, int] = {0: 1}
        cnt = 0
        for i in range(len(nums)):
            s.append(s[i] + nums[i])
            if s[i + 1] - k in prefix:
                cnt += prefix.get(s[i + 1] - k, 0)
            prefix[s[i + 1]] = prefix.get(s[i + 1], 0) + 1

        return cnt


# @lc code=end


#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#
