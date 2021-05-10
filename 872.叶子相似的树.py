#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode, res: List):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            else:
                dfs(root.left, res)
                dfs(root.right, res)
        
        res1 = []
        res2 = []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2
# @lc code=end

