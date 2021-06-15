import numpy as np

def rot(p, c, theta):
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])
    return r @ (p - c) + c

if __name__ == '__main__':
    n = int(input())
    p0 = list(map(int, input().split()))
    p0 = np.reshape(np.array(p0), (2, 1))
    pm = list(map(int, input().split()))
    pm = np.reshape(np.array(pm), (2, 1))

    p1 = rot(p0, (p0 + pm) / 2, 2 * np.pi / n)
    print(p1[0][0], p1[1][0])