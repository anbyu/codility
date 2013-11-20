def solution(A):
    A.sort()
    for i in xrange(1, len(A) - 1):
        if A[i - 1] + A[i] > A[i + 1]:
            return 1
    return 0
