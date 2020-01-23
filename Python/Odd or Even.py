def oddOrEven(arr):
    sum = 0
    for num in arr:
        if arr == []:
            return 'even'
        sum += num
    if sum%2 == 0:
        return 'even'
    elif sum%2 != 0:
        return 'odd'