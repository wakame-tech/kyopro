import bisect
from typing import List

def lis(arr: List[int]):
    """
    最長増加部分列
    """
    res = [arr[0]]
    for i in range(len(arr)):
        if res[-1] < arr[i]:
            res.append(arr[i])
        else:
            res[bisect.bisect_left(res, arr[i])] = arr[i]

    return res

def test_lis():
    arr = [1, 3, 5, 2, 4, 6]
    assert(lis(arr) == [1, 2, 4, 6])

test_lis()
