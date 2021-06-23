a, b, x = list(map(int, input().split()))

def ks_in_range(a: int, b: int, k: int):
    """
    count mult of k in [a, b]
    """
    r = a % k
    m = a - r
    answer = (b - m) // k + 1
    if r > 0:
        answer -= 1
    return answer

print(ks_in_range(a, b, x))