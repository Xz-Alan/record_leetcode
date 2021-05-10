from sortedcontainers import SortedList     # 有序列表
from typing import List
import bisect       # 二分
from collections import Counter     # 计数

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def genTree(arr):
    def gen(arr, i):
        if i < len(arr):
            tn = TreeNode(arr[i]) if arr[i] is not None else None
            if tn is not None:
                tn.left = gen(arr, 2 * i + 1)
                tn.right = gen(arr, 2 * i + 2)
            return tn
    return gen(arr, 0)

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

root1 = [1,2,3]
root2 = [1,3,2]
print(Solution().leafSimilar(genTree(root1), genTree(root2)))