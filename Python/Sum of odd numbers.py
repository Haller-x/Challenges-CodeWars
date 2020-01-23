def row_sum_odd_numbers(n):
    start = n * (n - 1) + 1
    total = 0
    for i in range(n):
        total += start
        start += 2
    return total