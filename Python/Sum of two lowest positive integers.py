def sum_two_smallest_numbers(numbers):
    numbers.sort(reverse=True)
    a = numbers.pop()
    b = numbers.pop()
    return a+b