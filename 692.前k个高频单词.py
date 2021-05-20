#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        return sorted(d.keys(), key=cmp_to_key(lambda x, y: int(d[x] < d[y] or (d[x] == d[y] and x > y)) - 0.5))[:k]
# @lc code=end

