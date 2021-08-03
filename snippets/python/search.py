
def binary_search(arr: list, key: int):
    """ 二分探索 """
    def is_ok(i: int):
        return arr[i] > key

    left = -1
    right = len(arr)

    while right - left > 1:
        mid = left + (right - left) // 2

        if is_ok(mid):
            right = mid
        else:
            left = mid

    return right