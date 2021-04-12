from functools import cmp_to_key
nums = [10, 2, 9, 0]
nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y : int(y + x) - int(x + y)))
# lambda x, y : 1 if x + y < y + x else -1