from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, left, sum = 0, 0, 0
        for right in range(len(nums)):
            sum += nums[right] != 1
            while sum > k:
                sum -= nums[left] != 1
                left += 1
            res = max(res, right - left + 1)
        return res
