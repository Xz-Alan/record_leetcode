class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        res = []
        num = abs(num)
        while num:
            res.append(str(num % 7))
            num //= 7
        if negative:
            res.append('-')
        return "".join(reversed(res))


num = 100
sol = Solution().convertToBase7(num)
print(sol)
