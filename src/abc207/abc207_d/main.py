import numpy as np
# from icecream import ic

def barycenter(poses: list):
    """ poses: List[np.ndarray] の重心 """
    return np.average(np.array(poses), axis=0)


def rot(p: np.ndarray, theta: float, c: np.ndarray = np.zeros((2, 1))):
    """ 点 p: np.ndarray(2x1) を 点 c: np.ndarray(2x1) を中心に theta[rad] 回転する """
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])
    return r @ (p - c) + c

def match(n, s: list, t: list):
    """ O(n^3) """
    atol = 1e-6
    for i in range(n):
        # assume s[0] map to t[i] by rotating θ
        theta = (np.arctan2(t[i][1], t[i][0]) - np.arctan2(s[0][1], s[0][0])).item()
        res = True
        for j in range(n):
            # s[j] -> ∃t[k]
            sj = rot(s[j], theta)
            res &= any(map(lambda tk: np.all(np.isclose(sj, tk, atol=atol)), t))
        
        if (res):
            return True
    
    return False

def solve(n, s, t):
    s -= barycenter(s)
    t -= barycenter(t)
    return match(n, s, t)

if __name__ == "__main__":
    # ic.disable()

    n = int(input())
    s, t = [], []
    for i in range(n):
        a, b = list(map(int, input().split()))
        p = np.reshape(np.array([a, b]), (2, 1))
        s.append(p)

    for i in range(n):
        c, d = list(map(int, input().split()))
        p = np.reshape(np.array([c, d]), (2, 1))
        t.append(p)

    print('Yes' if solve(n, s, t) else 'No')