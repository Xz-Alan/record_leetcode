#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(begin, combine, target):
            if target == 0:
                res.append(combine)
                return
            for index in range(begin, size):
                diff = target - candidates[index]
                if diff < 0:
                    break
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue
                dfs(index + 1, combine + [candidates[index]], diff)
                
        
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        combine = []
        dfs(0, combine, target)
        return res
# @lc code=end

