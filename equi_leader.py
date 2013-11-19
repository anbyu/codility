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
            
    counts = [0] * N
    prev_count = 0
    for i in xrange(N):
        if A[i] == x:
            prev_count += 1
        counts[i] = prev_count
    
    total = counts[-1]
    answer = 0
    if total > N // 2:
        for i in xrange(N):
            count = counts[i]
            if count > (i + 1) // 2 and total - count > (N - i - 1) // 2:
                answer += 1
    
    return answer
