#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, combine, res, target):
            if target == 0:
                res.append(combine)
                return
            for index in range(begin, size):
                diff = target - candidates[index]
                if diff < 0:
                    break
                dfs(candidates, index, size, combine + [candidates[index]], res, diff)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        combine = []
        dfs(candidates, 0, size, combine, res, target)
        return res
# @lc code=end

