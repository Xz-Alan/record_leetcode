#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = 2 * r - 2
        res = []
        for i in range(r):
            for j in range(0, n-i, t):
                res.append(s[j+i])
                if 0 < i < r-1 and j + t - i < n:
                    res.append(s[j+t-i])
        return "".join(res)


# @lc code=end

s = "PAYPALISHIRING"
numRows = 3
sol = Solution().convert(s, numRows)
print(sol)
