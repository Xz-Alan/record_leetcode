#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                stack[-2].extend(reversed(stack.pop()))
            else:
                stack[-1].append(c)
        return "".join(stack[0])

# @lc code=end

