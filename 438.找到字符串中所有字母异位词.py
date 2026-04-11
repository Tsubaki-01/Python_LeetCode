#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30402
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        # 统计目标字符串p的字符频次
        target = [0] * 26
        for c in p:
            target[ord(c) - ord("a")] += 1

        window = [0] * 26
        res = []

        # 初始化第一个窗口
        for i in range(len_p):
            window[ord(s[i]) - ord("a")] += 1
        if window == target:
            res.append(0)

        # 滑动窗口遍历
        for i in range(1, len_s - len_p + 1):
            # 移除左边界、添加右边界
            window[ord(s[i - 1]) - ord("a")] -= 1
            window[ord(s[i + len_p - 1]) - ord("a")] += 1
            if window == target:
                res.append(i)

        return res


# @lc code=end


#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#
