if __name__ == "__main__":
    inf = 10 ** 8
    n = int(input())
    x, y = list(map(int, input().split()))

    # [弁当][たこ焼き][たいやき]
    dp =[[[inf for _ in range(y)] for _ in range(x)] for _ in range(n + 1)]
    
    w = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        w.append((a, b))

    dp[0][0][0] = 0

    # TODO: solve