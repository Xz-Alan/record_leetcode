#
# @lc app=leetcode.cn id=1744 lang=python3
#
# [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
#

# @lc code=start
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        _sum = list(accumulate(candiesCount))
        ans = []
        for ftype, fday, fcap in queries:
            x1 = fday + 1
            y1 = (fday + 1) * fcap
            x2 = 1 if ftype == 0 else _sum[ftype - 1] + 1
            y2 = _sum[ftype]

            ans.append(not(x1 > y2 or y1 < x2))
        return ans
# @lc code=end

