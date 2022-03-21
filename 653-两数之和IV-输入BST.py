from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # dfs+双指针
        # def dfs(cur: TreeNode):
        #     if not cur:
        #         return
        #     dfs(cur.left)
        #     nums.append(cur.val)
        #     dfs(cur.right)

        # nums = []
        # dfs(root)
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     total = nums[left]+nums[right]
        #     if total > k:
        #         right -= 1
        #     elif total < k:
        #         left += 1
        #     else:
        #         return True
        # return False
        # 迭代+哈希
        hashset = set()
        que = deque([root])
        while que:
            cur = que.popleft(que)
            if k-cur.val in hashset:
                return True
            hashset.add(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        return False
