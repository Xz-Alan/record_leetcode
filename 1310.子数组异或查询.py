#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for num in arr:
            xors.append(xors[-1] ^ num)
        # xors = list(accumulate([0] + arr, xor))
        return [xors[left] ^ xors[right + 1] for left, right in queries]


# @lc code=end

