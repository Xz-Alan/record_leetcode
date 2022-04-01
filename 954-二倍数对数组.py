import math
from typing import Counter, List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 直接排序-最坏情况
        # arr.sort(key=lambda x: (-abs(x), -x))
        # match = []
        # for num in arr:
        #     if match and 2*num == match[0]:
        #         match.pop(0)
        #     else:
        #         match.append(num)
        # return len(match) == 0
        # 哈希表排序
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2*x] < cnt[x]:
                return False
            cnt[2*x] -= cnt[x]
        return True


arr = [3, 1, 3, 6]
sol = Solution().canReorderDoubled(arr)
print(sol)
