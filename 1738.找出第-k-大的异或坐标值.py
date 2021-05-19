#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#

# @lc code=start
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # 二维前缀和
        m, n = len(matrix), len(matrix[0])
        xor = [[0] * (n + 1) for _ in range(m + 1)]
        result = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xor[i][j] = xor[i-1][j] ^ xor[i][j-1] ^ xor[i-1][j-1] ^ matrix[i-1][j-1]
                result.append(xor[i][j])
        result.sort()
        return result[-k]
# @lc code=end

