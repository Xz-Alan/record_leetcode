from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for ch in ops:
            if ch == '+':
                res.append(res[-1]+res[-2])
            elif ch == 'D':
                res.append(2*res[-1])
            elif ch == 'C':
                res.pop()
            else:
                res.append(int(ch))
        return sum(res)


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
sol = Solution().calPoints(ops)
print(sol)
