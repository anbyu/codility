def solution(N, A):
    counters = [ 0 ] * N
    m = 0
    last_m = 0
    for a in A:
        if a == N + 1:
            last_m = m
        else:
            c = counters[a - 1]
            if c < last_m:
                c = last_m
            c += 1
            counters[a - 1] = c
            if c > m:
                m = c
    for i in xrange(N):
        if counters[i] < last_m:
            counters[i] = last_m
    return counters
