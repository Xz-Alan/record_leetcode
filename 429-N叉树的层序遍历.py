from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            sz = len(que)
            res = []
            for _ in range(sz):
                cur = que.popleft()
                res.append(cur.val)
                for tree in cur.children:
                    que.append(tree)
            result.append(res)
        return result
