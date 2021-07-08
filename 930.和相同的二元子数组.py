#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 前缀和
        presum = ans = 0
        n = len(nums)
        hashmap = Counter({0:1})   # defaultdict(int, {0:1})
        for num in nums:
            presum += num
            ans += hashmap[presum - goal]
            hashmap[presum] += 1
        return ans
# @lc code=end

