from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # 前缀和
        # if time > 2 * len(security) + 1:
        #     return []
        # if time == 0:
        #     return list(range(len(security)))
        # res = []
        # left = right = 0
        # for i in range(1, len(security) - time):
        #     if security[i] <= security[i-1]:
        #         left += 1
        #     else:
        #         left = 0
        #     if security[i+time-1] <= security[i+time]:
        #         right += 1
        #     else:
        #         right = 0
        #     if left >= time and right >= time:
        #         res.append(i)
        # return res
        # 动态规划
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                right[n-i-1] = right[n-i] + 1
        return [i for i in range(time, n-time) if left[i] >= time and right[i] >= time]


security = [5, 3, 3, 3, 5, 6, 2]
time = 2
sol = Solution().goodDaysToRobBank(security, time)
print(sol)
