def solution(A):
    N = len(A)
    bitmap = [0] * N
    for i in xrange(N):
        a = A[i]
        if a > N or bitmap[a - 1] == 1:
            return 0
        else:
            bitmap[a - 1] = 1
    return 1
