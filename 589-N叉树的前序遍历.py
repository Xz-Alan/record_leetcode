from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(cur: 'Node'):
            if not cur:
                return
            res.append(cur.val)
            for tree in cur.children:
                dfs(tree)

        res = []
        dfs(root)
        return res
