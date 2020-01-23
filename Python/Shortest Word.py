def find_short(s):
    s = s.split()
    x = min(s, key=len)
    y = len(x)
    return y