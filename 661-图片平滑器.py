from typing import List
import numpy as np


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        h, w = len(img), len(img[0])
        new_img = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                total = count = 0
                for x in range(max(i-1, 0), min(i+2, h)):
                    for y in range(max(j-1, 0), min(j+2, w)):
                        total += img[x][y]
                        count += 1
                new_img[i][j] = total // count
        return new_img


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
Solution().imageSmoother(img)
