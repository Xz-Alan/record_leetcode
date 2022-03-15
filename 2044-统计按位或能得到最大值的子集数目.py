from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val, res, n = 0, 0, len(nums)
        for i in range(1 << n):
            # 用n比特数表示2^n个子集，第i位表示数组第i个元素的选取状态
            tmp = 0
            for j in range(n):
                # 通过移位来判断第j个元素是否被选取
                if (i >> j) & 1 == 1:
                    tmp |= nums[j]
            if tmp == max_val:
                res += 1
            elif tmp > max_val:
                max_val = tmp
                res = 1
        return res


nums = [3, 1]
sol = Solution().countMaxOrSubsets(nums)
print(sol)
