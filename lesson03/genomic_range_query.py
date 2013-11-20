def solution(S, P, Q):
    ids = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
    
    sums = [[0, 0, 0, 0]]
    for i in xrange(len(S)):
        sums.append(list(sums[-1]))
        id = ids[S[i]]
        sums[-1][id] = sums[-2][id] + 1
        
    for i in xrange(len(P)):
        for j in range(4):
            if sums[Q[i] + 1][j] - sums[P[i]][j] > 0:
                P[i] = j + 1
                break
                
    return P
