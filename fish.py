def solution(A, B):
    N = len(A)
    left = 0
    i = 0
    while i < N and B[i] == 0:
        left += 1
        i += 1
    
    stack = []
    for i in xrange(i, N):
        size, direction = A[i], B[i]
        if direction == 1:
            stack.append(size)
        else:
            while len(stack) > 0 and size > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                left += 1
     
    return left + len(stack)
