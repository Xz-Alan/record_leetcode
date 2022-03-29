class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def find_largest(ch: str):
            res, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                res = max(res, right - left + 1)
            return res
        return max(find_largest('T'), find_largest('F'))
