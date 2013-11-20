def solution(A):
    MAX = 10 ** 9
    add = 0
    total = 0
    for a in A:
        if a == 0:
            add += 1
        else:
            total += add
            if total > MAX:
                return -1
    return total
    