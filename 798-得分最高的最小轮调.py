from typing import List
from collections import Counter


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        # 暴力超时
        # count = {}
        # for i in range(n):
        #     for ss in range(i+1, n-nums[i]+i+1):
        #         ss %= n
        #         if ss not in count:
        #             count[ss] = 1
        #         else:
        #             count[ss] += 1
        # return sorted(count, key=lambda x: (-count[x], x))[0]
        # 差分数组 diff[i] = count[i] - count[i-1]
        diffs = [0] * n
        for i in range(n):
            low = (i+1) % n
            high = (n-nums[i]+i+1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        # 遍历求前缀和得到max_count[i]
        max_count, idx, count = 0, 0, 0
        for i, diff in enumerate(diffs):
            count += diff
            if count > max_count:
                idx, max_count = i, count
        return idx


nums = [2, 3, 1, 4, 0]
sol = Solution().bestRotation(nums)
print(sol)
