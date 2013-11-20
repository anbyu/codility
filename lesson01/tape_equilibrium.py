def solution(A):
    N = len(A)
    
    sums = [A[0]] * N
    total = A[0]
    for i in xrange(1, N):
        a = A[i]
        sums[i] = sums[i - 1] + a
        total += a
    
    min_diff = abs(sums[0] - (total - sums[0]))
    for i in xrange(1, N - 1):
        s = sums[i]
        diff = abs(s - (total - s))
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
