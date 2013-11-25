from collections import deque

def add(graph, u, v, dist):
    edge = (v, dist)
    if not u in graph:
        graph[u] = [edge]
    else:
        graph[u].append(edge)

        
def solution(A, B, C, D):
    N, M = len(D), len(A)
    MAX = 10 ** 9 + 1
    
    graph = {}
    for i in xrange(M):
        u, v, dist = A[i], B[i], C[i]
        add(graph, u, v, dist)
        add(graph, v, u, dist)
        
    queue = deque([0])
    dists = [MAX] * N
    dists[0] = 0
    
    while len(queue) > 0:
        u = queue.popleft()
        for v, dist in graph.get(u, []):
            if dists[u] + dist < dists[v]:
                dists[v] = dists[u] + dist
                queue.append(v)

    ans = MAX
    for i in xrange(N):
        d = dists[i]
        if d < ans and d <= D[i]:
            ans = dists[i]
            
    return ans if ans < MAX else -1
