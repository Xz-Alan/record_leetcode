#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        '''
        # 迭代
        res = []
        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not cur: continue
            if flag == 0:
                # # 中序，标记法
                stack.append((0, cur.right))
                stack.append((1, cur))
                stack.append((0, cur.left))
            else:
                res.append(cur.val)
        '''
        # 递归
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)

        res = []
        dfs(root)
        return min([res[i + 1] - res[i] for i in range(len(res) - 1)])
# @lc code=end

