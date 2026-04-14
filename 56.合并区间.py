#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30402
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        print(sorted_intervals)

        if len(intervals) == 1:
            return intervals

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] <= sorted_intervals[i - 1][1]:
                sorted_intervals[i][0] = sorted_intervals[i - 1][0]
                if sorted_intervals[i][1] < sorted_intervals[i - 1][1]:
                    sorted_intervals[i][1] = sorted_intervals[i - 1][1]
            else:
                res.append(sorted_intervals[i - 1])

        res.append(sorted_intervals[-1])

        return res


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,7],[1,4]]\n
# @lcpr case=end

#
