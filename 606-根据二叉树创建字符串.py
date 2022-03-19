from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        stack = [root]
        vis = set()
        while stack:
            cur = stack[-1]
            if cur in vis:
                if cur != root:
                    res += ")"
                stack.pop()
            else:
                vis.add(cur)
                if cur != root:
                    res += "("
                res += str(cur.val)
                if not cur.left and cur.right:
                    res += "()"
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res
