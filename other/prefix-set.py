def solution(A):
    N = len(A)
    
    present = [False] * N
    left = 0
    
    for a in A:
        if not present[a]:
            present[a] = True
            left += 1
            
    for i in xrange(N):
        a = A[i]
        if present[a]:
            present[a] = False
            left -= 1
        if left == 0:
            return i
    return -1
