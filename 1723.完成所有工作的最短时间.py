#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(mid):
            arr = sorted(jobs)
            groups = [0] * k
            if arr[-1] > mid: return False
            return search(arr, groups, mid)
        
        def search(arr, groups, mid):
            if not arr: return True
            v = arr.pop()
            for i, group in enumerate(groups):
                if group + v <= mid:
                    groups[i] += v
                    if search(arr, groups, mid): return True
                    groups[i] -= v
                if not group: break
            arr.append(v)
            return False

        # jobs.sort()
        left, right = max(jobs), sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

