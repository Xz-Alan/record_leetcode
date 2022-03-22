class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = count_b = num_a = num_b = 0
        for ch in colors:
            if ch == "A":
                count_b = 0
                count_a += 1
                if count_a >= 3:
                    num_a += 1
            else:
                count_a = 0
                count_b += 1
                if count_b >= 3:
                    num_b += 1
        return num_a > num_b
