def expression_matter(a, b, c):
    list = [a * (b + c), a * b * c, a + b * c, (a + b) * c, a + b + c]

    xx = sorted(list)
    yy = xx.pop()
    return yy