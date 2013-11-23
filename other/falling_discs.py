def solution(A, B):
    N, M = len(A), len(B)
    
    for i in xrange(1, N):
        if A[i] > A[i - 1]:
            A[i] = A[i - 1]
            
    i, j = N - 1, 0
    total = 0
    while i >= 0 and j < M:
        if B[j] <= A[i]:
            j += 1
            total += 1
        i -= 1
        
    return total
