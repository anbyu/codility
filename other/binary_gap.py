def solution(N):
    while N % 2 == 0:
        N //= 2
    
    longest = 0
    current = 0
    while N > 0:
        if N % 2 == 1:
            if current > longest:
                longest = current
            current = 0
        else:
            current += 1
        N //= 2
    return longest
