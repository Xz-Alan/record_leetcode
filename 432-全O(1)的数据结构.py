from collections import Counter


# 超时
class AllOne:

    def __init__(self):
        self.count = Counter()

    def inc(self, key: str) -> None:
        self.count.update(Counter([key]))

    def dec(self, key: str) -> None:
        self.count[key] -= 1
        if self.count[key] == 0:
            del self.count[key]

    def getMaxKey(self) -> str:
        if len(self.count) == 0:
            return ""
        return self.count.most_common(1)[0][0]

    def getMinKey(self) -> str:
        if len(self.count) == 0:
            return ""
        return self.count.most_common()[-1][0]
