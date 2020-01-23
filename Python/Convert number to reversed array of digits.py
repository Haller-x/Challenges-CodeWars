def digitize(n):
    n = str(n)
    x = list(n)
    x.reverse()
    return [int(i) for i in x]