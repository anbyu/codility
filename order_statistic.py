from random import randint

def order_statistic(A, n, a, b):
    N = b - a
    ni = a + n - 1
    p = randint(a, b - 1)
    print p, n, a, b, A
    A[p], A[a] = A[a], A[p]
    p = a
    pivot = A[a]
    for i in xrange(a + 1, b):
        if A[i] < pivot:
            p += 1
            A[i], A[p] = A[p], A[i]
    A[p], A[a] = A[a], A[p]
    if p == ni:
        return pivot, ni
    elif p < ni:
        return order_statistic(A, n - p - 1, p + 1, b)
    else:
        return order_statistic(A, n, a, p)

def solution(A):
    N = len(A)
    c, ci = order_statistic(A, N / 2, 0, N)
    count = 0
    for i in xrange(N):
        if A[i] == c:
            occurence = i
            count += 1
    if count > N / 2:
        return ci
    return -1
    
print order_statistic([5, 6, 1, 4], 2, 0, 4)
