import heapq

q = int(input())

plus = [0]
arr = []
for i in range(q):
    p = 0
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(arr, (query[1] - plus[i], i + 1))
    elif query[0] == 2:
        p = query[1]
    else:
        v = heapq.heappop(arr)
        # print(f'{v[1]} -> {i}')
        # print(v[0] + (plus[i] - plus[v[1]]))
        print(v[0] + plus[i])
    # print(arr)

    plus.append(plus[-1] + p)

# print(plus)