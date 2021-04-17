#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if len(window) == k + 1:
                window.remove(nums[i - k - 1])
            window.add(nums[i])
            index = window.bisect_left(nums[i])
            if index > 0 and window[index] - window[index - 1] <= t:
                return True
            if index < len(window) - 1 and window[index + 1] - window[index] <= t:
                return True
        return False

# @lc code=end

