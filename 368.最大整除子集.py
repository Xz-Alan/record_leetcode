#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # 1. 动态规划找出最大子集的个数、最大子集中的最大整数
        dp = [1] * len(nums)
        max_size = 1
        max_val = dp[0]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]
        # 2. 倒推获得最大子集输出
        res = []
        if max_size == 1:
            return [nums[0]]
        for i in range(len(nums)-1 , -1, -1):
            if max_size > 0 and dp[i] == max_size and max_val % nums[i] == 0:
                res.append(nums[i])
                max_val = nums[i]
                max_size -= 1
        return res
        # 字典dp
        '''
        nums.sort()
        dp = dict()
        ans = []
        for num in nums:
            max_list = []
            for key, val in dp.items():
                if num % key == 0 and len(val) > len(max_list):
                    max_list = val
            if not max_list:
                dp[num] = [num]
            else:
                dp[num] = max_list + [num]
            if len(dp[num]) > len(ans):
                ans = dp[num]
        return ans
        '''
            
# @lc code=end

