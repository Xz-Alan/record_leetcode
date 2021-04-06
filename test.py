def dfs(candidates, begin, size, combine, res, target):
    if target == 0:
        res.append(combine)
        return
    for index in range(begin,size):
        diff = target - candidates[index]
        if diff < 0:
            break
        dfs(candidates, index, size, combine + [candidates[index]], res, diff)

candidates = [2,3,6,7]
target = 7
size = len(candidates)
if size == 0:
    print([])
candidates.sort()
res = []
combine = []
dfs(candidates, 0, size, combine, res, target)
print(res)