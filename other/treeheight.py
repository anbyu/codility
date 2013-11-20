def solution(T):
    height = 0
    s = [T]
    T.x = 0
    while len(s) != 0:
        c = s.pop()
        if c.x > height:
            height = c.x
        if c.l is not None:
            c.l.x = c.x + 1
            s.append(c.l)
        if c.r is not None:
            c.r.x = c.x + 1
            s.append(c.r)
    return height
