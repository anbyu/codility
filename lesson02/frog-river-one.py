def solution(X, A):
    N = len(A)
    has_leaf = [False] * X
    left = X
    
    for i in xrange(N):
        a = A[i]
        if not has_leaf[a - 1]:
            has_leaf[a - 1] = True
            left -= 1
        if left == 0:
            return i
    return -1
