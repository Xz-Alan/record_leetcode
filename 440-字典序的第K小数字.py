class Solution:
    def getStep(self, n, cur):
        step, first, last = 0, cur, cur
        while first <= n:
            step += min(n, last) - first + 1
            first *= 10
            last = last*10 + 9
        return step

    def findKthNumber(self, n: int, k: int) -> int:
        # 暴力超时
        # nums = [str(i) for i in range(1, n+1)]
        # nums.sort(key=lambda x: x)
        # return int(nums[k-1])
        # 字典树思想
        cur = 1
        k -= 1
        while k:
            step = self.getStep(n, cur)
            if step <= k:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
