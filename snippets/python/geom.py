import numpy as np

def rot_np(p: np.ndarray, c: np.ndarray, theta: float):
    """ 点 p: np.ndarray(2x1) を 点 c: np.ndarray(2x1) を中心に theta[rad] 回転する """
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])
    return r @ (p - c) + c

import math
import cmath

def rot(p: list, c: list, theta: float):
    """ 点 p: np.ndarray(2x1) を 点 c: np.ndarray(2x1) を中心に theta[rad] 回転する """
    x, y = p[0] - c[0], p[1] - c[1]
    rx = math.cos(theta) * x - math.sin(theta) * y
    ry = math.sin(theta) * x + math.cos(theta) * y
    return (rx + c[0], ry + c[1])


def rot_c(p: complex, c: complex, theta: float):
    """ 複素数 """
    return ((p - c) * (math.cos(theta) + 1j * math.sin(theta))) + c

def angle(p: complex):
    """ 偏角 """
    return cmath.phase(p)