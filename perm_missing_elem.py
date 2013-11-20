def solution(A):
    N = len(A)
    s = sum(A)
    return (1 + N + 1) * (N + 1) / 2 - s
