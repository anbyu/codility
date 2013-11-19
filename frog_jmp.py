def solution(X, Y, D):
    a = Y - X
    r = a // D
    return r if a % D == 0 else r + 1
