#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        best = 10**7
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            #--------------------------------------------------
            max_target = nums[i] + nums[n-2] + nums[n-1]
            min_target = nums[i] + nums[i+1] + nums[i+2]
            if min_target > target:
                if abs(min_target - target) < abs(best - target):
                    best = min_target
                break
            elif max_target < target:
                if abs(max_target - target) < abs(best - target):
                    best = max_target
                continue
            #--------------------------------------------------
            l, r = i+1, n-1
            while l < r:
                s = nums [i] + nums[l] + nums[r]
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    l += 1
                    while l < r and nums[l]==nums[l-1]:
                        l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r]==nums[r+1]:
                        r -= 1
                else:
                    return target
        return best
# @lc code=end

