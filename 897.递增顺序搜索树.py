#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        self.traver(root)
        # 链表哨兵节点
        dummy = TreeNode()
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
        
    def traver(self, root):
        if not root:
            return
        self.traver(root.left)
        self.res.append(root)
        self.traver(root.right)

# @lc code=end

