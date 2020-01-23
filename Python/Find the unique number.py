def find_uniq(arr):
    arr.sort()
    for i in arr:
        if arr[0] == arr[1]:
            x = arr[len(arr)-1]
            return x
        elif arr[len(arr)-1] == arr[len(arr)-2]:
            x = arr[0]
            return x