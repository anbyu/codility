def solution(H):
    N = len(H)
    stack = [H[0]]
    pieces = 1
    
    for i in xrange(1, N):
        h = H[i]
        while len(stack) > 0 and h < stack[-1]:
            stack.pop()
        if len(stack) == 0 or h != stack[-1]:        
            stack.append(h)
            pieces += 1
            
    return pieces
    