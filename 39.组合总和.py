#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(begin, combine, target):
            if target == 0:
                res.append(combine)
                return
            for index in range(begin, size):
                diff = target - candidates[index]
                if diff < 0:
                    break
                dfs(index, combine + [candidates[index]], diff)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        combine = []
        dfs(0, combine, target)
        return res
# @lc code=end

