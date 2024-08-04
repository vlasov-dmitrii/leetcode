import math

def minEatingSpeed(pile, h):
    l = 1 
    r = max(pile)
    res = r
    while l <= r:
        k = (l + r) // 2
        time = 0
        for p in pile:
            time += math.ceil(float(p) / k)
        if time <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res
