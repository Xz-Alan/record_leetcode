from typing import List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = [0]*n  # 记录每个点的度
        map = defaultdict(list)  # 存储邻居节点
        # 初始化每个节点的度和邻居
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        # 记录度为1的叶子节点，加入队列中，从叶子节点往上遍历
        que = deque()
        for i in range(n):
            if degree[i] == 1:
                que.append(i)
        # 每次遍历叶子节点，每一轮将叶子节点从树上删除后将新的叶子节点入队进行下一轮遍历
        while que:
            res = []
            length = len(que)
            for i in range(length):
                cur = que.popleft()
                res.append(cur)
                neighbors = map[cur]
                for neighbor in neighbors:
                    # 将叶子节点的邻居节点的度减一，若是新的叶子节点，则入队
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        que.append(neighbor)
        # 返回最后一轮的叶子节点，就是最小高度树的根节点
        return res
