#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30402
#
# [54] 螺旋矩阵
#

# @lc code=start


DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):  # 一共走 mn 步
            ans.append(matrix[i][j])
            matrix[i][j] = None  # 标记，表示已经访问过（已经加入答案）
            x, y = i + DIRS[di][0], j + DIRS[di][1]  # 下一步的位置
            # 如果 (x, y) 出界或者已经访问过
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4  # 右转 90°
            i += DIRS[di][0]
            j += DIRS[di][1]  # 走一步
        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#
