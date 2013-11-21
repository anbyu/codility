def solution(A):
    s = set()
    for a in A:
        s.add(abs(a))
    return len(s)
