#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        # 两次二分
        row_target = bisect.bisect_right(col0, target) - 1
        i = bisect.bisect_left(matrix[row_target], target)
        if i < n and matrix[row_target][i] == target:
            return True
        else:
            return False
# @lc code=end

