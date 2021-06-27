import numpy as np

def rot(p: np.ndarray, c: np.ndarray, theta: float):
    """ 点 p: np.ndarray(2x1) を 点 c: np.ndarray(2x1) を中心に theta[rad] 回転する """
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])
    return r @ (p - c) + c


def barycenter(poses: list):
    """ poses: List[np.ndarray] の重心 """
    return np.sum(poses) / len(poses)