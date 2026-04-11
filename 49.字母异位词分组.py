#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30402
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_dict: dict[tuple, list[str]] = {}

        def get_tuple(s: str) -> tuple:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            return tuple(count)

        for s in strs:
            tup = get_tuple(s)
            if tup not in tuple_dict:
                tuple_dict[tup] = []
            tuple_dict[tup].append(s)
        return list(tuple_dict.values())


# @lc code=end


#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#
