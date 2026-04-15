#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30402
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        k = (n + 1) // 2
        print(k)

        for t in range(k):
            for i in range(t, n - t - 1):
                tmp = matrix[t][i]
                matrix[t][i] = matrix[n - 1 - i][t]
                matrix[n - 1 - i][t] = matrix[n - 1 - t][n - 1 - i]
                matrix[n - 1 - t][n - 1 - i] = matrix[i][n - 1 - t]
                matrix[i][n - 1 - t] = tmp


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#
