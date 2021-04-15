from typing import List
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

class Solution_1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
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
        return min([res[i + 1] - res[i] for i in range(len(res) - 1)])


class Solution_2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)

        res = []
        dfs(root)
        return min([res[i + 1] - res[i] for i in range(len(res) - 1)])

root = genTree([4,2,6,1,3])
print(Solution_1().preorderTraversal(root))