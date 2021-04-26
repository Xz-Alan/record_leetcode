#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            day, cur = 1, 0
            for weight in weights:
                cur += weight
                if cur > mid:
                    day += 1
                    cur = weight
            if day > D:
                left = mid + 1
            else:
                right = mid
        return left

# @lc code=end

