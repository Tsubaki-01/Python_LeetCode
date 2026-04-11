#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30402
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hash_set = set()
        res = 0
        tmp = 0

        if (len(s) == 1) or (len(s) == 0):
            return len(s)

        while right < len(s):
            if s[right] not in hash_set:
                tmp += 1
                hash_set.add(s[right])
            else:
                while s[left] != s[right]:
                    hash_set.remove(s[left])
                    tmp -= 1
                    left += 1
                left += 1

            right += 1
            res = max(res, tmp)

        return res


# @lc code=end


#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
