#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30402
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = any(matrix[0][i] == 0 for i in range(len(matrix[0])))
        col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        print(row_zero, col_zero)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(matrix)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


# @lc code=end


#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#
