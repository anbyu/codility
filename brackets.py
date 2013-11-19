def solution(S):
    stack = []
    pairs = { '{': '}', '[': ']', '(': ')' }
    
    for c in S:
        if c in pairs:
            stack.append(c)
        elif len(stack) > 0 and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return 0
    return 1 if len(stack) == 0 else 0
