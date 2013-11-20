def solution(A):
    N = len(A)
    count = 0
    for i in xrange(N):
        if count == 0:
            x = A[i]
            count = 1
        elif x == A[i]:
            count += 1
        else:
            count -= 1
    count = 0
    for i in xrange(N):
        if A[i] == x:
            count += 1
            pos = i
    return pos if count > N // 2 else -1
