def solution(A):
    A.sort()
    top = A[-1] * A[-2] * A[-3]
    bot = A[0] * A[1] * A[-1]
    return top if top > bot else bot        
