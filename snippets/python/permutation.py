from typing import List, Tuple

# <https://teratail.com/questions/184042>
def cyclic_form(permutation: List[int]) -> List[List[int]]:
    """
    順列を置換の積で表す
    """
    cycles = []
    unvisited = permutation.copy()
    while unvisited:
        j = i = unvisited.pop()
        cycle = [i]
        while True:
            j = permutation[j]
            if j == i:
                break 
            cycle.append(j)
            unvisited.remove(j)
        cycles.append(cycle)

    return cycles

def transpositions(cycles: List[List[int]]) -> List[Tuple[int]]:
    """
    置換を互換の積に分解する
    """
    trans = []
    for c in cycles:
        cycle_len = len(c)
        if cycle_len == 2:
            trans.append(tuple(c))
        elif cycle_len > 2:
            first = c[0]
            for x in c[cycle_len - 1:0:-1]:
                trans.append((first, x))
    return trans

if __name__ == "__main__":
    # (1, 2, 3, 4) -> (2, 3, 4, 1) == (1, 4)(1, 3)(1, 2)
    dst = [1, 2, 3, 0]
    cycles = cyclic_form(dst)
    assert(cycles == [[0, 1, 2, 3]])
    trans = transpositions(cycles)
    assert(trans == [(0, 3), (0, 2), (0, 1)])