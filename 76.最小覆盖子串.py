#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30402
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        need = defaultdict(int)  # t 需要的字符和数量
        window = defaultdict(int)  # 当前窗口里的字符和数量

        # 统计目标字符需求
        for ch in t:
            need[ch] += 1

        left = 0
        valid = 0  # 已经满足数量的字符种类
        start = 0
        min_len = float("inf")

        # 右指针一直向右扩展
        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                window[ch] += 1
                # 数量刚好匹配时，有效种类+1
                if window[ch] == need[ch]:
                    valid += 1

            # 窗口满足条件，开始收缩左指针，尽量变短
            while valid == len(need):
                # 更新最小窗口
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                # 左指针右移，移除字符
                left_ch = s[left]
                left += 1

                if left_ch in need:
                    if window[left_ch] == need[left_ch]:
                        valid -= 1
                    window[left_ch] -= 1

        # 没找到返回空字符串
        return s[start : start + min_len] if min_len != float("inf") else ""


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
