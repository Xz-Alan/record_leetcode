class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res=min(self.res,root.val-self.pre)
            self.pre=root.val
            dfs(root.right)
            
        self.pre=float('-inf')
        self.res=float('inf')
        dfs(root)
        return self.res
