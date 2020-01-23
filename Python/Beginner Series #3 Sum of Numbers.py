def get_sum(a, b):
    if b > a:
        x = range(a, b + 1)
        y = sum(x)
    else:
        x = range(b, a + 1)
        y = sum(x)
    return y
