#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

# @lc code=start
class Solution:
    def clumsy(self, N: int) -> int:
        '''
        # 遇到乘除立即算，遇到加减先入栈
        op = 0
        stack = [N]
        for i in range(N-1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / i))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            op = (op + 1) % 4
        return sum(stack)
        '''
        # 归纳法
        temp = [0, 1, 2, 6, 7]
        if N <= 4:
            return temp[N]
        if N % 4 == 0:
            return N + 1
        elif N % 4 == 3:
            return N - 1
        else:
            return N + 2
# @lc code=end

