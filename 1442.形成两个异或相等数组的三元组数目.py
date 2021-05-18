#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#

# @lc code=start
from typing import Counter


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        '''
        # i到k的连续异或等于0即可
        for i in range(n):
            xor = arr[i]
            for k in range(i + 1, n):
                xor ^= arr[k]
                if xor == 0:
                    count += k - i
        '''
        # 前缀和
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)
        '''
        # 双循环 s[i] == s[k+1]
        for i in range(n):
            for k in range(i + 1, n):
                if s[i] == s[k+1]:
                    count += k - i
        '''
        # 哈希表
        cnt, total = Counter(), Counter()
        for k in range(n):
            if s[k + 1] in cnt:
                count += cnt[s[k + 1]] * k - total[s[k + 1]]
            cnt[s[k]] += 1
            total[s[k]] += k
        return count
# @lc code=end

