from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isselfDividing(num):
            x = num
            while x:
                x, d = divmod(x, 10)
                if d == 0 or num % d:
                    return False
            return True
        res = []
        for i in range(left, right+1):
            if isselfDividing(i):
                res.append(i)
        return res
