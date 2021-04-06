#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l, r= j+1, n-1 
                while l<r:
                    current = nums[i] + nums[j] + nums[l] + nums[r]
                    if current == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l += 1
                        while l<r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif current > target:
                        r -= 1
                    else:
                        l += 1
        return res


# @lc code=end

