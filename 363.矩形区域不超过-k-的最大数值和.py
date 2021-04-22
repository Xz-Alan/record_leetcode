#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            nums = [0] * row
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                cur = 0
                min_sort = [0]
                for num in nums:
                    cur += num
                    idx = bisect.bisect_left(min_sort, cur - k)
                    if idx < len(min_sort):
                        res = max(cur - min_sort[idx], res)
                    bisect.insort_left(min_sort, cur)
        return res
# @lc code=end

