import heapq

n, m = map(int, input().split())
a = list(map(lambda e: int(e) * -1, input().split()))
heapq.heapify(a)

for i in range(m):
    mx = -heapq.heappop(a)
    heapq.heappush(a, -(mx // 2))

print(-sum(a))