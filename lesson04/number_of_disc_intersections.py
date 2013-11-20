def solution(A):
    MAX = 10 ** 7
    N = len(A)
    points = []
    for i in xrange(N):
        a = A[i]
        points.append((i - a, 0)) # 0 -> left
        points.append((i + a, 1)) # 1 -> right
    points.sort()
    
    intersections = 0
    count = 0
    
    for p in points:
        if p[1] == 0:
            count += 1
        else:
            count -= 1
            intersections += count
            if intersections > MAX:
                return -1

    return intersections
