from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 暴力
        # res = 0
        # if len(nums) <= 1:
        #     return res
        # for i in range(len(nums)):
        #     min_v, max_v = float('inf'), -float('inf')
        #     for j in range(i, len(nums)):
        #         min_v = min(nums[j], min_v)
        #         max_v = max(nums[j], max_v)
        #         res += max_v - min_v
        # return res
        # 单调栈
        n = len(nums)

        min_l, max_l = [0]*n, [0]*n
        min_stack, max_stack = [], []
        for i, num in enumerate(nums):
            # 单调递增栈，得到左侧最近的比num小的数
            while min_stack and num < nums[min_stack[-1]]:
                min_stack.pop()
            min_l[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)
            # 单调递减栈，得到左侧最近的比num大的数
            while max_stack and num >= nums[max_stack[-1]]:
                max_stack.pop()
            max_l[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)

        min_r, max_r = [0]*n, [0]*n
        min_stack, max_stack = [], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            # 单调递增栈，得到右侧最近的比num小的数
            while min_stack and num <= nums[min_stack[-1]]:
                min_stack.pop()
            min_r[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)
            # 单调递减栈，得到右侧最近的比num大的数
            while max_stack and num > nums[max_stack[-1]]:
                max_stack.pop()
            max_r[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        min_sum = max_sum = 0
        for i, num in enumerate(nums):
            min_sum += (i - min_l[i]) * (min_r[i] - i) * num
            max_sum += (i - max_l[i]) * (max_r[i] - i) * num
        return max_sum - min_sum


nums = [4, -2, -3, 4, 1]
sol = Solution().subArrayRanges(nums)
print(sol)
