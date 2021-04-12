import heapq
n = 10
factors = [2, 3, 5]
seen = {1}
heap = [1]

for i in range(n - 1):
    curr = heapq.heappop(heap)
    print('curr:', curr)
    for factor in factors:
        if (nxt := curr * factor) not in seen:
            print(nxt)
            seen.add(nxt)
            print(seen)
            heapq.heappush(heap, nxt)
            print(heap)
            # input("____________________")

print(heapq.heappop(heap))
