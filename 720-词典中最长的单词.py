from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ""
        hash = {""}
        # str不能取负, 因此先长度降序，字典升序，再反转
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        for word in words:
            if word[:-1] in hash:
                res = word
                hash.add(word)
        return res
