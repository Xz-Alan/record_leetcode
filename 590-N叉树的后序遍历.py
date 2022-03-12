from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(cur: 'Node'):
            if not cur:
                return
            for tree in cur.children:
                dfs(tree)
            res.append(cur.val)

        res = []
        dfs(root)
        return res
